# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：test_launcher.py
# 当前用户的登录名：73988
# 当前系统日期：2023/6/13
# 当前系统时间：15:24
# 用于创建文件的IDE的名称: PyCharm


import pytest
from scripts.logger import logger


class TestLauncher:

    @pytest.mark.launcher_app
    def test_launcher_app(self, init_launcher):
        """
        测试launcher功能
        :param init_launcher:
        :return:
        """
        launcher_page = init_launcher
        lists = launcher_page.app_list_elems

        try:
            assert len(lists) == 18
            logger.info(lists)
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.swipe_launcher
    def test_swipe_launcher(self, init_launcher):
        """
        滑动launcher
        :param init_launcher:
        :return:
        """
        launcher_page = init_launcher
        p_source = launcher_page.get_page_source()
        logger.info('p_source: {}'.format(p_source))
        launcher_page.swipe_up_and_down(2000, 600, 300, 600)
        source = launcher_page.get_page_source()
        logger.info('source: {}'.format(source))
        try:
            assert p_source != source
            logger.info('launcher滑动成功')
        except AssertionError as e:
            logger.error('launcher滑动失败')
            raise e

    @pytest.mark.skipif(reason='还在开发中，暂不开放')
    def test_control_bar(self, init_launcher):
        """
        操作状态栏
        :param init_launcher:
        :return:
        """
        launcher_page = init_launcher
        result = launcher_page.get_system_bar()
        print(result)
