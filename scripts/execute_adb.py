# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：execute_adb.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/31
# 当前系统时间：18:23
# 用于创建文件的IDE的名称: PyCharm


import subprocess

from scripts.device_driver import caps
from scripts.logger import logger


DEVICE_NAME = caps['deviceName']


class ADB:
    """
    Python执行adb相关方法
    """

    def __init__(self):
        self.device_name = DEVICE_NAME

    @classmethod
    def run(cls, cmd):
        """
        运行adb命令
        :param cmd:
        :return:
        """
        return subprocess.run(cmd, capture_output=True, text=True, shell=True)

    def device_exit(self):
        """
        判断设备是否链接
        :return:
        """
        device_info = ADB.run('adb devices')

        result = device_info.stdout
        if self.device_name in result:
            logger.info(result)
            return True

        logger.error('{} 设备未连接'.format(self.device_name))
        return False

    def get_adb_result(self, cmd):
        """
        运行adb相关命令并返回预期结果
        :param cmd:
        :return:
        """
        if self.device_exit():
            try:
                expect = ADB.run(cmd)
                logger.info(expect)
                return int(expect.stdout)
            except Exception as e:
                logger.error(e)
                raise e

    @property
    def get_device_bright(self):
        """
        获取当前屏幕亮度
        :return:
        """
        bright = self.get_adb_result('adb shell "settings get system screen_brightness"')
        return bright


adb = ADB()


if __name__ == '__main__':
    adb = ADB()
    res = adb.device_exit()
    print(res)
    print(adb.get_device_bright)
