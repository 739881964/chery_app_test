# coding: utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：test_gallery.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/22
# 当前系统时间：17:48
# 用于创建文件的IDE的名称: PyCharm

import pytest

from time import sleep
from scripts.logger import logger
from data.picture_data import no_usb_data
from appium.webdriver.webelement import WebElement


class TestGallery:
    """
    图库功能
    """

    @pytest.mark.view_picture
    def test_choose_view_mode_pic(self, init_gallery):
        """
        切换至浏览模式并选择一张图片
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.type_picture_elem.click()
        for i in range(2):
            gallery.picture_elem.click()

        try:
            assert isinstance(gallery.picture_name_elem.text, str)
            logger.info('成功切换至浏览模式并选择一张图片,name is: {}'.format(gallery.picture_name_elem.text))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.type_pic
    def test_switch_pic_type(self, init_gallery):
        """
        查看图片分类
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.type_picture_elem.click()
        view_mode = gallery.picture_elem

        try:
            assert isinstance(view_mode, WebElement)
            logger.info('切换浏览模式成功, view_mode is: {} and type({}) is: {}'.format(view_mode, view_mode, WebElement))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.swipe_picture
    def test_swipe_picture(self, init_gallery):
        """
        随机选择某个图片并滑动至其他图片
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.picture_elem.click()
        pic_name = gallery.picture_name_elem.text
        gallery.swipe_picture()
        swipe_name = gallery.picture_name_elem.text
        try:
            assert pic_name != swipe_name
            logger.info('滑动图片成功， 滑动前图片name：{}； 滑动后图片的name：{}'.format(pic_name, swipe_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.select_all_export
    @pytest.mark.parametrize('data', no_usb_data)
    def test_all_select_export(self, init_gallery, data):
        """
        全选导出照片-无usb，异常用例
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.local_edit_elem.click()
        gallery.all_select_elem.click()
        gallery.export_elem.click()
        text = data[0]
        try:
            toast = gallery.show_toast(text)
            logger.info('错误提示为: {}'.format(toast))
            assert text in toast
            logger.info('导出失败，无usb设备，测试异常导出图片成功')
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.skip(reason='功能实现，但调试时不开放，原因是：删除功能不能随便用')
    @pytest.mark.select_all_delete
    def test_all_select_delete(self, init_gallery):
        """
        全选删除
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.local_edit_elem.click()
        gallery.all_select_elem.click()
        gallery.delete_elem.click()
        try:
            pass
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.select_all
    def test_all_select(self, init_gallery):
        """
        全选
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.local_edit_elem.click()
        d_type = gallery.delete_elem
        logger.info('before delete property is : {}'.format(d_type))
        gallery.all_select_elem.click()
        _d_type = gallery.delete_elem
        logger.info('after delete property is : {}'.format(_d_type))
        try:
            assert d_type != _d_type
            logger.info('图片已被全部选中')
        except AssertionError as e:
            logger.info(e)
            raise e

    @pytest.mark.parametrize('data', no_usb_data)
    @pytest.mark.random_select_pic
    def test_random_select_pic_explore(self, data, init_gallery):
        """
        本地随机选择图片并分享失败，无usb设备
        :param data:
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.local_edit_elem.click()
        gallery.picture_elem.click()
        gallery.local_export_elem.click()
        text = data[0]
        try:
            toast = gallery.show_toast(text)
            logger.info('错误提示为: {}'.format(toast))
            assert text in toast
            logger.info('导出失败，无usb设备，测试异常导出图片成功')
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.local_no_select_pic_export
    def test_local_no_select_pic_export(self, init_gallery):
        """
        本地不选择图片并分享
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.local_edit_elem.click()

        enabled_bool = gallery.local_export_elem.get_attribute('enabled')
        try:
            assert enabled_bool == 'false'
            logger.info('导出按钮置灰: {}，无法分享'.format(enabled_bool))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.skip(reason='功能实现，但调试时不开放，原因是：删除功能不能随便用')
    @pytest.mark.delete_pic
    def test_delete_pic(self, init_gallery):
        """
        删除图片
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.picture_elem.click()
        gallery.delete_elem.click()

    @pytest.mark.set_wallpaper
    def test_set_wallpaper(self, init_gallery):
        """
        设置图片壁纸
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.picture_elem.click()
        pic_name = gallery.picture_name_elem.text
        gallery.set_wallpaper_elem.click()
        gallery.setting_wallpaper_elem.click()

        set_toast = gallery.show_toast('成功')
        try:
            assert '成功' in set_toast
            logger.info('设置壁纸为 {} 成功'.format(pic_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.wallpaper_cancel
    def test_set_wallpaper_cancel(self, init_gallery):
        """
        设置图片壁纸-取消
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.picture_elem.click()
        gallery.set_wallpaper_elem.click()
        gallery.wallpaper_back_elem.click()
        pic_name = gallery.picture_name_elem.text

        try:
            assert 'jpg' in pic_name
            logger.info('取消设置当前 {} 图片为壁纸成功'.format(pic_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.enlarge_pic
    def test_enlarge_pic(self, init_gallery):
        """
        放大图片并恢复原图大小
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.enlarge_pic()
        pass

    @pytest.mark.parametrize('data', no_usb_data)
    @pytest.mark.export_pic_no_usb
    def test_export_pic_no_usb(self, data, init_gallery):
        """
        导出图片无usb设备时
        :param init_gallery:
        :param data:
        :return:
        """
        gallery = init_gallery[0]
        gallery.picture_elem.click()
        gallery.export_elem.click()

        toast_text = data[0]
        logger.info('测试数据为: {}'.format(toast_text))

        try:
            # 获取导出无usb设备的toast
            no_usb_toast = gallery.show_toast(data[0])
            logger.info('错误提示为: {}'.format(no_usb_toast))
            assert toast_text in no_usb_toast
            logger.info('导出失败，无usb设备，测试异常导出图片成功')
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.click_picture
    def test_click_picture(self, init_gallery):
        """
        随机查看图片
        :param init_gallery:
        :return:
        """
        gallery = init_gallery[0]
        gallery.picture_elem.click()
        sleep(1)

        try:
            pic_name = gallery.picture_name_elem.text
            assert 'jpg' in pic_name
            logger.info('随机查看图片: {} 成功'.format(pic_name))
        except AssertionError as e:
            logger.error('查看图片失败')
            raise e

        gallery.back_elem.click()
        sleep(1)

    @pytest.mark.switch_from
    def test_switch_from(self, init_gallery):
        """
        usb&&本地切换
        :return:
        """
        local_page, use_page = init_gallery

        # 切换前获取本地/usb图库是否被选择属性
        # local_mark = local_page.local_elem.get_attribute('selected')  # true
        local_mark = local_page.get_elem_attribute(local_page.local_elem, 'selected')
        usb_mark = use_page.usb_elem.get_attribute('selected')  # false

        # 切换图库来源
        use_page.usb_elem.click()

        # 切换后获取本地/usb图库是否被选择属性
        new_local_mark = local_page.local_elem.get_attribute('selected')  # false
        new_usb_mark = use_page.usb_elem.get_attribute('selected')  # true

        try:
            assert local_mark == new_usb_mark == 'true'
            assert usb_mark == new_local_mark == 'false'
            logger.info('切换图片来源成功，从 {} -> {}'.format('local', 'usb'))
        except AssertionError as e:
            logger.error('图库来源切换到usb失败')
            raise e


if __name__ == '__main__':
    pytest.main()
