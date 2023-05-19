# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_btphone.py
# 当前用户的登录名：yuxiang
# 当前编辑文件名：test_bt
# 当前系统日期：2023/5/18
# 当前系统时间：18:34
# 用于创建文件的IDE的名称: PyCharm


import pytest
import logging

from pages.btphone_page import BTPhonePage
from pages.connect_page import ConnectPage


class TestBTPhone:
    """
    测试蓝牙电话功能
    """

    @pytest.mark.test_open_bt
    def test_open_bt(self, init_btphone):
        """
        打开蓝牙
        :return:
        """
        btphone_page, connect_page = init_btphone
        btphone_page.conn_bt_elem.click()
        text = connect_page.bt_button_elem.get_attribute('checked')
        if text == 'true':
            assert text == 'true', '蓝牙已打开'
            print('蓝牙已打开')
        else:
            connect_page.bt_button_elem.click()
            result = connect_page.bt_button_elem.get_attribute('checked')
            try:
                assert result == 'true'
                print('蓝牙开启成功')
            except AssertionError as e:
                print('打开蓝牙失败')
                raise e

    @pytest.mark.test_close_bt
    def test_close_bt(self, init_btphone):
        """
        关闭蓝牙
        :return:
        """
        btphone_page, connect_page = init_btphone
        btphone_page.conn_bt_elem.click()
        text = connect_page.bt_button_elem.get_attribute('checked')
        if text == 'false':
            assert text == 'true', '蓝牙已关闭'
            print('蓝牙已关闭')
        else:
            connect_page.bt_button_elem.click()
            result = connect_page.bt_button_elem.get_attribute('checked')
            try:
                assert result == 'false'
                print('蓝牙关闭成功')
            except AssertionError as e:
                print('关闭蓝牙失败')
                raise e

    @pytest.mark.save_bt_name
    def test_edit_bt_name(self, init_btphone):
        """
        编辑蓝牙名称功能
        :param init_btphone:
        :return:
        """
        bt_page, conn_page = init_btphone
        new_name = 'test_bt_name'
        bt_page.conn_bt_elem.click()
        text = conn_page.bt_button_elem.get_attribute('checked')

        if text == 'false':
            conn_page.bt_button_elem.click()
        # if text == 'true':
        #     bt_page.new_bt_name(new_name)
        # else:
        #     conn_page.bt_button_elem.click()
        bt_page.new_bt_name(new_name)

        name = bt_page.bt_name_elem.text
        try:
            assert new_name == name
            print('修改蓝牙名称为：{} 成功'.format(new_name))
        except AssertionError as e:
            print('修改蓝牙名称为：{} 失败'.format(new_name))
            raise e


if __name__ == '__main__':
    pytest.main()
