from appium.webdriver.common.appiumby import AppiumBy


class NineDayForecastLocators:
    nine_day_forecast_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("hko.MyObservatory_v1_0:id/title").textMatches("9-Day Forecast|九天預報|九天预报")')
    general_situation = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit')
    each_day_weather_parts = (AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout')
    sevenday_forecast_date = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_date')
    sevenday_forecast_weekday = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week')
    sevenday_forecast_icon = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_Icon')
    sevenday_forecast_temp = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_temp')
    sevenday_forecast_rh = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_rh')
    sevenday_forecast_psrIcon = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/psrIcon')
    sevenday_forecast_psrText = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/psrText')
    sevenday_forecast_wind = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_wind')
    sevenday_forecast_detail = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/sevenday_forecast_details')
