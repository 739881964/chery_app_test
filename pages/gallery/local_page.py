# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：local_page.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/22
# 当前系统时间：17:40
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class LocalPage(BasePage):
    """
    图库-本地
    """

    # locators
    local_locator = (By.XPATH, '//android.widget.LinearLayout[@content-desc="本地"]/android.widget.TextView')
    picture_locator = (By.XPATH, '(//android.view.ViewGroup[@content-desc="浏览模式"])')
    back_locator = (By.ID, 'com.mega.chery.gallery:id/backBtn')
    picture_name_locator = (By.ID, 'com.mega.chery.gallery:id/title')
    set_wallpaper_locator = (By.ID, 'com.mega.chery.gallery:id/wallpaperBtn')
    auto_broadcast_locator = (By.ID, 'com.mega.chery.gallery:id/slideshowBtn')
    export_locator = (By.ID, 'com.mega.chery.gallery:id/exportBtn')
    delete_locator = (By.ID, 'com.mega.chery.gallery:id/deleteBtn')
    setting_wallpaper_locator = (By.ID, 'com.mega.chery.gallery:id/setWallpaperBtn')
    wallpaper_back_locator = (By.ID, 'com.mega.chery.gallery:id/cancelSetWallpaperBtn')
    local_edit_locator = (By.ID, 'com.mega.chery.gallery:id/editBtn')
    local_export_locator = (By.ID, 'com.mega.chery.gallery:id/exportBtn')
    all_select_locator = (By.ID, 'com.mega.chery.gallery:id/selectAllBtn')
    type_picture_locator = (By.ID, 'com.mega.chery.gallery:id/viewTypeBtn')
    view_mode_locator = (By.XPATH, '//android.view.ViewGroup[@content-desc="浏览模式"]')

    # elements
    wallpaper_back_elem = Element(wallpaper_back_locator, method='click', desc='设置壁纸-返回按钮')
    setting_wallpaper_elem = Element(setting_wallpaper_locator, method='click', desc='设置壁纸按钮')
    auto_broadcast_elem = Element(auto_broadcast_locator, method='click', desc='自动播放图片')
    local_export_elem = Element(local_export_locator, method='presence', desc='本地导出按钮')
    delete_elem = Element(delete_locator, method='click', desc='删除按钮')
    set_wallpaper_elem = Element(set_wallpaper_locator, method='click', desc='设置壁纸')
    picture_name_elem = Element(picture_name_locator, method='click', desc='获取图片名称')
    back_elem = Element(back_locator, method='click', desc='返回按钮')
    local_edit_elem = Element(local_edit_locator, method='click', desc='本地-编辑')
    export_elem = Element(export_locator, method='click', desc='图片中导出按钮')
    local_elem = Element(locator=local_locator, method='click', desc='usb按钮')
    all_select_elem = Element(locator=all_select_locator, method='click', desc='全选')
    type_picture_elem = Element(locator=type_picture_locator, method='click', desc='图片分类')
    view_mode_elem = Element(locator=view_mode_locator, method='click', desc='浏览模式')

    @property
    def picture_elem(self) -> (WebElement, str):
        """
        随机选择图片
        :return:
        """
        picture = self.find_elements(self.picture_locator)
        if picture:
            return self.wait_click_element(picture[self.generate_random(0, len(picture) - 1)])
        return NoSuchElementException

    def swipe_picture(self):
        """
        滑动图片
        :return:
        """
        self.swipe_up_and_down(2000, 700, 400, 700)

    def look_picture(self):
        """
        查看图片
        :return:
        """
        self.picture_elem.click()
        sleep(1)
        self.back_elem.click()
        sleep(1)

    def enlarge_pic(self):
        """
        放大图片
        :return:
        """
        picture = self.picture_elem
        picture.click()
        sleep(1)
        self.double_click(picture)
        sleep(1)
        self.back_elem.click()
        sleep(1)
