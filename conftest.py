# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：conftest.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/4/26
# 当前系统时间：00:54
# 用于创建文件的IDE的名称: PyCharm


import pytest
import yaml

from appium.webdriver import Remote

import pages.car_settings.sound_page
from pages.car_settings.car_settings_page import CarSettingPage
from pages.car_settings.menu_light_page import MenuLightPage
from config import DEVICE_INFO
from pages.btphone_page import BTPhonePage
from pages.car_settings.connect_page import ConnectPage
from pages.gallery.local_page import LocalPage
from pages.gallery.usb_page import UsbPage
from pages.car_settings.sound_page import SoundPage
from pages.car_settings.show_page import ShowPage

URL = 'http://127.0.0.1:4723/wd/hub'

# 获取设备cap信息
with open(DEVICE_INFO, 'r', encoding='utf8') as f:
    caps = yaml.load(f, Loader=yaml.FullLoader)
    print(caps)


def base_driver(url=URL, **kwargs):
    for k, v in kwargs.items():
        caps[k] = v
    driver = Remote(desired_capabilities=caps, command_executor=url)

    return driver


@pytest.fixture()
def init_sound():
    """
    初始化声音驱动
    :return:
    """
    driver = base_driver()
    sound_page = SoundPage(driver)
    yield sound_page
    driver.quit()


@pytest.fixture()
def init_show():
    """
    初始化车辆设置-显示驱动
    :return:
    """
    driver = base_driver()
    show_page = ShowPage(driver)
    yield show_page
    driver.quit()


@pytest.fixture()
def init_gallery():
    """
    初始化图库驱动
    :return:
    """
    driver = base_driver()
    local_page, usb_page = LocalPage(driver), UsbPage(driver)
    yield local_page, usb_page
    driver.quit()


@pytest.fixture()
def init_app():
    """
    初始化app驱动
    :return:
    """
    driver = base_driver()
    yield driver
    driver.quit()


@pytest.fixture()
def init_setting():
    """
    初始化车辆设置驱动
    :return:
    """
    driver = base_driver()
    page = CarSettingPage(driver)
    print(driver.contexts)
    yield page
    driver.quit()


@pytest.fixture()
def init_menu_light():
    """
    初始化灯光驱动
    :return:
    """
    driver = base_driver()
    page = MenuLightPage(driver)
    yield page
    driver.quit()


@pytest.fixture()
def init_btphone():
    """
    初始化蓝牙电话驱动
    :return:
    """
    driver = base_driver()
    btphone_page, connect_page = BTPhonePage(driver), ConnectPage(driver)
    yield btphone_page, connect_page
    driver.quit()


if __name__ == '__main__':
    base_driver()
