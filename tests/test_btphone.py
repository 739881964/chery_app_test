# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_btphone.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/18
# 当前系统时间：18:34
# 用于创建文件的IDE的名称: PyCharm


import pytest

from scripts.logger import logger
from data.btphone_name_data import bt_name_data

from time import sleep


class TestBTPhone:
    """
    测试蓝牙电话功能
    """

    @pytest.mark.test_disconnect_device
    def test_reconnect_device(self, init_btphone):
        """
        连接设备异常失败测试用例
        :param init_btphone:
        :return:
        """
        btphone_page, connect_page = init_btphone
        btphone_page.conn_bt_elem.click()

        text = connect_page.bt_button_elem.get_attribute('checked')
        logger.info('蓝牙开关属性为: {}'.format(text))

        # 确保蓝牙打开
        if text == 'true':
            logger.info('蓝牙已打开')
        else:
            connect_page.bt_button_elem.click()

        btphone_page.disconnect_elem.click()
        sleep(10)

        try:
            alert_text = btphone_page.connect_failed_elem.text
            assert alert_text == '配对失败'
            logger.info('蓝牙连接失败，设备不在通讯范围内')
        except AssertionError as e:
            logger.error('蓝牙连接异常')
            raise e
        btphone_page.know_elem.click()

    @pytest.mark.test_open_bt
    def test_open_bt(self, init_btphone):
        """
        打开蓝牙
        :return:
        """
        btphone_page, connect_page = init_btphone
        btphone_page.conn_bt_elem.click()
        text = connect_page.bt_button_elem.get_attribute('checked')
        logger.info('蓝牙开关属性为: {}'.format(text))

        if text == 'true':
            assert text == 'true', '蓝牙已打开'
            logger.info('蓝牙已打开')
        else:
            connect_page.bt_button_elem.click()
            result = connect_page.bt_button_elem.get_attribute('checked')
            try:
                assert result == 'true'
                logger.info('蓝牙打开打开')
            except AssertionError as e:
                logger.error('打开蓝牙失败')
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
        logger.info('蓝牙开关属性为: {}'.format(text))

        if text == 'false':
            assert text == 'true', '蓝牙已关闭'
            logger.info('蓝牙已关闭')
        else:
            connect_page.bt_button_elem.click()
            result = connect_page.bt_button_elem.get_attribute('checked')
            logger.info('蓝牙开关属性为: {}'.format(result))

            try:
                assert result == 'false'
                logger.info('蓝牙关闭成功')
            except AssertionError as e:
                logger.error('关闭蓝牙失败')
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
        logger.info('蓝牙开关属性为: {}'.format(text))

        if text == 'false':
            conn_page.bt_button_elem.click()
        bt_page.new_bt_name(new_name)

        # bt_page.hide_keyboard()
        name = bt_page.bt_name_elem.text
        logger.info('蓝牙名称为: {}'.format(name))

        try:
            assert new_name == name
            logger.info('修改蓝牙名称为：{} 成功'.format(new_name))
        except AssertionError as e:
            logger.error('修改蓝牙名称为：{} 失败'.format(new_name))
            raise e

    @pytest.mark.cancel_edit
    def test_cancel_edit(self, init_btphone):
        """
        取消重命名
        :param init_btphone:
        :return:
        """
        bt_page, conn_page = init_btphone
        bt_page.conn_bt_elem.click()
        text = conn_page.bt_button_elem.get_attribute('checked')
        logger.info('蓝牙开关属性为: {}'.format(text))

        if text == 'false':
            conn_page.bt_button_elem.click()
        b_name = bt_page.bt_name_elem.text

        bt_page.edit_bt_name_elem.click()
        bt_page.hide_keyboard()
        bt_page.cancel_elem.click()
        a_name = bt_page.bt_name_elem.text
        logger.info('蓝牙名称为: {}'.format(a_name))

        try:
            assert b_name == a_name, '返回成功'
            logger.info('取消编辑蓝牙名称成功')
        except AssertionError as e:
            logger.error('取消编辑蓝牙名称成功')
            raise e

    @pytest.mark.test_error_data
    @pytest.mark.parametrize('bt_data', bt_name_data)
    def test_error_name(self, bt_data, init_btphone):
        """
        编辑蓝牙名称，命名异常数据
        :param bt_data:
        :param init_btphone:
        :return:
        """
        bt_page, con_page = init_btphone
        new_name = bt_data[0]
        bt_page.conn_bt_elem.click()
        checked = con_page.bt_button_elem.get_attribute('checked')
        logger.info('蓝牙开关属性为: {}'.format(checked))

        # old_name = bt_page.bt_name_elem.text
        # if checked == 'false':
        #     con_page.bt_button_elem.click()
        bt_page.input_name(new_name)

        # save_enabled = bt_page.save_elem.get_attribute('enabled')
        # if save_enabled == 'false':
        #     bt_page.back_elem.click()
        bt_page.save_elem.click()

        name = bt_page.bt_name_elem.text
        logger.info('蓝牙名称为: {}'.format(name))

        # if save_enabled == 'false':
        #     assert name == old_name
        try:
            if len(new_name) <= 32:
                assert name == new_name
            else:
                assert name == new_name[0:32]
            logger.info('修改蓝牙名称为：{} 成功'.format(name))
        except AssertionError as e:
            logger.error('修改蓝牙名称为：{} 失败'.format(new_name))
            raise e


if __name__ == '__main__':
    pytest.main()
