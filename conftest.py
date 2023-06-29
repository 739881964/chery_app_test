# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：conftest.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/4/26
# 当前系统时间：00:54
# 用于创建文件的IDE的名称: PyCharm

import os
import time
import pytest
import yaml
import subprocess

from appium.webdriver import Remote
from scripts.logger import logger
from config import DEVICE_INFO
from time import sleep

from scripts.logger import logger

import pages.car_settings.sound_page
from pages.car_settings.car_settings_page import CarSettingPage
from pages.car_settings.menu_light_page import MenuLightPage
from pages.btphone_page import BTPhonePage
from pages.car_settings.connect_page import ConnectPage
from pages.gallery.local_page import LocalPage
from pages.gallery.usb_page import UsbPage
from pages.car_settings.sound_page import SoundPage
from pages.car_settings.show_page import ShowPage
from pages.car_settings.drive_page import DrivePage
from pages.calendar_page import CalendarPage
from pages.launcher_page import LauncherPage
from pages.media_page import MediaPage
from pages.wifi_page import WiFiPage
from pages.weather_page import WeatherPage

from scripts.appium_server import AppiumServer

URL = 'http://127.0.0.1:4723/wd/hub'


# @pytest.fixture(scope='session', autouse=True)
def start_appium_server():
    """
    启动appium服务，用例执行结束后关闭服务
    :return:
    """
    app_server = AppiumServer()
    app_server.start_appium()
    yield
    app_server.kill_appium_server()


# 获取设备信息cap
def get_device_caps(cap: str) -> dict:
    """
    获取不同app对应的caps配置信息
    :param cap:
    :return: info
    """
    with open(DEVICE_INFO, 'r', encoding='utf8') as f:
        info = yaml.load(f, Loader=yaml.FullLoader)
        # print(caps)

    try:
        app_activity = info['appActivity']
        app_package = info['appPackage']

        info['appActivity'] = app_activity[cap]
        info['appPackage'] = app_package[cap]
    except Exception as e:
        logger.error(e)
        raise e

    logger.info('cap info: {}'.format(info))
    return info


def base_driver(app_name='car_settings', url=URL, **kwargs):
    """
    启动app driver
    :param app_name:
    :param url:
    :param kwargs:
    :return:  driver
    """
    caps = get_device_caps(app_name)
    for k, v in kwargs.items():
        caps[k] = v

    logger.info('启动app参数为: {}'.format(caps))
    driver = Remote(command_executor=url, desired_capabilities=caps)

    return driver


@pytest.fixture()
def init_weather():
    """
    初始化天气app
    :return:
    """
    driver = base_driver('weather')
    logger.info('{} 成功'.format(init_weather.__doc__))
    weather_page = WeatherPage(driver)
    sleep(10)
    # 若有预警弹出框，先关闭
    try:
        if weather_page.gain_warning_attribute:
            weather_page.alert_close_elem.click()
    except Exception as e:
        logger.warning(e)
    yield weather_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_wifi():
    """
    初始化wifi驱动
    """
    driver = base_driver('car_settings')
    logger.info('{} 成功'.format(init_wifi.__doc__))
    wifi_page = WiFiPage(driver)
    ConnectPage(driver).swipe_to_connect()
    yield wifi_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_media():
    """
    初始化本地畅想音乐
    """
    driver = base_driver('media')
    logger.info('{} 成功'.format(init_media.__doc__))
    drive_page = MediaPage(driver)
    yield drive_page
    logger.info('正在关闭驱动')
    driver.stop_client()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_launcher():
    """
    初始化launcher驱动
    """
    driver = base_driver('launcher')
    logger.info('{} 成功'.format(init_launcher.__doc__))
    drive_page = LauncherPage(driver)
    yield drive_page
    logger.info('正在关闭驱动')
    # driver.quit()
    driver.stop_client()
    logger.info('关闭驱动成功！')


@pytest.fixture(scope='class')
def init_calendar():
    """
    初始化日历驱动driver
    """
    driver = base_driver('calendar')
    logger.info('{} 成功'.format(init_calendar.__doc__))
    drive_page = CalendarPage(driver)
    yield drive_page
    logger.info('正在关闭驱动')
    # driver.quit()
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture(scope='class')
def init_drive():
    """
    初始化驾驶驱动
    :return:
    """
    driver = base_driver()
    logger.info('{} 成功'.format(init_sound.__doc__))
    drive_page = DrivePage(driver)
    yield drive_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_sound():
    """
    初始化声音驱动
    """
    driver = base_driver('car_settings')
    logger.info('{} 成功'.format(init_sound.__doc__))
    sound_page = SoundPage(driver)
    yield sound_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_show():
    """
    初始化车辆设置-显示驱动
    """
    driver = base_driver('car_settings')
    logger.info('{} 成功'.format(init_show.__doc__))
    # logger.info('初始化车辆设置-显示驱动driver成功')
    show_page = ShowPage(driver)
    logger.info(show_page)
    yield show_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_gallery():
    """
    初始化图库驱动
    """
    driver = base_driver('gallery')
    logger.info('{} 成功'.format(init_gallery.__doc__))
    local_page, usb_page = LocalPage(driver), UsbPage(driver)
    yield local_page, usb_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_app():
    """
    初始化app驱动
    """
    driver = base_driver('car_settings')
    logger.info('{} 成功'.format(init_app.__doc__))
    yield driver
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_setting():
    """
    初始化车辆设置驱动
    """
    driver = base_driver('car_settings')
    logger.info('{} 成功'.format(init_setting.__doc__))
    page = CarSettingPage(driver)
    print(driver.contexts)
    yield page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture(scope='class')
def init_menu_light():
    """
    初始化灯光驱动
    """
    driver = base_driver('car_settings')
    logger.info('{} 成功'.format(init_menu_light.__doc__))
    page = MenuLightPage(driver)
    yield page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


@pytest.fixture()
def init_btphone():
    """
    初始化蓝牙电话驱动
    """
    driver = base_driver('bt_phone')
    logger.info('{} 成功'.format(init_btphone.__doc__))
    btphone_page, connect_page = BTPhonePage(driver), ConnectPage(driver)
    yield btphone_page, connect_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')


if __name__ == '__main__':
    print(get_device_caps('bt_phone'))
