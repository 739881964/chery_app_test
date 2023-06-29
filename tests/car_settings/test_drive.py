# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_drive.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/30
# 当前系统时间：16:30
# 用于创建文件的IDE的名称: PyCharm

import allure
import pytest

from data.drive_data import drive_data
from scripts.logger import logger
from time import sleep


@allure.feature('测试驾驶功能')
class TestDrive:
    """
    测试驾驶功能
    """

    @allure.story('选择不同的驾驶模式')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('data', drive_data)
    @pytest.mark.select_drive_1
    def test_select_drive(self, init_drive, data):
        """
        选择不同的驾驶模式
        :return:
        """
        drive_page = init_drive

        mode = data[0]
        logger.info('选择的驾驶模式为: {}'.format(mode))
        drive_page.select_drive_mode(mode)

        sleep(3)

        checked = drive_page.drive_list_select_elem(mode).get_attribute('checked')
        logger.info('选择的驾驶模式bool值是: {}'.format(checked))

        try:
            assert checked == data[-1]
            logger.info('drive mode checked is: {}'.format(checked))
        except AssertionError as e:
            logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main()
