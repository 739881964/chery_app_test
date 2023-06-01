# -*- coding:utf-8 -*-
#  zlgcan.py
#
#  ~~~~~~~~~~~~
#
#  ZLGCAN API
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : guochuangjian    
#  Last change: 23.05.2023
#
#  Language: Python 2.7, 3.6, 3.10
#  ------------------------------------------------------------------
#
from ctypes import *
import platform

ZCAN_DEVICE_TYPE = c_uint

INVALID_DEVICE_HANDLE = 0
INVALID_CHANNEL_HANDLE = 0

'''
 Device Type
'''
ZCAN_PCI5121 = ZCAN_DEVICE_TYPE(1)
ZCAN_PCI9810 = ZCAN_DEVICE_TYPE(2)
ZCAN_USBCAN1 = ZCAN_DEVICE_TYPE(3)
ZCAN_USBCAN2 = ZCAN_DEVICE_TYPE(4)
ZCAN_PCI9820 = ZCAN_DEVICE_TYPE(5)
ZCAN_CAN232 = ZCAN_DEVICE_TYPE(6)
ZCAN_PCI5110 = ZCAN_DEVICE_TYPE(7)
ZCAN_CANLITE = ZCAN_DEVICE_TYPE(8)
ZCAN_ISA9620 = ZCAN_DEVICE_TYPE(9)
ZCAN_ISA5420 = ZCAN_DEVICE_TYPE(10)
ZCAN_PC104CAN = ZCAN_DEVICE_TYPE(11)
ZCAN_CANETUDP = ZCAN_DEVICE_TYPE(12)
ZCAN_CANETE = ZCAN_DEVICE_TYPE(12)
ZCAN_DNP9810 = ZCAN_DEVICE_TYPE(13)
ZCAN_PCI9840 = ZCAN_DEVICE_TYPE(14)
ZCAN_PC104CAN2 = ZCAN_DEVICE_TYPE(15)
ZCAN_PCI9820I = ZCAN_DEVICE_TYPE(16)
ZCAN_CANETTCP = ZCAN_DEVICE_TYPE(17)
ZCAN_PCIE_9220 = ZCAN_DEVICE_TYPE(18)
ZCAN_PCI5010U = ZCAN_DEVICE_TYPE(19)
ZCAN_USBCAN_E_U = ZCAN_DEVICE_TYPE(20)
ZCAN_USBCAN_2E_U = ZCAN_DEVICE_TYPE(21)
ZCAN_PCI5020U = ZCAN_DEVICE_TYPE(22)
ZCAN_EG20T_CAN = ZCAN_DEVICE_TYPE(23)
ZCAN_PCIE9221 = ZCAN_DEVICE_TYPE(24)
ZCAN_WIFICAN_TCP = ZCAN_DEVICE_TYPE(25)
ZCAN_WIFICAN_UDP = ZCAN_DEVICE_TYPE(26)
ZCAN_PCIe9120 = ZCAN_DEVICE_TYPE(27)
ZCAN_PCIe9110 = ZCAN_DEVICE_TYPE(28)
ZCAN_PCIe9140 = ZCAN_DEVICE_TYPE(29)
ZCAN_USBCAN_4E_U = ZCAN_DEVICE_TYPE(31)
ZCAN_CANDTU_200UR = ZCAN_DEVICE_TYPE(32)
ZCAN_CANDTU_MINI = ZCAN_DEVICE_TYPE(33)
ZCAN_USBCAN_8E_U = ZCAN_DEVICE_TYPE(34)
ZCAN_CANREPLAY = ZCAN_DEVICE_TYPE(35)
ZCAN_CANDTU_NET = ZCAN_DEVICE_TYPE(36)
ZCAN_CANDTU_100UR = ZCAN_DEVICE_TYPE(37)
ZCAN_PCIE_CANFD_100U = ZCAN_DEVICE_TYPE(38)
ZCAN_PCIE_CANFD_200U = ZCAN_DEVICE_TYPE(39)
ZCAN_PCIE_CANFD_400U = ZCAN_DEVICE_TYPE(40)
ZCAN_USBCANFD_200U = ZCAN_DEVICE_TYPE(41)
ZCAN_USBCANFD_100U = ZCAN_DEVICE_TYPE(42)
ZCAN_USBCANFD_MINI = ZCAN_DEVICE_TYPE(43)
ZCAN_CANFDCOM_100IE = ZCAN_DEVICE_TYPE(44)
ZCAN_CANSCOPE = ZCAN_DEVICE_TYPE(45)
ZCAN_CLOUD = ZCAN_DEVICE_TYPE(46)
ZCAN_CANDTU_NET_400 = ZCAN_DEVICE_TYPE(47)
ZCAN_VIRTUAL_DEVICE = ZCAN_DEVICE_TYPE(99)

