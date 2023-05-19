# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：config.py
# 当前用户的登录名：yuxiang
# 当前编辑文件名：config
# 当前系统日期：2023/4/26
# 当前系统时间：01:02
# 用于创建文件的IDE的名称: PyCharm


import os

# 项目的路径
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# 设备信息路径
DEVICE_INFO = os.path.join(ROOT_PATH, 'cap.yaml')
# print(DEVICE_INFO)

# log 的路径
LOG_PATH = os.path.join(ROOT_PATH, 'logs')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
    # os.makedirs()

# 截图位置
IMG_PATH = os.path.join(LOG_PATH, 'imgs')
if not os.path.exists(LOG_PATH):
    os.mkdir(IMG_PATH)
