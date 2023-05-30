# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：test_show.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/25
# 当前系统时间：15:27
# 用于创建文件的IDE的名称: PyCharm

import allure
import pytest
from data.kinds_of_theme import theme_data, show_mode_data

from scripts.logger import logger
from time import sleep


@allure.feature('测试车辆设置-显示功能')
class TestShow:
    """
    车辆显示功能测试
    """

    @pytest.mark.off_video_limiter
    @allure.story('关闭视频限制功能')
    def test_off_video_limiter(self, init_show):
        """
        关闭视频限制功能
        :param init_show:
        :return:
        """
        show_page = init_show
        show_page.scroll_to_show()
        show_page.scroll_to_last()

        checked = show_page.video_limiter_elem.get_attribute('checked')
        if checked == 'false':
            logger.info('视频限制开关已关闭，正在重新开启-关闭')
            for i in range(2):
                show_page.video_limiter_elem.click()
        show_page.video_limiter_elem.click()

        checked_result = show_page.video_limiter_elem.get_attribute('checked')
        logger.info('video limiter checked is: {}'.format(checked))
        try:
            assert checked_result == 'false'
            logger.info('video limiter checked is: {}'.format(checked_result))
        except AssertionError as e:
            logger.info(e)

    @pytest.mark.on_video_limiter
    @allure.story('开启视频限制功能')
    def test_on_video_limiter(self, init_show):
        """
        开启视频限制功能
        :param init_show:
        :return:
        """
        show_page = init_show
        show_page.scroll_to_show()
        show_page.scroll_to_last()

        checked = show_page.video_limiter_elem.get_attribute('checked')
        if checked == 'true':
            logger.info('视频限制开关已开启，正在重新关闭-开启')
            for i in range(2):
                show_page.video_limiter_elem.click()
        show_page.video_limiter_elem.click()

        checked_result = show_page.video_limiter_elem.get_attribute('checked')
        logger.info('video limiter checked is: {}'.format(checked))
        try:
            assert checked_result == 'true'
            logger.info('video limiter checked is: {}'.format(checked_result))
        except AssertionError as e:
            logger.info(e)

    @pytest.mark.select_show_mode
    @allure.story('显示模式选择')
    @pytest.mark.parametrize('select_data', show_mode_data)
    def test_select_show_mode(self, init_show, select_data):
        """
        选择不同的显示模式
        :param init_show:
        :param select_data:
        :return:
        """
        show_page = init_show
        show_page.scroll_to_show()

        change_data = select_data[0]
        show_page.show_mode_select_elem(change_data).click()

        checked = show_page.show_mode_select_elem(change_data).get_attribute('checked')
        logger.info('show mode checked is: {}'.format(checked))

        try:
            assert checked == select_data[-1]
            logger.info('切换显示模式为 [{}] 成功'.format(change_data))
        except AssertionError as e:
            logger.error(e)

    @allure.story('测试清洗屏幕功能')
    @pytest.mark.test_screen_clear
    def test_clear_screen(self, init_show):
        """
        显示-屏幕清洁功能
        :param init_show:
        :return:
        """
        show_page = init_show
        show_page.clear_screen()

        return_page = show_page.screen_clear_elem.text
        try:
            assert return_page == '清洁屏幕'
            logger.info('清洁屏幕成功')
        except AssertionError as e:
            logger.error(e)

    @allure.story('测试更换主题功能')
    @pytest.mark.modify_theme
    @pytest.mark.parametrize('data', theme_data)
    def test_modify_theme(self, data, init_show):
        """
        修改主题功能
        :param init_show:
        :return:
        """
        show_page = init_show
        show_page.scroll_to_show()
        show_page.modify_theme_elem.click()

        theme = data[0]
        logger.info('选择的主题为: {}'.format(theme))
        show_page.choose_theme(theme).click()

        # show_page.current_window_handle().refresh()
        # 重新进入主题选择
        show_page.return_elem.click()
        show_page.modify_theme_elem.click()

        checked = show_page.choose_theme(theme).get_attribute('checked')
        logger.info('theme_checked: {}'.format(checked))
        try:
            assert checked == data[-1]
            logger.info('choose theme success, checked is {}'.format(checked))
        except AssertionError as e:
            logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main()
