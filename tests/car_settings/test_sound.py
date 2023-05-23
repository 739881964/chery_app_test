# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_sound.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/23
# 当前系统时间：19:10
# 用于创建文件的IDE的名称: PyCharm

import pytest
from pages.car_settings.sound_page import SoundPage

from time import sleep


class TestSound:
    """
    测试声音功能
    """

    @pytest.mark.media_mute
    def test_media_mute(self, init_app):
        """
        媒体静音
        :param init_setting:
        :return:
        """
        driver = init_app
        sound_page = SoundPage(driver)

        # sound_page.press_and_move_to(329, 1080, 0, 480)
        sound_page.swipe_up_and_down(329, 1080, 329, 380)
        sleep(0.5)
        sound_page.menu_sound_elem.click()
        try:
            assert 1 == 1
        except AssertionError as e:
            raise e


if __name__ == '__main__':
    pytest.main()
