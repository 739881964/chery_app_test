# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_menu_light.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/10
# 当前系统时间：10:47
# 用于创建文件的IDE的名称: PyCharm

import allure
import pytest

from data.meun_light_data import light_value_data, light_high_data, light_delay_data
from scripts.logger import logger


@allure.feature('车辆设置-外灯')
class TestMenuLight:
    """
    外灯
    """

    @allure.story('大灯延时操作')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.set_light_delay_control
    @pytest.mark.parametrize('delay_data', light_delay_data)
    def test_set_light_delay(self, delay_data, init_menu_light):
        """
        大灯延时操作
        :param init_menu_light:
        :param delay_data:
        :return:
        """
        menu_light_page = init_menu_light
        mode_key, bool_key = delay_data[0], delay_data[-1]
        # 设置灯光的模式操作步骤
        menu_light_page.set_light_delay(mode_key)

        # 获取大灯设置模式对应的checked属性值
        result = menu_light_page.light_delay_elem(mode_key).get_attribute('checked')
        try:
            assert result == bool_key, f'设置大灯延时-{mode_key}-模式成功'
            logger.info('result = {}'.format(bool_key))
        except AssertionError as e:
            logger.error('result !=  {}'.format(bool_key))
            raise e

    @allure.story('大灯高度调节操作')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.set_light_high_control
    @pytest.mark.parametrize('high_data', light_high_data)
    def test_set_light_high(self, high_data, init_menu_light):
        """
        大灯高度调节操作
        :param init_menu_light:
        :param high_data:
        :return:
        """
        menu_light_page = init_menu_light
        mode_key, bool_key = high_data[0], high_data[-1]
        # 设置灯光的模式操作步骤
        menu_light_page.set_light_high(mode_key)

        # 获取大灯设置模式对应的checked属性值
        result = menu_light_page.light_high_control(mode_key).get_attribute('checked')
        try:
            assert result == bool_key, f'切换大灯高度-{mode_key}-模式成功'
            logger.info('result = {}'.format(bool_key))
        except AssertionError as e:
            logger.error('result !=  {}'.format(bool_key))
            raise e

    @allure.story('大灯调节操作')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.set_light_case
    @pytest.mark.parametrize('data', light_value_data)
    def test_set_light(self, data, init_menu_light):
        """
        大灯调节操作
        :param init_menu_light:
        :param data:
        :return:
        """
        menu_light_page = init_menu_light
        mode_key, bool_key = data[0], data[-1]
        # 设置灯光的模式操作步骤
        menu_light_page.set_light(mode_key)

        # 获取大灯设置模式对应的checked属性值
        result = menu_light_page.light_set_elem(mode_key).get_attribute('checked')
        try:
            assert result == bool_key, f'切换大灯-{mode_key}-模式成功'
            logger.info('result = {}'.format(bool_key))
        except AssertionError as e:
            logger.error('result !=  {}'.format(bool_key))
            raise e


if __name__ == '__main__':
    pytest.main()
