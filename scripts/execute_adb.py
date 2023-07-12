# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：execute_adb.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/31
# 当前系统时间：18:23
# 用于创建文件的IDE的名称: PyCharm

# import torch
# import tensorflow as tf
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

        logger.error('{} 设备未连接'.format(self.device_name))

    @property
    def get_device_bright(self):
        """
        获取当前屏幕亮度
        :return:
        """
        bright = self.get_adb_result('adb shell "settings get system screen_brightness"')
        return bright

    def run_monkey_enter(self,
                         seed: '随机种子数: int' = 1000,
                         log_level: '日志级别: str' = '-v -v -v',
                         throttle: '事件结束间隔时间: int' = 100,
                         touch: '触摸事件: int' = 30,
                         motion: '滑动事件: int' = 30,
                         times: '执行多少次: int' = 10000,
                         white_file=False,
                         black_file=False,
                         appoint_package=None,
                         log_path='/Users/yuxiang/PycharmProjects/chery_app_test/monkey_log.txt',
                         ):
        """
        monkey 稳定性测试
        :param seed:
        :param log_level:
        :param throttle:
        :param touch:
        :param motion:
        :param times:
        :param white_file:
        :param black_file:
        :param appoint_package:
        :param log_path:
        :return:
        """
        if white_file:
            monkey_cmd = f'adb shell monkey --pkg-whitelist-file /data/whitelist.txt --pct-touch {touch} ' \
                         f'--pct-motion {motion} --ignore-crashes --ignore-timeouts --throttle {throttle}' \
                         f' -s {seed} {log_level} {times} > {log_path}'
        elif black_file:
            monkey_cmd = f'adb shell monkey --pkg-blacklist-file /data/blacklist.txt --pct-touch {touch} ' \
                         f'--pct-motion {motion} --ignore-crashes --ignore-timeouts --throttle {throttle} ' \
                         f'-s {seed} {log_level} {times} > {log_path}'
        elif appoint_package:
            monkey_cmd = f'adb shell monkey -p {appoint_package} --pct-touch {touch}  --pct-motion {motion} ' \
                         f'--ignore-crashes --ignore-timeouts --throttle {throttle} -s {seed} {log_level} {times} ' \
                         f'> {log_path}'
        else:
            monkey_cmd = f'adb shell monkey --pct-touch {touch} --pct-motion {motion} --ignore-crashes ' \
                         f'--ignore-timeouts --throttle {throttle} -s {seed} {log_level} {times} > {log_path}'

        logger.info(monkey_cmd)
        self.run(monkey_cmd)


adb = ADB()

if __name__ == '__main__':
    ADB().run_monkey_enter(seed=200,
                           log_level='-v -v -v',
                           touch=30,
                           motion=30,
                           throttle=300,
                           times=100,
                           black_file=True,
                           )
