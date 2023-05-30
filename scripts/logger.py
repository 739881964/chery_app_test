# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：logger.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/26
# 当前系统时间：10:13
# 用于创建文件的IDE的名称: PyCharm

import logging
from scripts.get_configs import config
from config import LOGS_FILE_PATH


class Logger(object):

    def __init__(self):
        self.log = logging.getLogger(config.get_value('log', 'loger_name'))  # 日志解释器对象
        self.log.setLevel(config.get_value('log', 'loger_level'))  # 日志解释器日志等级

        # 日志输出方式
        console_log = logging.StreamHandler()  # 控制台输出
        file_log = logging.FileHandler(LOGS_FILE_PATH, encoding='utf-8')  # 文件输出

        # 日志输出格式
        simple_log = logging.Formatter(config.get_value('log', 'more'))
        more_log = logging.Formatter(config.get_value('log', 'more'))

        console_log.setFormatter(more_log)
        file_log.setFormatter(more_log)

        # 输出等级
        console_log.setLevel(config.get_value('log', 'console_level'))
        file_log.setLevel(config.get_value('log', 'file_level'))

        self.log.addHandler(console_log)
        self.log.addHandler(file_log)

    def get_log(self):
        return self.log


logger = Logger().get_log()
