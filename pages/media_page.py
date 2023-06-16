# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：media_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/15
# 当前系统时间：15:21
# 用于创建文件的IDE的名称: PyCharm

from pages.base_page import BasePage, Element
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from scripts.logger import logger


class MediaPage(BasePage, Element):
    """
    畅听
    """
    # locators
    media_login_locator = (By.ID, 'com.lion.media:id/logoLl')
    local_music_locator = (By.ID, 'com.lion.media:id/musicLocalTv')
    random_song_locator = (By.ID, 'com.lion.media:id/nameTv')
    broadcasting_name_locator = (By.ID, 'com.lion.media:id/nameTv')
    broadcasting_icon_locator = (By.ID, 'com.lion.media:id/playAnimView')
    current_time_locator = (By.ID, 'com.lion.media:id/currentTimeTv')
    play_media_locator = (By.ID, 'com.lion.media:id/playIv')
    next_song_locator = (By.ID, 'com.lion.media:id/nextIv')
    last_song_locator = (By.ID, 'com.lion.media:id/preIv')
    play_mode_locator = (By.ID, 'com.lion.media:id/playModelIv')

    # elements
    media_login_elem = Element(locator=media_login_locator, method='click', desc='音源切换')
    local_music_elem = Element(local_music_locator, 'click', '本地音乐')
    broadcasting_name_elem = Element(broadcasting_name_locator, 'presence', '正在播放的音乐名称', is_elems=True, one_elem=True,
                                     index=2, one_from_elems=True)
    # random_song_elem = Element(random_song_locator, 'click', '音乐图标')
    broadcasting_icon_elem = Element(broadcasting_icon_locator, 'presence', '正在播放音乐图标')
    current_time_elem = Element(current_time_locator, 'presence', '当前已播放的时间')
    play_media_elem = Element(play_media_locator, 'click', '播放按钮')
    next_song_elem = Element(next_song_locator, 'click', '下一曲')
    last_song_elem = Element(last_song_locator, 'click', '上一曲')
    play_mode_elem = Element(play_mode_locator, 'click', '循环模式')

    @property
    def get_song_name(self):
        """
        获取正在播放的歌曲名称
        :return:
        """
        return self.broadcasting_name_elem.text

    def swipe_progress_seek_bar(self, x=330, y=1170, high=990):
        """
        滑动正在播放的歌曲进度条
        :return:
        """
        _x = self.generate_random(x=x, y=y)
        self.swipe_up_and_down(x, high, _x, high)
        logger.info('向x轴滑动距离{}, 滑动正在播放的歌曲进度条成功'.format(x))

    @property
    def get_time(self):
        """
        获取已播放的时间
        :return:
        """
        return self.current_time_elem.text

    @property
    def random_song_elem(self):
        """
        随机选择一首音乐
        :return:
        """
        try:
            music = self.find_elements(self.random_song_locator)
            if music:
                return self.wait_click_element(music[self.generate_random(3, len(music) - 1)])
        except (NoSuchElementException, TimeoutException) as e:
            logger.error(e)
            raise e

    # @property
    def broadcasting_music_name_elem(self):
        """
        正在播放的音乐名称
        :return:
        """
        ...
