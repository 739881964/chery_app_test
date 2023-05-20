# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：device_driver.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/4/26
# 当前系统时间：00:37
# 用于创建文件的IDE的名称: PyCharm


import pytest
import yaml
from appium.webdriver import Remote

from config import DEVICE_INFO


# 获取设备cap信息
with open(DEVICE_INFO, 'r', encoding='utf8') as f:
    caps = yaml.load(f, Loader=yaml.FullLoader)
    print(caps)


def base_driver(url='http://127.0.0.1:4723/wd/hub', **kwargs):
    for k, v in kwargs.items():
        caps[k] = v
    driver = Remote(desired_capabilities=caps, command_executor=url)

    return driver


if __name__ == '__main__':
    base_driver()
