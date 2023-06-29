# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_weather.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/28
# 当前系统时间：14:15
# 用于创建文件的IDE的名称: PyCharm

import allure
import pytest

from scripts.logger import logger
from data.weather_data import new_city


@allure.feature('天气app测试')
# @pytest.mark.skipif(reason='stop testing')
class TestWeather:
    """
    天气App测试
    """

    @allure.story('新增城市测试')
    @pytest.mark.parametrize('city_name', new_city)
    @pytest.mark.flaky(rerun=3)
    @pytest.mark.add_city
    def test_add_city(self, init_weather, city_name):
        """
        新增城市功能
        :param init_weather:
        :param city_name:
        :return:
        """
        city = city_name[0]
        weather_page = init_weather
        weather_page.more_action_elem.click()
        weather_page.add_city_elem.click()
        weather_page.search_city(city_name=city)
        weather_page.search_button_elem.click()
        weather_page.first_add_elem.click()
        try:
            if weather_page.gain_warning_attribute:
                weather_page.alert_close_elem.click()
        except Exception as e:
            logger.warning(e)

        try:
            assert city in weather_page.gain_city_name
            logger.info('天气app新增城市 <<{}>> 成功'.format(city))
        except AssertionError as e:
            logger.error(e)
            raise e
