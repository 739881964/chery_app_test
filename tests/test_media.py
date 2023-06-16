# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_media.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/15
# 当前系统时间：15:24
# 用于创建文件的IDE的名称: PyCharm

import pytest
import allure

from appium.webdriver.webelement import WebElement
from scripts.logger import logger
from time import sleep


@allure.feature('畅听功能测试')
class TestMedia:
    """
    畅听功能测试
    """
    @allure.story('拖动正在播放音乐的进度条')
    @pytest.mark.change_progress_seek_bar
    def test_change_progress_seek_bar(self, init_media):
        """
        拖动正在播放音乐的进度条
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        time = media_page.get_time
        media_page.swipe_progress_seek_bar()
        sleep(1)
        current_time = media_page.get_time
        try:
            assert time != current_time
            logger.info('已把正在播放的音乐 <<{}>> 播放时间从 {} 拖动到 {} 成功'.format(name, time, current_time))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.skip(reason='正在开发中')
    @allure.story('返回本地音乐并暂停')
    @pytest.mark.return_local_and_pause
    def test_return_local_and_pause(self, init_media):
        """
        返回本地音乐并暂停
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        sleep(2)
        media_page.play_media_elem.click()
        sleep(2)
        time = media_page.get_time
        sleep(2)
        current_time = media_page.get_time
        try:
            assert time == current_time
            logger.info('正在播放的音乐 <<{}>> 已暂停成功'.format(name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.skip(reason='正在开发中')
    @allure.story('返回本地音乐并切换下一曲')
    @pytest.mark.return_local_and_next
    def test_return_local_and_next(self, init_media):
        """
        返回本地音乐并切换下一曲
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        media_page.next_song_elem.click()
        sleep(1)
        next_name = media_page.get_song_name
        logger.info('broadcast music name is : <<{}>>'.format(next_name))

        try:
            assert name != next_name
            logger.info('把正在播放的音乐 <<{}>> 切换到下一曲 <<{}>> 成功'.format(name, next_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.skip(reason='正在开发中')
    @allure.story('返回本地音乐并切换上一曲')
    @pytest.mark.return_local_and_last
    def test_return_local_and_last(self, init_media):
        """
        返回本地音乐并切换上一曲
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        media_page.next_song_elem.click()
        sleep(1)
        next_name = media_page.get_song_name
        logger.info('broadcast music name is : <<{}>>'.format(next_name))

        try:
            assert name != next_name
            logger.info('把正在播放的音乐 <<{}>> 切换到下一曲 <<{}>> 成功'.format(name, next_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @allure.story('下一曲')
    @pytest.mark.next_song
    def test_switch_next_song(self, init_media):
        """
        下一曲
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        media_page.next_song_elem.click()
        sleep(1)
        next_name = media_page.get_song_name
        logger.info('broadcast music name is : <<{}>>'.format(next_name))

        try:
            assert name != next_name
            logger.info('把正在播放的音乐 <<{}>> 切换到下一曲 <<{}>> 成功'.format(name, next_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @allure.story('上一曲')
    @pytest.mark.last_song
    def test_switch_last_song(self, init_media):
        """
        上一曲
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        media_page.last_song_elem.click()
        sleep(1)
        last_name = media_page.get_song_name
        logger.info('broadcast music name is : <<{}>>'.format(last_name))

        try:
            assert name != last_name
            logger.info('把正在播放的音乐 <<{}>> 切换到上一曲 <<{}>> 成功'.format(name, last_name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @allure.story('暂停正在播放的音乐')
    @pytest.mark.pause_music
    def test_pause_music(self, init_media):
        """
        暂停正在播放的音乐
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music = media_page.random_song_elem
        name = media_page.get_song_name
        music.click()
        logger.info('broadcast music name is : <<{}>>'.format(name))
        sleep(2)
        media_page.play_media_elem.click()
        sleep(2)
        time = media_page.get_time
        sleep(2)
        current_time = media_page.get_time
        try:
            assert time == current_time
            logger.info('正在播放的音乐 <<{}>> 已暂停成功'.format(name))
        except AssertionError as e:
            logger.error(e)
            raise e

    @allure.story('播放本地音乐')
    @pytest.mark.test_local_music_broadcast
    def test_broadcast_local_music(self, init_media):
        """
        播放本地音乐
        :param init_media:
        :return:
        """
        media_page = init_media
        media_page.media_login_elem.click()
        media_page.local_music_elem.click()
        music_elem = media_page.random_song_elem
        music_name = music_elem.text
        logger.info('music name is : <<{}>>'.format(music_name))
        music_elem.click()

        name = media_page.get_song_name
        time = media_page.get_time
        sleep(1)
        current_time = media_page.get_time
        logger.info('broadcasting music name is : <<{}>>'.format(name))
        # logger.info('broadcasting music time is from "{}" to "{}"'.format(time, current_time))
        try:
            # assert isinstance(media_page.broadcasting_icon_elem, WebElement)
            assert music_name == name
            assert time != current_time
            logger.info('随机选择的音乐：<<{}>> == 正在播放的音乐: <<{}>>'.format(music_name, name))
            logger.info('broadcasting music time is from "{}" to "{}"'.format(time, current_time))
        except AssertionError as e:
            logger.error(e)
            raise e
