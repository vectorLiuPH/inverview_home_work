import pytest

from src.pages.homePage.actions import HomePageActions
from src.pages.navigator.forecastWarningServices.nineDayForecast.actions import NineDayForecastActions


@pytest.fixture(scope="function")
def open_9_day_forecast(init_with_dealing_dialog):
    home_page_actions = HomePageActions(init_with_dealing_dialog)
    home_page_actions.open_navigator()
    home_page_actions.open_forecast_warning_services()
    nine_day_forecast_actions = NineDayForecastActions(init_with_dealing_dialog)
    nine_day_forecast_actions.open_nine_days_forecast()
    yield init_with_dealing_dialog, nine_day_forecast_actions


def test_check_general_situation(open_9_day_forecast):
    nine_day_forecast_actions = open_9_day_forecast[1]
    brief_text_from_api = nine_day_forecast_actions.get_general_situation_from_api()
    brief_text_display = nine_day_forecast_actions.get_general_situation_text()
    assert brief_text_display in brief_text_from_api


def test_check_each_day_weather(open_9_day_forecast):
    nine_day_forecast_actions = open_9_day_forecast[1]
    days_weather_info_from_api = nine_day_forecast_actions.get_days_weather_info_from_api()
    days_weather_info_from_display = nine_day_forecast_actions.get_days_weather_info()
    for _ in zip(days_weather_info_from_api,days_weather_info_from_display):
        from_api=_[0]
        from_display=_[1]
        assert from_display.date in from_api.date
        assert from_display.weekday in from_api.weekday
        assert from_display.desc == from_api.desc
        assert from_display.psr_text == from_api.psr_text
        assert from_display.wind_info == from_api.wind_info
        assert from_display.range_rh == from_api.range_rh
        assert from_display.range_temp == from_api.range_temp
