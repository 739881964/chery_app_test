# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_menu_light.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/10
# 当前系统时间：10:47
# 用于创建文件的IDE的名称: PyCharm

import logging
import pytest
from pages.menu_light_page import MenuLightPage

from data.meun_light_data import light_value_data


class TestMenuLight:
    """
    外灯
    """

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
        # menu_light_page = MenuLightPage(driver)
        # 获取对应的模式value、是否被选中true/false
        mode_key, bool_key = data[0], data[-1]
        # 设置灯光的模式操作步骤
        menu_light_page.set_light(mode_key)

        # 获取大灯设置模式对应的checked属性值
        result = menu_light_page.light_set_elem(mode_key).get_attribute('checked')
        try:
            assert result == bool_key, f'切换大灯-{mode_key}-模式成功'
            logging.info(result, " = ", bool_key)
        except AssertionError as e:
            logging.error(result, ' != ', bool_key)
            raise e


if __name__ == '__main__':
    pytest.main()
