from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        """
        根据特征找单个元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 返回元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def find_elements(self, feature, timeout=10, poll=1.0):
        """
                根据特征找多个符合条件的元素
                :param feature: 特征
                :param timeout: 超时时间
                :param poll: 频率
                :return: 返回多个元素
        """
        feature_by, feature_value = feature
        elements = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return elements

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()

    def is_toast_exist(self, message):
        message_xpath = "//*[contains(@text, '%s')]" % message
        """
        根据部分内容判断toast是否存在
        :param message:部分内容
        :return：是否存在
        """
        try:
            self.find_element(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据部分内容获取toast上的所有内容
        :param message: 部分内容
        :return: 所有内容
        """
        if self.is_toast_exist(message):
            message_xpath = "//*[contains(@text, '%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现或未捕获到")
