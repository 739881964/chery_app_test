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
from pages.car_settings_page import CarSettingPage
from pages.menu_light_page import MenuLightPage
from config import DEVICE_INFO
from pages.btphone_page import BTPhonePage
from pages.connect_page import ConnectPage

# 获取设备cap信息
with open(DEVICE_INFO, 'r', encoding='utf8') as f:
    caps = yaml.load(f, Loader=yaml.FullLoader)
    print(caps)


def base_driver(url='http://127.0.0.1:4723/wd/hub', **kwargs):
    for k, v in kwargs.items():
        caps[k] = v
    driver = Remote(desired_capabilities=caps, command_executor=url)

    return driver


@pytest.fixture()
def init_app():
    driver = base_driver()
    yield driver
    driver.quit()


@pytest.fixture()
def init_setting():
    driver = base_driver()
    page = CarSettingPage(driver)
    yield page
    driver.quit()


@pytest.fixture()
def init_menu_light():
    driver = base_driver()
    page = MenuLightPage(driver)
    yield page
    driver.quit()


@pytest.fixture()
def init_btphone():
    driver = base_driver()
    btphone_page, connect_page = BTPhonePage(driver), ConnectPage(driver)
    yield btphone_page, connect_page
    driver.quit()


if __name__ == '__main__':
    base_driver()
