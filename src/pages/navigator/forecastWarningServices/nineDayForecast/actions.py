from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy

from src.apis import call_wxinfo_json_api, call_FND_json, call_wxinfo_json_uc_api
from src.pages.base_actions import BaseActions
from src.pages.navigator.forecastWarningServices.nineDayForecast.locators import NineDayForecastLocators


week_map = {
    'Mon': '星期一',
    'Tue': '星期二',
    'Wed': '星期三',
    'Thu': '星期四',
    'Fri': '星期五',
    'Sat': '星期六',
    'Sun': '星期日'
}

class WeatherInfo(object):
    def __init__(self, date, weekday, range_temp, range_rh, desc, wind_info, psr_text):
        self.date = date
        self.weekday = weekday
        self.range_temp = range_temp
        self.range_rh = range_rh
        self.desc = desc
        self.wind_info = wind_info
        self.psr_text = psr_text


class NineDayForecastActions(BaseActions):
    ndfl = NineDayForecastLocators()

    def open_nine_days_forecast(self):
        self.click_element(self.ndfl.nine_day_forecast_button)

    def get_general_situation_text(self):
        return self.get_text(self.ndfl.general_situation)

    def get_general_situation_from_api(self):
        return (call_wxinfo_json_api()['F9D']['GeneralSituation'],call_wxinfo_json_uc_api()['F9D']['GeneralSituation'])

    def get_days_weather_info_from_api(self):
        resp = call_FND_json()
        FND = resp['DYN_DAT_MINDS_FND']
        days_weather_info = []
        for i in range(1, 10):
            wi = WeatherInfo(
                (datetime.strptime(FND[f'Day{i}ForecastDate']['Value_Eng'], '%Y%m%d').strftime('%-d %b'),datetime.strptime(FND[f'Day{i}ForecastDate']['Value_Eng'], '%Y%m%d').strftime('%m月%d日')),
                (f'({datetime.strptime(FND[f'Day{i}ForecastDate']['Value_Eng'], '%Y%m%d').strftime('%a')})',f'({week_map[datetime.strptime(FND[f'Day{i}ForecastDate']['Value_Eng'], '%Y%m%d').strftime('%a')]})'),
                f'{FND[f'Day{i}MinTemp']['Value_Eng']} - {FND[f'Day{i}MaxTemp']['Value_Eng']}°C',
                f'{FND[f'Day{i}MinRH']['Value_Eng']} - {FND[f'Day{i}MaxRH']['Value_Eng']}%',
                f'{FND[f'Day{i}WxDesc']['Value_Eng']}',
                f'{FND[f'Day{i}WindInfo']['Value_Eng']}',
                f'{FND[f'Day{i}PSR10']['Value_Eng']}',

            )
            days_weather_info.append(wi)
        return days_weather_info

    def get_days_weather_info(self):
        days_weather_info = {}
        while len(days_weather_info) != 9:
            dates = self.find_elements(self.ndfl.sevenday_forecast_date)
            for date in dates:
                date_text = date.text
                if date_text not in days_weather_info:
                    weather_info_part = self.find_element(locator=(AppiumBy.XPATH, f'//*[@text="{date_text}"]/../..'))
                    if (self.is_element_exist(locator=self.ndfl.sevenday_forecast_psrText, driver=weather_info_part) and
                            self.is_element_exist(locator=self.ndfl.sevenday_forecast_weekday, driver=weather_info_part) and
                            self.is_element_exist(locator=self.ndfl.sevenday_forecast_temp, driver=weather_info_part) and
                            self.is_element_exist(locator=self.ndfl.sevenday_forecast_rh, driver=weather_info_part) and
                            self.is_element_exist(locator=self.ndfl.sevenday_forecast_detail, driver=weather_info_part) and
                            self.is_element_exist(locator=self.ndfl.sevenday_forecast_wind, driver=weather_info_part)
                    ):
                        psr_text = self.get_text(locator=self.ndfl.sevenday_forecast_psrText, driver=weather_info_part)
                        weekday = self.get_text(locator=self.ndfl.sevenday_forecast_weekday, driver=weather_info_part)
                        range_temp = self.get_text(locator=self.ndfl.sevenday_forecast_temp, driver=weather_info_part)
                        range_rh = self.get_text(locator=self.ndfl.sevenday_forecast_rh, driver=weather_info_part)
                        desc = self.get_text(locator=self.ndfl.sevenday_forecast_detail, driver=weather_info_part)
                        wind_info = self.get_text(locator=self.ndfl.sevenday_forecast_wind, driver=weather_info_part)
                        days_weather_info[date_text] = WeatherInfo(date_text, weekday, range_temp, range_rh, desc, wind_info, psr_text)
            self.driver.scroll(self.find_elements(self.ndfl.sevenday_forecast_temp)[-1],
                               self.find_elements(self.ndfl.sevenday_forecast_temp)[-2])
        return list(days_weather_info.values())
