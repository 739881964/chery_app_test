# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_common_used.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/7/3
# 当前系统时间：16:56
# 用于创建文件的IDE的名称: PyCharm

import pytest
import allure

from data.common_used_data import lock_data
from time import sleep
from scripts.logger import logger


# lock_data = [(1, 3, 5,), ]


class TestCommonUsed:
    """
    测试'车辆设置-常用'功能
    """

    @pytest.mark.flaky(rerun=3)
    @allure.story('选择不同的常用车锁')
    @pytest.mark.parametrize('common_lock_data', lock_data)
    @pytest.mark.test_lock_select
    def test_lock_select(self, init_common, common_lock_data):
        """
        选择不同的常用车锁
        :param init_common:
        :param common_lock_data:
        :return:
        """
        common_page = init_common
        case_title = common_lock_data[0]
        locator = common_lock_data[1]

        origin_checked = common_page.gain_elem_property(locator)
        common_page.select_lock(locator).click()
        sleep(3)
        try:
            last_checked = common_page.gain_elem_property(locator)
            assert origin_checked != last_checked
            logger.info('切换 {} 成功，状态从 {} -> {}'.format(case_title, origin_checked, last_checked))
        except AssertionError as e:
            logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main()
