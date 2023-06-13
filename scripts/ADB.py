# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：ADB.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/2
# 当前系统时间：14:54
# 用于创建文件的IDE的名称: PyCharm


import subprocess
import re

DEVICE_NAME = 'IBBA7DJVWOD67LZ9'  # caps['deviceName']


class ADB:

    def __init__(self):
        pass

    def adb(self, command) -> list:
        """
        执行adb返回结果
        :param command:
        :return:
        """
        return [i.decode() for i in subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE, ).stdout.readlines()]

    def get_device_model(self) -> str:
        """
        获取设备信息
        :return:
        """
        return self.adb('adb shell getprop ro.product.model')[0].split()[0]

    def get_device(self) -> str:
        """
        获取设备名称
        :return:
        """
        return self.adb('adb devices')[1].strip().split()[0]

    def get_device_bright(self):
        """
        获取设备屏幕亮度
        :return:
        """
        return self.adb('adb shell "settings get system screen_brightness"')[0].strip()

    def get_packages(self, _filter=''):
        """
        获取android设备所有包名
        :param _filter:
        :return:
        """
        name_list = []
        pack = self.adb('adb shell pm list packages')
        if _filter:
            for pack_name in pack:
                if _filter in pack_name:
                    name = str(pack_name).split(':')
                    name_list.append(name[1].split()[0])
            return [name.rstrip() for name in name_list]
        else:
            return [p.rstrip() for p in pack]

    def get_cpu_info(self):
        body = self.adb('adb  shell cat /proc/cpuinfo')

        return body
        # cpu_pro = 0
        # cpu_info = ''
        # if len(body) >= 1:
        #     for i in body:
        #         if 'processor' in i.split():
        #             cpu_pro += 1
        #         if 'Hardware' in i.split():
        #             cpu_info = i.split()[2] + '_' + i.split()[3] + '_' + i.split()[4]
        #     return str(cpu_info), str(cpu_pro)

    def get_device_cpu(self):
        """
        获取设备cpu数量及序列号
        :return:
        """

        body = self.adb('adb  shell cat /proc/cpuinfo')

        cpu_info = {}
        for by in body:
            content = [i.strip() for i in by.split(':')]
            key = content[0]
            value = content[-1]
            cpu_info[key] = value

        return cpu_info


adb = ADB()

if __name__ == '__main__':
    # print(adb.get_device_model())
    print((adb.get_device()))
    # print(len(adb.get_device()))
    # print(adb.get_device_bright())
    # print(adb.get_pack_3())
    # print(adb.get_cpu_info())
    # print(adb.get_device_cpu())