'''
 Interface return status
'''
ZCAN_STATUS_ERR = 0
ZCAN_STATUS_OK = 1
ZCAN_STATUS_ONLINE = 2
ZCAN_STATUS_OFFLINE = 3
ZCAN_STATUS_UNSUPPORTED = 4

'''
 CAN type
'''
ZCAN_TYPE_CAN = c_uint(0)
ZCAN_TYPE_CANFD = c_uint(1)

'''
 Device information
'''


class ZCanDeviceInfo(Structure):
    _fields_ = [("hw_Version", c_ushort),
                ("fw_Version", c_ushort),
                ("dr_Version", c_ushort),
                ("in_Version", c_ushort),
                ("irq_Num", c_ushort),
                ("can_Num", c_ubyte),
                ("str_Serial_Num", c_ubyte * 20),
                ("str_hw_Type", c_ubyte * 40),
                ("reserved", c_ushort * 4)]

    def __str__(self):
        return "Hardware Version:%s\nFirmware Version:%s\nDriver Interface:%s\nInterface Interface:%s\nInterrupt Number:%d\nCAN Number:%d\nSerial:%s\nHardware Type:%s\n" % ( \
            self.hw_version, self.fw_version, self.dr_version, self.in_version, self.irq_num, self.can_num, self.serial,
            self.hw_type)

    @staticmethod
    def _version(version):
        return ("V%02x.%02x" if version // 0xFF >= 9 else "V%d.%02x") % (version // 0xFF, version & 0xFF)

    @property
    def hw_version(self):
        return self._version(self.hw_Version)

    @property
    def fw_version(self):
        return self._version(self.fw_Version)

    @property
    def dr_version(self):
        return self._version(self.dr_Version)

    @property
    def in_version(self):
        return self._version(self.in_Version)

    @property
    def irq_num(self):
        return self.irq_Num

    @property
    def can_num(self):
        return self.can_Num

    @property
    def serial(self):
        serial = ''
        for c in self.str_Serial_Num:
            if c > 0:
                serial += chr(c)
            else:
                break
        return serial

    @property
    def hw_type(self):
        hw_type = ''
        for c in self.str_hw_Type:
            if c > 0:
                hw_type += chr(c)
            else:
                break
        return hw_type


class _ZCanChannelCanInitConfig(Structure):
    _fields_ = [("acc_code", c_uint),
                ("acc_mask", c_uint),
                ("reserved", c_uint),
                ("filter", c_ubyte),
                ("timing0", c_ubyte),
                ("timing1", c_ubyte),
                ("mode", c_ubyte)]


class _ZCanChannelCanFDInitConfig(Structure):
    _fields_ = [("acc_code", c_uint),
                ("acc_mask", c_uint),
                ("abit_timing", c_uint),
                ("dbit_timing", c_uint),
                ("brp", c_uint),
                ("filter", c_ubyte),
                ("mode", c_ubyte),
                ("pad", c_ushort),
                ("reserved", c_uint)]


class _ZCanChannelInitConfig(Union):
    _fields_ = [("can", _ZCanChannelCanInitConfig), ("canfd", _ZCanChannelCanFDInitConfig)]


class ZCanChannelInitConfig(Structure):
    _fields_ = [("can_type", c_uint),
                ("config", _ZCanChannelInitConfig)]


class ZCanChannelErrorInfo(Structure):
    _fields_ = [("error_code", c_uint),
                ("passive_ErrData", c_ubyte * 3),
                ("arLost_ErrData", c_ubyte)]


class ZCanChannelStatus(Structure):
    _fields_ = [("errInterrupt", c_ubyte),
                ("regMode", c_ubyte),
                ("regStatus", c_ubyte),
                ("regALCapture", c_ubyte),
                ("regECCapture", c_ubyte),
                ("regEWLimit", c_ubyte),
                ("regRECounter", c_ubyte),
                ("regTECounter", c_ubyte),
                ("Reserved", c_ubyte)]


class ZCanCanFrame(Structure):
    _fields_ = [("can_id", c_uint, 29),
                ("err", c_uint, 1),
                ("rtr", c_uint, 1),
                ("eff", c_uint, 1),
                ("can_dlc", c_ubyte),
                ("__pad", c_ubyte),
                ("__res0", c_ubyte),
                ("__res1", c_ubyte),
                ("data", c_ubyte * 8)]


class ZCanCanFdFrame(Structure):
    _fields_ = [("can_id", c_uint, 29),
                ("err", c_uint, 1),
                ("rtr", c_uint, 1),
                ("eff", c_uint, 1),
                ("len", c_ubyte),
                ("brs", c_ubyte, 1),
                ("esi", c_ubyte, 1),
                ("__res", c_ubyte, 6),
                ("__res0", c_ubyte),
                ("__res1", c_ubyte),
                ("data", c_ubyte * 64)]


class ZCanTransmitData(Structure):
    _fields_ = [("frame", ZCanCanFrame), ("transmit_type", c_uint)]


class ZCanReceiveData(Structure):
    _fields_ = [("frame", ZCanCanFrame), ("timestamp", c_ulonglong)]


class ZCanTransmitFdData(Structure):
    _fields_ = [("frame", ZCanCanFdFrame), ("transmit_type", c_uint)]


class ZCanReceiveFdData(Structure):
    _fields_ = [("frame", ZCanCanFdFrame), ("timestamp", c_ulonglong)]


class ZCanAutoTransmitObj(Structure):
    _fields_ = [("enable", c_ushort),
                ("index", c_ushort),
                ("interval", c_uint),
                ("obj", ZCanTransmitData)]


class ZCanFdAutoTransmitObj(Structure):
    _fields_ = [("enable", c_ushort),
                ("index", c_ushort),
                ("interval", c_uint),
                ("obj", ZCanTransmitFdData)]


class IProperty(Structure):
    _fields_ = [("SetValue", c_void_p),
                ("GetValue", c_void_p),
                ("GetPropertys", c_void_p)]


class ZCan(object):
    def __init__(self):
        if platform.system() == "Windows":
            self.__dll = windll.LoadLibrary("./zlgcan.dll")
        else:
            print("No support now!")
        if self.__dll is None:
            print("DLL couldn't be loaded!")

    def open_device(self, device_type, device_index, reserved):
        try:
            return self.__dll.ZCAN_OpenDevice(device_type, device_index, reserved)
        except Exception as e:
            print("Exception on OpenDevice!")
            raise e

    def close_device(self, device_handle):
        try:
            return self.__dll.ZCAN_CloseDevice(device_handle)
        except Exception as e:
            print("Exception on CloseDevice!")
            raise e

    def get_device_info(self, device_handle):
        try:
            information = ZCanDeviceInfo()
            res = self.__dll.ZCAN_GetDeviceInf(device_handle, byref(info))
            return information if res == ZCAN_STATUS_OK else None
        except Exception as e:
            print("Exception on ZCAN_GetDeviceInf")
            raise e

    def device_online(self, device_handle):
        try:
            return self.__dll.ZCAN_IsDeviceOnLine(device_handle)
        except Exception as e:
            print("Exception on ZCAN_ZCAN_IsDeviceOnLine!")
            raise e

    def init_can(self, device_handle, can_index, init_config):
        try:
            return self.__dll.ZCAN_InitCAN(device_handle, can_index, byref(init_config))
        except Exception as e:
            print("Exception on ZCAN_InitCAN!")
            raise e

    def start_can(self, channel_handle):
        try:
            return self.__dll.ZCAN_StartCAN(channel_handle)
        except Exception as e:
            print("Exception on ZCAN_StartCAN!")
            raise e

    def reset_can(self, channel_handle):
        try:
            return self.__dll.ZCAN_ResetCAN(channel_handle)
        except Exception as e:
            print("Exception on ZCAN_ResetCAN!")
            raise e

    def clear_buffer(self, channel_handle):
        try:
            return self.__dll.ZCAN_ClearBuffer(channel_handle)
        except Exception as e:
            print("Exception on ZCAN_ClearBuffer!")
            raise

    def read_channel_error_info(self, channel_handle):
        try:
            error_info = ZCanChannelErrorInfo()
            res = self.__dll.ZCAN_ReadChannelErrInfo(channel_handle, byref(error_info))
            return error_info if res == ZCAN_STATUS_OK else None
        except Exception as e:
            print("Exception on ZCAN_ReadChannelErrInfo!")
            raise e

    def read_channel_status(self, channel_handle):
        try:
            status = ZCanChannelStatus()
            res = self.__dll.ZCAN_ReadChannelStatus(channel_handle, byref(status))
            return status if res == ZCAN_STATUS_OK else None
        except Exception as e:
            print("Exception on ZCAN_ReadChannelStatus!")
            raise e

    def get_receive_num(self, channel_handle, can_type=ZCAN_TYPE_CAN):
        try:
            return self.__dll.ZCAN_GetReceiveNum(channel_handle, can_type)
        except Exception as e:
            print("Exception on ZCAN_GetReceiveNum!")
            raise e

    def transmit(self, channel_handle, std_msg, msg_len):
        try:
            return self.__dll.ZCAN_Transmit(channel_handle, byref(std_msg), msg_len)
        except Exception as e:
            print("Exception on ZCAN_Transmit!")
            raise e

    def receive(self, channel_handle, receive_num, wait_time=c_int(-1)):
        try:
            rcv_can_msgs = (ZCanReceiveData * rcv_num)()
            res = self.__dll.ZCAN_Receive(channel_handle, byref(rcv_can_msgs), receive_num, wait_time)
            return rcv_can_msgs, res
        except Exception as e:
            print("Exception on ZCAN_Receive!")
            raise e

    def transmit_fd(self, channel_handle, fd_msg, msf_len):
        try:
            return self.__dll.ZCAN_TransmitFD(channel_handle, byref(fd_msg), msf_len)
        except Exception as e:
            print("Exception on ZCAN_TransmitFD!")
            raise e

    def receive_fd(self, channel_handle, receive_num, wait_time=c_int(-1)):
        try:
            receive_canfd_msg = (ZCanReceiveFdData * rcv_num)()
            res = self.__dll.ZCAN_ReceiveFD(channel_handle, byref(receive_canfd_msg), receive_num, wait_time)
            return rcv_canfd_msgs, res
        except Exception as e:
            print("Exception on ZCAN_ReceiveFD!")
            raise e

    def get_iproperty(self, device_handle):
        try:
            self.__dll.GetIProperty.restype = POINTER(IProperty)
            return self.__dll.GetIProperty(device_handle)
        except Exception as e:
            print("Exception on ZCAN_GetIProperty!")
            raise e

    @staticmethod
    def set_value(iproperty, path, value):
        try:
            func = CFUNCTYPE(c_uint, c_char_p, c_char_p)(iproperty.contents.SetValue)
            return func(c_char_p(path.encode("utf-8")), c_char_p(value.encode("utf-8")))
        except Exception as e:
            print("Exception on IProperty SetValue")
            raise e

    @staticmethod
    def get_value(iproperty, path):
        try:
            func = CFUNCTYPE(c_char_p, c_char_p)(iproperty.contents.GetValue)
            return func(c_char_p(path.encode("utf-8")))
        except Exception as e:
            print("Exception on IProperty GetValue")
            raise e

    def release_iproperty(self, iproperty):
        try:
            return self.__dll.ReleaseIProperty(iproperty)
        except Exception as e:
            print("Exception on ZCAN_ReleaseIProperty!")
            raise e


###############################################################################
'''
USBCANFD-MINI Demo
'''


def can_start(zcanlib, device_handle, channel):
    ip = zcanlib.GetIProperty(device_handle)
    res = zcanlib.SetValue(ip, str(channel) + "/clock", "60000000")
    if res != ZCAN_STATUS_OK:
        print("Set CH%d CANFD clock failed!" % (channel))
    res = zcanlib.SetValue(ip, str(channel) + "/canfd_standard", "0")
    if res != ZCAN_STATUS_OK:
        print("Set CH%d CANFD standard failed!" % (channel))
    res = zcanlib.SetValue(ip, str(channel) + "/initenal_resistance", "1")
    if res != ZCAN_STATUS_OK:
        print("Open CH%d resistance failed!" % (channel))
    res = zcanlib.SetValue(ip, str(channel) + "/canfd_abit_baud_rate", "500000")
    if res != ZCAN_STATUS_OK:
        print("Set CH%d CANFD canfd_abit_baud_rate failed!" % (channel))
    res = zcanlib.SetValue(ip, str(channel) + "/canfd_dbit_baud_rate", "2000000")
    if res != ZCAN_STATUS_OK:
        print("Set CH%d CANFD canfd_dbit_baud_rate failed!" % (channel))
    zcanlib.ReleaseIProperty(ip)

    chn_init_cfg = ZCanChannelInitConfig
    chn_init_cfg.can_type = ZCAN_TYPE_CANFD
    # chn_init_cfg.config.canfd.abit_timing = 0x0001975e #1Mbps
    # chn_init_cfg.config.canfd.dbit_timing = 101166 #1Mbps
    chn_init_cfg.config.canfd.mode = 0
    channel_handle = zcanlib.InitCAN(device_handle, channel, chn_init_cfg)
    if channel_handle is None:
        return None
    zcanlib.StartCAN(channel_handle)
    return channel_handle


if __name__ == "__main__":
    zcan_lib = ZCan()
    handle = zcan_lib.open_device(ZCAN_USBCANFD_MINI, 0, 0)
    if handle == INVALID_DEVICE_HANDLE:
        print("Open Device failed!")
        exit(0)
    print("device handle:%d." % (handle))

    info = zcan_lib.get_device_info(handle)
    print("Device Information:\n%s" % (info))

    # Start CAN
    chn_handle = can_start(zcan_lib, handle, 0)
    print("channel handle:%d." % (chn_handle))

    # Send CAN Messages
    transmit_num = 10
    msgs = (ZCanTransmitData * transmit_num)()
    for i in range(transmit_num):
        msgs[i].transmit_type = 0  # Send Self
        msgs[i].frame.eff = 0  # extern frame
        msgs[i].frame.rtr = 0  # remote frame
        msgs[i].frame.can_id = i
        msgs[i].frame.can_dlc = 8
        for j in range(msgs[i].frame.can_dlc):
            msgs[i].frame.data[j] = j
    ret = zcan_lib.transmit(chn_handle, msgs, transmit_num)
    print("Tranmit Num: %d." % ret)

    # Send CANFD Messages
    # transmit_canfd_num = 10
    # canfd_msgs = (ZCAN_TransmitFD_Data * transmit_canfd_num)()
    # for i in range(transmit_num):
    # canfd_msgs[i].transmit_type = 2 #Send Self
    # canfd_msgs[i].frame.eff     = 0 #extern frame
    # canfd_msgs[i].frame.rtr     = 0 #remote frame
    # canfd_msgs[i].frame.brs     = 1 #BRS
    # canfd_msgs[i].frame.can_id  = i
    # canfd_msgs[i].frame.len     = 8
    # for j in range(canfd_msgs[i].frame.len):
    # canfd_msgs[i].frame.data[j] = j
    # ret = zcanlib.TransmitFD(chn_handle, canfd_msgs, transmit_canfd_num)
    # print("Tranmit CANFD Num: %d." % ret)

    # Recive Messages
    while True:
        rcv_num = zcan_lib.get_receive_num(chn_handle, ZCAN_TYPE_CAN)
        rcv_canfd_num = zcan_lib.get_receive_num(chn_handle, ZCAN_TYPE_CANFD)
        if rcv_num:
            print("Receive CAN message number:%d" % rcv_num)
            rcv_msg, rcv_num = zcan_lib.receive(chn_handle, rcv_num)
            for i in range(rcv_num):
                print("[%d]:ts:%d, id:%d, dlc:%d, eff:%d, rtr:%d, data:%s" % (i, rcv_msg[i].timestamp,
                                                                              rcv_msg[i].frame.can_id,
                                                                              rcv_msg[i].frame.can_dlc,
                                                                              rcv_msg[i].frame.eff,
                                                                              rcv_msg[i].frame.rtr,
                                                                              ''.join(
                                                                                  str(rcv_msg[i].frame.data[j]) + ' '
                                                                                  for j in
                                                                                  range(rcv_msg[i].frame.can_dlc))))
        elif rcv_canfd_num:
            print("Receive CANFD message number:%d" % rcv_canfd_num)
            rcv_canfd_msgs, rcv_canfd_num = zcan_lib.receive_fd(chn_handle, rcv_canfd_num, 1000)
            for i in range(rcv_canfd_num):
                print("[%d]:ts:%d, id:%d, len:%d, eff:%d, rtr:%d, esi:%d, brs: %d, data:%s" % (
                    i, rcv_canfd_msgs[i].timestamp, rcv_canfd_msgs[i].frame.can_id, rcv_canfd_msgs[i].frame.len,
                    rcv_canfd_msgs[i].frame.eff, rcv_canfd_msgs[i].frame.rtr,
                    rcv_canfd_msgs[i].frame.esi, rcv_canfd_msgs[i].frame.brs,
                    ''.join(str(rcv_canfd_msgs[i].frame.data[j]) + ' ' for j in range(rcv_canfd_msgs[i].frame.len))))
        else:
            break

    # Close CAN
    # zcan_lib.reset_can(chn_handle)
    # # Close Device
    # zcan_lib.close_device(handle)

