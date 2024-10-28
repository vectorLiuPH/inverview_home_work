from appium.webdriver.common.appiumby import AppiumBy


class PreActionsLocators:
    disclaimer = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Disclaimer|免责申明|免責聲明")')
    disclaimer_agree_button = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/btn_agree')

    PPS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Privacy Policy Statements|隐私政策声明|私隱政策聲明")')
    PPS_agree_button = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/btn_agree')

    send_notifications_dialog = (
    AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Allow MyObservatory to send notifications?|是否允许“我的天文台”发送通知|是否允許“我的天文臺”發送通知")')
    allow_all_the_time_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Allow all the time|始终允许|始終允許")')

    access_location_dialog = (
    AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Background Access to Location Information|背景存取位置咨询|背景存取位置資訊")')
    access_location_dialog_ok_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("OK|确定|確定")')

    access_location_info = (
    AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Allow MyObservatory to access location info?|是否允许“我的天文台”获取位置信息|是否允許“我的天文臺”獲取位置信息")')
    allow_while_using_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("Allow only while using the app|仅在使用中允许|僅在使用中允許")')

    allow_access_location_info = (AppiumBy.ANDROID_UIAUTOMATOR,
                                  'new UiSelector().textMatches("Allow MyObservatory to access location info in the background?|是否允许“我的天文台”在后台对设备进行定位|是否允許“我的天文臺”在後臺對設備進行定位")')
