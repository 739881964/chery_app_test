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
from scripts.logger import logger

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
from pages.car_settings.drive_page import DrivePage

URL = 'http://127.0.0.1:4723/wd/hub'


# 获取设备信息cap
def get_device_caps(cap: str):
    """
    获取不同app对应的caps配置信息
    :param cap:
    :return:
    """
    with open(DEVICE_INFO, 'r', encoding='utf8') as f:
        info = yaml.load(f, Loader=yaml.FullLoader)
        # print(caps)

    app_activity = info['appActivity']
    app_package = info['appPackage']

    info['appActivity'] = app_activity[cap]
    info['appPackage'] = app_package[cap]

    return info


def base_driver(app_name='car_settings', url=URL, **kwargs):
    caps = get_device_caps(app_name)
    for k, v in kwargs.items():
        caps[k] = v

    logger.info('启动app参数为: {}'.format(caps))
    driver = Remote(command_executor=url, desired_capabilities=caps)

    return driver


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


@pytest.fixture()
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
