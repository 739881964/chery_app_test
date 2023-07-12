# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_car_setting.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/8
# 当前系统时间：16:43
# 用于创建文件的IDE的名称: PyCharm

import pytest


# @pytest.mark.screen_clear
class TestCarSetting:
    """
    车辆设置
    """

    @pytest.mark.skipif(reason='用例已废弃')
    @pytest.mark.flaky(reruns=3)
    # @pytest.mark.parametrize()
    @pytest.mark.screen_clear
    def test_screen_clear(self, init_setting):
        """
        车辆设置-显示-屏幕清洗
        :param init_setting:
        :return:
        """
        # car_setting_page = init_setting
        # # car_setting_page = CarSettingPage(driver)
        # print('')
        # car_setting_page.clear_screen()
        #
        # assert car_setting_page.clear_button_elem.text == "清洁屏幕"
        pass


if __name__ == '__main__':
    pytest.main()
