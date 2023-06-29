# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：appium_server.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/29
# 当前系统时间：13:11
# 用于创建文件的IDE的名称: PyCharm


import subprocess
import time
import os

from time import sleep
from scripts.logger import logger
from config import Appium_Log


class AppiumServer:
    """
    运行脚本前，启动appium服务，结束后，关闭appium服务
    """

    def __init__(self, port=4723):
        self.port = port

    @staticmethod
    def send_cmd(cmd, encoding='utf-8'):
        """
        cmd发送命令
        :param cmd:命令
        :param encoding: 编码方式，默认utf-8,出现乱码用gbk
        :return:
        """
        res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, encoding=encoding)
        com = res.communicate()
        value = com[0]
        res.terminate()
        return value

    def start_appium(self):
        bp = int(self.port) + 1
        self.kill_appium_server(self.port)
        # self.kill_appium_server(port=bp)
        # appium_log = os.path.join(DirPath.Logs, 'Appium_' + name + '.log')
        # 后台执行
        cmd = "appium -p " + str(self.port) + " -g " + Appium_Log + " -a 127.0.0.1"
        # cmd = "appium -p " + str(self.port) + " -bp " + str(
        #     bp) + " -g " + Appium_Log + " --session-override -a 127.0.0.1 --command-timeout 300"
        logger.info(cmd)
        self.send_cmd(cmd)
        time.sleep(3)

    def kill_appium_server(self, port=4723):
        try:
            # 查找对应端口的pid
            cmd_find = 'lsof -i tcp:%s' % port
            text = self.send_cmd(cmd_find, encoding="gbk")
            if text != '':
                res = text.split("\n")
                for i in res:
                    if "LISTEN" in i:
                        pid = i.split()[1]
                        # 执行被占用端口的pid
                        cmd = 'kill -9 %s' % pid
                        self.send_cmd(cmd, encoding="gbk")
                        logger.info("port %s appium server close" % str(self.port))
                        # logger.info(res)
                        # logger.debug(str(res).strip())
                        # if ("成功" in res) or ("SUCCESS".lower() in res.lower()):
                        #     logger.debug("port %s appium server close" % str(self.port))
            else:
                return
        except Exception as e:
            logger.error(e)
            return


if __name__ == '__main__':
    appium_server = AppiumServer()
    appium_server.start_appium()
    # appium_server.kill_appium_server()
