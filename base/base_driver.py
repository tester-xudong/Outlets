from appium import webdriver


def init_driver():
    # 设备信息
    desired_caps = dict()
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '20693c64'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True

    # app信息
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = '.activity.MainActivity'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
