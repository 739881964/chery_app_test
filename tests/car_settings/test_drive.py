# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_drive.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/30
# 当前系统时间：16:30
# 用于创建文件的IDE的名称: PyCharm

import allure
import pytest

from data.drive_data import drive_data, energy_level_data
from scripts.logger import logger
from time import sleep


@allure.feature('测试驾驶功能')
class TestDrive:
    """
    测试驾驶功能
    """

    @pytest.mark.parametrize('recovery_data', energy_level_data)
    @pytest.mark.flaky(reruns=3)
    @allure.story('选择能量回收等级')
    @pytest.mark.test_energy_recovery
    def test_select_energy_recovery_level(self, init_drive, recovery_data):
        """
        选择能量回收等级
        :param init_drive:
        :param recovery_data:
        :return:
        """
        drive_page = init_drive
        # drive_page.swipe_to_energy()

        level_name = recovery_data[0]
        excepted_result = recovery_data[1]
        logger.info('选择的能量回收的等级为: {}'.format(level_name))

        drive_page.select_energy(level_name)
        sleep(3)

        checked = drive_page.energy_recovery_level_select(level_name).get_attribute('checked')

        try:
            assert excepted_result == checked, True
            logger.info('energy recovery level checked is: {}'.format(checked))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.skipif(reason='功能优化，暂时无法使用')
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
