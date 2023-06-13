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
import screen_brightness_control as sbc
import random

from appium.webdriver.common import multi_action
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver import Remote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import IMG_PATH
from scripts.keys import KeyCode
from scripts.logger import logger


class BasePage:

    def __init__(self, driver: Remote):
        """
        初始化驱动
        :param driver:
        """
        self.driver = driver
        logger.info('开始初始化驱动driver......')
        self.driver.implicitly_wait(10)
        # logger.info(self.driver.get_settings())

    def get_system_bar(self):
        """
        状态栏
        :return:
        """
        self.driver.get_system_bars()

    def get_page_source(self):
        """
        获取页面所有元素
        :return:
        """
        return self.driver.page_source

    def element_is_exist(self, element):
        """
        判断元素是否存在页面中
        :return:
        """
        source = self.driver.page_source
        logger.info('page_source: {}'.format(source))
        if element in source:
            return True
        return False

    @staticmethod
    def generate_random(x=758, y=1473):
        """
        生成随机数
        :return:
        """
        return random.randint(x, y)

    @staticmethod
    def get_location(elem):
        """
        获取元素elem的x, y坐标轴位置信息
        :return:
        """
        x = elem.location.get('x')
        y = elem.location.get('y')
        return x, y

    # def find_elements(self, locator):
    #     """
    #     获取元素list
    #     :param locator:
    #     :return:
    #     """
    #     return self.driver.find_elements(*locator)

    @classmethod
    def get_window_brightness(cls, display=0):
        """
        获取当前屏幕亮度
        :return:
        """
        brightness = sbc.get_brightness(display=display)
        return brightness

    @staticmethod
    def get_elem_attribute(locator, text):
        """
        获取元素属性值
        :param locator:
        :param text:
        :return:
        """
        return locator.get_attribute(text)

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
            logger.info('wait_locator: {}'.format(locator))
            return wait.until(ec.element_to_be_clickable(locator))

        except (TimeoutException, NoSuchElementException) as e:
            # 加 logger
            logger.error('元素 {} 没有定位到: {}'.format(locator, e))
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
            logger.info('wait_locator: {}'.format(locator))
            return wait.until(ec.presence_of_element_located(locator))

        except (TimeoutException, NoSuchElementException) as e:
            # 加 logger
            logger.error('元素 {} 没有定位到: {}'.format(locator, e))
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
            logger.info('wait_locator: {}'.format(locator))
            return wait.until(ec.visibility_of_element_located(locator))

        except (TimeoutException, NoSuchElementException) as e:
            logger.error('元素 {} 没有定位到: {}'.format(locator, e))
            # 截图 screen_shot()
            self.screen_shot()

    def screen_shot(self) -> object:
        """
        截图，保存到指定的位置
        :return:
        """
        current_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        png_name = os.path.join(IMG_PATH, current_time_str + '.png')

        logger.info('错误截图为: {}'.format(png_name))
        return self.driver.save_screenshot(png_name)

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
        # 定位某个元素
        # TODO: try...except
        try:
            elem = self.driver.find_element(*locator)
            logging.info(elem)
            return elem

        except (NoSuchElementException, TimeoutException) as e:
            logger.error('元素 {} 没有定位到: {}'.format(locator, e))
            self.screen_shot()
            raise e

    def find_elements(self, locator) -> list:
        # 定位一组元素 list
        try:
            elems = self.driver.find_elements(*locator)
            logging.info(elems)
            return elems
        except (NoSuchElementException, TimeoutException) as e:
            logger.error('元素 {} 没有定位到: {}'.format(locator, e))
            self.screen_shot()
            raise e

    @property
    def size(self) -> dict:
        return self.driver.get_window_size()

    @property
    def width(self) -> (int, float):
        return self.size['width']

    @property
    def height(self) -> (int, float):
        return self.size['height']

    def scroll_view(self, locator):
        """
        滑动到指定元素
        :return:
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

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

    def swipe_up_and_down(self, x1, y1, x2, y2, duration=200):
        """
        滑动屏幕操作
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param duration:
        :return:
        """
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y2, duration=duration)

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

    def hide_keyboard(self):
        """
        收起键盘
        :return:
        """
        self.driver.hide_keyboard()

    def send_keycode(self, key):
        """
        发送物理按键
        :param key:
        :return:
        """
        return self.driver.press_keycode(key)

    def back(self):
        return self.send_keycode(KeyCode.KEYCODE_BACK)

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
        try:
            toast = self.wait_presence_element((
                MobileBy.XPATH, f'//*[contains(@text, "{toast_text}")]'), timeout=30, poll=0.1).text
            logger.info('获取toast成功: {}'.format(toast))
            return toast

        except (TimeoutException, NoSuchElementException) as e:
            logger.error('获取toast失败: {}'.format(e))
            self.screen_shot()
            raise e

    def double_click(self, element):
        """
        双击某个元素
        :param element:
        :return:
        """
        action = ActionChains(self.driver).move_to_element(element).double_click()
        return action

    def press(self, x, y, wait_time=6000, el=None):
        """
        按压, Element
        :param wait_time:
        :param x:
        :param y:
        :param el:
        :return:
        """
        action = TouchAction(self.driver)

        logger.info('action: {}'.format(action))
        return action.press(el=el, x=x, y=y).wait(wait_time).perform()

    def move_to(self, x, y):
        """
        移动手势
        :param x:
        :param y:
        :return:
        """
        action = TouchAction(self.driver).move_to(x, y).perform()
        logger.info('action: {}'.format(action))
        return action

    def press_and_move_to(self, x1, y1, x2, y2):
        """
        坐标滑动屏幕
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """
        action = TouchAction(self.driver)

        logger.info('action: {}'.format(action))
        return action.press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()

    def long_press(self, x, y, wait=8000, el=None):
        """
        长按某个元素
        :param x:
        :param y:
        :param wait:
        :param el:
        :return:
        """
        action = TouchAction(self.driver)

        logger.info('action: {}'.format(action))
        return action.long_press(el=el, x=x, y=y).wait(wait).release().perform()

    def execute_js(self, script=True):
        # 滑动到顶部
        if not script:
            script = "var q=document.documentElement.scrollTop=0"
        # 滑动到底部
        else:
            script = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(script)


class Element:
    """
    描述符
    """
    Locate_Method = {'click': ec.element_to_be_clickable, 'presence': ec.presence_of_element_located,
                     'visibility': ec.visibility_of_element_located}

    def __init__(self, locator,
                 method='click',
                 desc='元素',
                 value=None,
                 is_elems=False,
                 one_elem=True,
                 index=None,
                 one_from_elems=False
                 ):
        """
        元素定位
        :param locator: 元素定位表达式
        :param method: 显示等待方法
        :param desc: 元素描述
        :param value: xxx
        :param is_elems: 定位的元素是否是列表
        :param one_elem: 是否返回单个element对象
        :param index: 返回多个element指定index索引对象
        :param one_from_elems: 从多个elements返回某个指定的element
        """
        self.locator = locator
        self.method = method
        self.desc = desc
        self.value = value
        self.is_elems = is_elems
        self.one_elem = one_elem
        self.index = index
        self.one_from_elems = one_from_elems

    def __get__(self, instance, owner):
        """
        定位元素
        :param instance:
        :param owner:
        :return:
        """
        logger.info('元素描述为: {}'.format(self.desc))
        web_elem = None
        try:
            if self.Locate_Method[self.method]:
                wait = WebDriverWait(instance.driver, timeout=10, poll_frequency=0.2)

                if not self.is_elems:
                    web_elem = wait.until(self.Locate_Method[self.method](self.locator))
                    logger.info('web_elem: {}'.format(web_elem))
                else:
                    if self.one_elem:
                        if self.one_from_elems:
                            web_elem = instance.driver.find_elements(*self.locator)[self.index]
                        else:
                            web_elem = instance.driver.find_element(*self.locator)

                        # logger.info('elem: {}'.format(web_elem))
                        # web_elem = wait.until(self.Locate_Method[self.method](elem))
                        logger.info('web_elem: {}'.format(web_elem))

                logger.info('{} locator: {}'.format(self.desc, self.locator))
                self.web_elem = web_elem
                return self

            logger.error('元素等待方式 {} 不存在，请重新再检查'.format(self.method))
            return

        except (NoSuchElementException, TimeoutException) as e:
            logger.error('元素 {} 的表达式 {} 未定位到: {}'.format(self.desc, self.locator, e))
            current_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
            png_name = os.path.join(IMG_PATH, current_time_str + '.png')
            logger.info('错误截图为: {}'.format(png_name))
            return instance.driver.save_screenshot(png_name)

        # login_page.driver.find_element(*self.locator)
        # web_elem = instance.driver.find_element(*self.locator)
        # self.web_elem = web_elem

        # app不生效颜色，web可以使用
        # 找到的元素标成红色 # js
        # js_code = 'arguments[0].style.border = "1px solid red"'
        # instance.driver.execute_script(js_code, web_elem)

        # return self

    def get_attribute(self, text):
        """
        获取元素属性
        :param text:
        :return:
        """
        return self.web_elem.get_attribute(text)

    @property
    def text(self):
        """
        获取属性text
        :return:
        """
        return self.web_elem.text

    def double_click(self, element):
        """
        双击某个元素
        :param element:
        :return:
        """
        action = ActionChains(self.web_elem).move_to_element(element).double_click()
        return action

    def click(self):
        self.web_elem.click()

    def send_keys(self, data):
        self.web_elem.send_keys(data)


if __name__ == '__main__':
    def generate_random():
        """
        生成随机数
        :return:
        """
        return random.randint(758, 1473)


    print(generate_random())
