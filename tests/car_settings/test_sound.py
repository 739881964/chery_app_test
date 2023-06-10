# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_sound.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/23
# 当前系统时间：19:10
# 用于创建文件的IDE的名称: PyCharm

import pytest
from pages.car_settings.sound_page import SoundPage
from scripts.logger import logger
from time import sleep


class TestSound:
    """
    测试声音功能
    """

    @pytest.mark.open_media_mute
    def test_open_media_mute(self, init_sound):
        """
        打开媒体静音
        :param init_setting:
        :return:
        """
        sound_page = init_sound

        # sound_page.press_and_move_to(329, 1080, 0, 480)
        sound_page.scroll_to_mute()
        checked = sound_page.media_mute_elem.get_attribute('checked')
        if checked == 'true':
            sound_page.media_mute_elem.click()
            sleep(1)
        sound_page.media_mute_elem.click()

        checked = sound_page.media_mute_elem.get_attribute('checked')
        try:
            assert checked == 'true', '打开媒体静音成功'
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.close_media_mute
    def test_close_media_mute(self, init_sound):
        """
        关闭媒体静音
        :param init_app:
        :return:
        """
        sound_page = init_sound
        sound_page.scroll_to_mute()
        checked = sound_page.media_mute_elem.get_attribute('checked')
        if checked == 'false':
            sound_page.media_mute_elem.click()
            sleep(1)
        sound_page.media_mute_elem.click()

        checked = sound_page.media_mute_elem.get_attribute('checked')
        try:
            assert checked == 'false'
        except AssertionError as e:
            logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main()
