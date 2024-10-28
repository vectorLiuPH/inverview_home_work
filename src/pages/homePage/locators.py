from appium.webdriver.common.appiumby import AppiumBy


class HomePageLocators:


    navigator = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="hko.MyObservatory_v1_0:id/toolbar"]/android.widget.ImageButton')
    forecast_warning_services_drop_down = (
    AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout')
    background_image = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/backgroundImage')

    right_top_options=(AppiumBy.XPATH,'//androidx.appcompat.widget.LinearLayoutCompat/android.widget.ImageView')
    switch_language_button=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("hko.MyObservatory_v1_0:id/title").textContains("Language")')
    english_language_option=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("English")')
