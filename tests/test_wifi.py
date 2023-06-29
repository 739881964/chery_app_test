# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_wifi.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/27
# 当前系统时间：15:50
# 用于创建文件的IDE的名称: PyCharm

import pytest
import allure

from data.wifi_data import wifi_success_data, wifi_error_data, no_password_data
from scripts.logger import logger
from time import sleep


@allure.feature('wifi功能测试')
@pytest.mark.skipif(reason='缺少设备，暂时无法测试')
class TestWiFi:
    """
    测试wifi连接
    """

    @allure.story('wifi连接-密码错误')
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.error_passwd
    @pytest.mark.parametrize('error_passwd', wifi_error_data)
    def test_connect_error_passwd(self, error_passwd, init_wifi):
        """
        密码错误，wifi连接失败测试用例
        :param error_passwd:
        :param init_wifi:
        :return:
        """
        wifi_page = init_wifi
        name = error_passwd[0]
        passwd = error_passwd[1]
        error_toast = error_passwd[2]
        if not wifi_page.wifi_button_property:
            wifi_page.wifi_switch_widget_elem.click()

        wifi_page.connect_wifi_step(name, passwd)
        sleep(2)
        actual_toast = wifi_page.show_toast(error_toast)
        logger.info('错误提示: {}'.format(actual_toast))
        try:
            assert error_toast in actual_toast
            logger.info('连接wifi：<<{}>> 失败，密码 <<{}>>错误，请重新输入密码'.format(name, passwd))
        except AssertionError as e:
            # logger.error('连接wifi：<<{}>> 失败'.format(name))
            logger.error(e)
            raise e
        finally:
            wifi_page.tap_wifi_screen()

    @allure.story('wifi首次连接成功-需要密码')
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('success_name', wifi_success_data)
    @pytest.mark.connect_success
    def test_connect_wifi_success_02(self, success_name, init_wifi):
        """
        首次连接wifi成功用例
        :param success_name:
        :param init_wifi:
        :return:
        """
        wifi_page = init_wifi
        name = success_name[0]
        passwd = success_name[-1]
        if not wifi_page.wifi_button_property:
            wifi_page.wifi_switch_widget_elem.click()

        wifi_page.connect_wifi_step(name, passwd)
        sleep(2)
        try:
            assert wifi_page.connect_exist is True
            logger.info('连接wifi：<<{}>> 成功'.format(name))
        except AssertionError as e:
            logger.error('连接wifi：<<{}>> 失败'.format(name))
            logger.error(e)
            raise e
        else:
            wifi_page.wifi_name(name).click()
            wifi_page.disconnect_sure_elem.click()
            # wifi_page.wifi_delete_elem.click()
        finally:
            wifi_page.tap_wifi_screen()

    @allure.story('wifi连接-无密码连接成功')
    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('no_password', no_password_data)
    @pytest.mark.reconnect_no_password_success
    def test_reconnect_wifi_success_with_no_password_03(self, no_password, init_wifi):
        """
        连接wifi-无密码成功用例
        :param no_password:
        :param init_wifi:
        :return:
        """
        wifi_page = init_wifi
        name = no_password[0]
        if not wifi_page.wifi_button_property:
            wifi_page.wifi_switch_widget_elem.click()
        wifi_page.wifi_arrow_elem.click()

        sleep(2)
        wifi_page.wifi_name(name).click()
        wifi_page.connect_sure_elem.click()
        sleep(2)
        try:
            assert wifi_page.connect_exist is True
            logger.info('连接wifi：<<{}>> 成功'.format(name))
        except AssertionError as e:
            logger.error('连接wifi：<<{}>> 失败'.format(name))
            logger.error(e)
            raise e
        else:
            wifi_page.wifi_name(name).click()
            wifi_page.disconnect_sure_elem.click()
            wifi_page.wifi_delete_elem.click()
            wifi_page.disconnect_sure_elem.click()
        finally:
            wifi_page.tap_wifi_screen()
