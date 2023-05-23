# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：usbcan2.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/23
# 当前系统时间：10:30
# 用于创建文件的IDE的名称: PyCharm

from zlgcan import *
import time
import platform

zcanlib = ZCAN()


def open_usbcan2():
    device_handle = zcanlib.OpenDevice(ZCAN_USBCAN2, 0, 0)
    if device_handle == INVALID_DEVICE_HANDLE:
        print("Open Device failed!")
        exit(0)
    print("device handle:%d." % (device_handle))
    # info = zcanlib.GetDeviceInf(device_handle)
    # print("Device Information:\n%s" %(info))
    return device_handle


def open_channel(device_handle, channel):
    chn_init_cfg = ZCAN_CHANNEL_INIT_CONFIG()
    chn_init_cfg.can_type = ZCAN_TYPE_CAN
    chn_init_cfg.config.can.acc_mode = 0
    chn_init_cfg.config.can.acc_mask = 0xFFFFFFFF
    # From dev_info.json
    # 250K: (1,28)
    # 500K: (0,28)
    # 1M  : (0,20)
    chn_init_cfg.config.can.timing0 = 0
    chn_init_cfg.config.can.timing1 = 28
    chn_handle = zcanlib.InitCAN(device_handle, channel, chn_init_cfg)
    if chn_handle is None:
        return None
    zcanlib.StartCAN(chn_handle)
    return chn_handle


def transmit_can(chn_handle, stdorext, id, data, len):
    transmit_num = 1
    msgs = (ZCAN_Transmit_Data * transmit_num)()
    for i in range(transmit_num):
        msgs[i].transmit_type = 0  # Send Self
        msgs[i].frame.eff = 0
        if stdorext:
            msgs[i].frame.eff = 1  # extern frame
        msgs[i].frame.rtr = 0  # remote frame
        msgs[i].frame.can_id = id
        msgs[i].frame.can_dlc = len
        for j in range(msgs[i].frame.can_dlc):
            msgs[i].frame.data[j] = data[j]
    ret = zcanlib.Transmit(chn_handle, msgs, transmit_num)
    # print("Tranmit Num: %d." % ret)ret


def receive_can(chn_handle):
    rcv_num = zcanlib.GetReceiveNum(chn_handle, ZCAN_TYPE_CAN)
    if rcv_num:
        print("Receive CAN message number:%d" % rcv_num)
        rcv_msg, rcv_num = zcanlib.Receive(chn_handle, rcv_num)
        for i in range(rcv_num):
            print("[%d]:ts:%d, id:0x%x, dlc:%d, eff:%d, rtr:%d, data:%s" % (i, rcv_msg[i].timestamp,
                                                                            rcv_msg[i].frame.can_id,
                                                                            rcv_msg[i].frame.can_dlc,
                                                                            rcv_msg[i].frame.eff, rcv_msg[i].frame.rtr,
                                                                            ''.join(
                                                                                hex(rcv_msg[i].frame.data[j])[2:] + ' '
                                                                                for j in
                                                                                range(rcv_msg[i].frame.can_dlc))))


if __name__ == "__main__":

    # dll support
    if platform.python_version() >= '3.8.0':
        import os

        os.add_dll_directory(os.getcwd())

    # open device and channel 0
    dev_handle = open_usbcan2()
    chn_handle = open_channel(dev_handle, 0)
    chn1_handle = open_channel(dev_handle, 1)
    print("channel 0 handle:%d." % (chn_handle))
    print("channel 1 handle:%d." % (chn_handle))

    # send can message
    data = [0, 1, 2, 3, 4, 5, 6, 0xFF]
    for i in range(2):
        transmit_can(chn_handle, 0, 0x100, data, 6)
        transmit_can(chn1_handle, 0, 0x101, data, 7)
        transmit_can(chn_handle, 1, 0x12345678, data, 8)
        transmit_can(chn1_handle, 1, 0x12345679, data, 8)
        data[0] = data[0] + 1
        time.sleep(0.1)

    # receive can message
    zcanlib.ClearBuffer(chn_handle)
    time.sleep(3)
    receive_can(chn_handle)
    receive_can(chn1_handle)

    # Close Channel
    zcanlib.ResetCAN(chn_handle)
    zcanlib.ResetCAN(chn1_handle)
    # Close Device
    zcanlib.CloseDevice(dev_handle)
    print("Finished")
