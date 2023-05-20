# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：base_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/4/26
# 当前系统时间：14:35
# 用于创建文件的IDE的名称: PyCharm

import os
import time
from datetime import datetime
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import IMG_PATH

from scripts.keys import KeyCode


class BasePage:

    def __init__(self, driver: Remote):
        """
        初始化驱动
        :param driver:
        """
        self.driver = driver

    def wait_click_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        """
        等待元素可点击
        :param locator:
        :param timeout:
        :param poll:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll)
            return wait.until(ec.element_to_be_clickable(locator))

        except (TimeoutException, NoSuchElementException):
            # 加 logger
            logging.error('元素没有定位到')
            # 截图 screen_shot()
            self.screen_shot()

    def wait_presence_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        """
        等待元素出现
        :param locator:
        :param timeout:
        :param poll:
        :return:
        """

        try:
            wait = WebDriverWait(self.driver, timeout, poll)
            return wait.until(ec.presence_of_element_located(locator))

        except (TimeoutException, NoSuchElementException):
            # 加 logger
            logging.error('元素没有定位到')
            # 截图 screen_shot()
            self.screen_shot()

    def wait_visibility_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        """
        等待元素可见
        :param locator:
        :param timeout:
        :param poll:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll)
            return wait.until(ec.visibility_of_element_located(locator))

        except (TimeoutException, NoSuchElementException):
            logging.error('元素没有被定位到')
            self.screen_shot()

    def screen_shot(self) -> object:
        """
        截图，保存到指定的位置
        :return:
        """
        current_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        return self.driver.save_screenshot(os.path.join(IMG_PATH, current_time_str + '.png'))

    def click(self, locator):
        """
        点击元素
        :param locator:
        :return:
        """
        return self.wait_click_element(locator).click()

    def switch_frame(self, locator=None, timeout=10, fqc=20):
        """
        切换iframe
        :param locator:
        :param timeout:
        :param fqc:
        :return:
        """
        if not locator:
            return self.driver.switch_to.default_content()
        return WebDriverWait(self.driver, timeout, poll_frequency=fqc).until(
            ec.frame_to_be_available_and_switch_to_it(locator))

    def switch_context(self, context_name=None):
        """
        上下文切换
        :param context_name:
        :return:
        """
        # 在只有两个上下文的情况。
        # 'NAVTIVE, WEB_VIEW
        if not context_name:
            return self.driver.switch_to.context("NATIVE_APP")
        current_contexts = self.driver.contexts
        for ctx in current_contexts:
            if ctx == context_name:
                self.driver.switch_to.context(context_name)

    def find_element(self, locator) -> WebElement:
        # TODO: try...except
        return self.driver.find_element(*locator)

    @property
    def size(self) -> dict:
        return self.driver.get_window_size()

    @property
    def width(self) -> (int, float):
        return self.size['width']

    @property
    def height(self) -> (int, float):
        return self.size['height']

    def swipe_left(self, duration=200):
        """
        向左划
        :param duration:
        :return:
        """
        # size = self.driver.get_window_size()
        # width = size['width']
        # height = size['height']
        self.driver.swipe(self.width * 0.9, self.height * 0.5, self.width * 0.1, self.height * 0.5, duration)

    def swipe_right(self, duration=200):
        """
        向右划
        :param duration:
        :return:
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width * 0.1, height * 0.5, width * 0.9, height * 0.5, duration)

    def swipe_down(self, duration=200):
        """
        向下划
        :param duration:
        :return:
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width * 0.5, height * 0.1, width * 0.5, height * 0.9, duration)

    def swipe(self, direction):
        """
        选择滑动方向
        :param direction:
        :return:
        """
        if direction == 'left':
            return self.swipe_left()
        elif direction == 'right':
            return self.swipe_right()

    def jiugongge(self, e, points):
        """
        九宫格绘制 [5,7,3,6,9].
        :param e:
        :param points:
        :return:
        """
        action = TouchAction(self.driver)

        start_x = e.rect["x"]
        start_y = e.rect["y"]
        width = e.rect["width"]
        height = e.rect["height"]

        # 1,2,3,6,9
        static_point = [
            {"x": start_x + width * 1 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 1 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 1 / 6, "y": start_y + height * 5 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 5 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 5 / 6},
        ]
        action.press(**static_point[points[0] - 1]).wait(200)
        for p in points[1:]:
            action.move_to(**static_point[p - 1]).wait()
        action.release().perform()

    def send_keycode(self, key):
        """
        发送物理按键
        :param key:
        :return:
        """
        return self.driver.press_keycode(key)

    def volume_up(self):
        return self.send_keycode(KeyCode.VOLUME_UP)

    def confirm(self):
        """
        回车
        :return:
        """
        return self.send_keycode(KeyCode.ENTER)

    def volume_down(self):
        """
        音量减
        :return:
        """
        return self.send_keycode(KeyCode.VOLUME_DOWN)

    def change_context_(self, ctx_name=None):
        """
        上下文切换, WEBVIEW_.... NATIVE_APP, 混合应用，h5
        :param ctx_name:
        :return:
        """
        if ctx_name is None:
            return self.driver.switch_to.context("NATIVE_APP")
        self.driver.switch_to.context(ctx_name)

    def show_toast(self, toast_text):
        """
        获取 toast
        :param toast_text:
        :return:
        """
        # TODO: 要用 presence_locatored, visiblity
        self.wait_presence_element((
            MobileBy.XPATH, f"//*[contains(@text, {toast_text})]"), timeout=20, poll=0.2)

    def double_click(self):
        pass

    def press(self, x, y):
        """
        按压, Element
        :param x:
        :param y:
        :return:
        """
        action = TouchAction(self.driver)
        return action.press(x, y).perform()

    def move_to(self, x, y):
        """
        移动手势
        :param x:
        :param y:
        :return:
        """
        action = TouchAction(self.driver)
        return action.move_to(x, y).perform()

    def long_press(self, elem, wait=6000):
        """
        长按某个元素
        :param elem:
        :param wait:
        :return:
        """
        action = TouchAction(self.driver)
        return action.long_press(elem).wait(wait).release().perform()

    def execute_js(self, js=True):
        # 喜欢ii选哪个javascript
        # 滑动到顶部
        if not js:
            js = "var q=document.documentElement.scrollTop=0"
        # 滑动到底部
        else:
            js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

    def get_elem_property(self) -> str:
        """
        获取元素的属性值
        :return:
        """
        pass


class Element(object):
    def __init__(self, locator, desc='元素'):
        self.locator = locator
        self.desc = desc

    def __get__(self, instance, owner):
        """
        定位元素
        :param instance:
        :param owner:
        :return:
        """
        # login_page.driver.find_element(*self.locator)
        web_elem = instance.driver.find_element(*self.locator)
        self.web_elem = web_elem

        # app不生效颜色，web可以使用
        # 找到的元素标成红色 # js
        # js_code = 'arguments[0].style.border = "1px solid red"'
        # instance.driver.execute_script(js_code, web_elem)

        return self

    def click(self):
        self.web_elem.click()

    def send_keys(self, data):
        self.web_elem.send_keys(data)


if __name__ == '__main__':
    pass
