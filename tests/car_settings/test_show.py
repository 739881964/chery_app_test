# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：test_show.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/25
# 当前系统时间：15:27
# 用于创建文件的IDE的名称: PyCharm

import pytest


class TestShow:
    """
    车辆显示功能测试
    """

    @pytest.mark.test_clear_screen
    def test_clear_screen(self, init_show):
        """
        显示-屏幕清洁功能
        :param init_show:
        :return:
        """
        show_page = init_show
        show_page.clear_screen()
        print('清洁屏幕成功')

    @pytest.mark.modify_theme
    def test_modify_theme(self, init_show):
        """
        修改主题功能
        :param init_show:
        :return:
        """
        show_page = init_show
        show_page.scroll_to_show()
        show_page.modify_theme_elem.click()
        pass


if __name__ == '__main__':
    pytest.main()
