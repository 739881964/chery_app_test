# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：launcher_page.py
# 当前用户的登录名：73988
# 当前系统日期：2023/6/13
# 当前系统时间：15:24
# 用于创建文件的IDE的名称: PyCharm

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element


class LauncherPage(BasePage, Element):
    """
    launcher页面
    """

    app_list_locator = (By.ID, 'com.android.launcher3:id/list_text')

    @property
    def app_list_elems(self):
        """
        获取launcher app list
        :return:
        """
        return self.find_elements(self.app_list_locator)
