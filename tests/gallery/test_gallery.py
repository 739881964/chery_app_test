# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：test_gallery.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/22
# 当前系统时间：17:48
# 用于创建文件的IDE的名称: PyCharm

import pytest


class TestGallery:
    """
    图库功能
    """

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
        except AssertionError as e:
            print('图库来源切换到usb失败')
            raise e


if __name__ == '__main__':
    pytest.main()
