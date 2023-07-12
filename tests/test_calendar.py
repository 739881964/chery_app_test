# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_calendar.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/8
# 当前系统时间：12:20
# 用于创建文件的IDE的名称: PyCharm

import allure
import pytest

from time import sleep
from data.calendar_data import title_exit_data, no_title_data
from scripts.logger import logger


@allure.feature('日历app测试')
class TestCalendar:
    """
    日历
    """

    @pytest.mark.run(order=6)
    @allure.feature('关闭重要节日提醒')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.close_reminders
    def test_close_reminders(self, init_calendar):
        """
        关闭重要节日提醒
        :param init_calendar:
        :return:
        """
        calendar_page = init_calendar
        if not calendar_page.element_is_exist('dropdown'):
            calendar_page.select_drop_down_elem.click()

        type1 = calendar_page.reminders_button_property
        if type1 == 'false':
            calendar_page.days_reminders_elem.click()
        calendar_page.days_reminders_elem.click()

        type2 = calendar_page.reminders_button_property
        try:
            assert type2 == 'false'
            assert calendar_page.element_is_exist('important_layout') is False
            logger.info('关闭重要节日提醒成功')
        except AssertionError as e:
            logger.error(e)
            raise e
        finally:
            calendar_page.select_drop_down_elem.click()

    @pytest.mark.run(order=5)
    @allure.feature('打开重要节日提醒')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.open_reminders
    def test_open_reminders(self, init_calendar):
        """
        打开重要节日提醒
        :param init_calendar:
        :return:
        """
        calendar_page = init_calendar
        if not calendar_page.element_is_exist('dropdown'):
            calendar_page.select_drop_down_elem.click()

        type1 = calendar_page.reminders_button_property
        # print(type1)
        if type1 == 'true':
            calendar_page.days_reminders_elem.click()
        calendar_page.days_reminders_elem.click()

        type2 = calendar_page.reminders_button_property
        try:
            assert type2 == 'true'
            assert calendar_page.element_is_exist('important_layout') is True
            logger.info('打开重要节日提醒成功')
        except AssertionError as e:
            logger.error(e)
            raise e
        finally:
            calendar_page.select_drop_down_elem.click()

    @pytest.mark.run(order=4)
    @allure.feature('打开行程主动提醒')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.open_itinerary
    def test_open_itinerary(self, init_calendar):
        """
        打开行程主动提醒
        :param init_calendar:
        :return:
        """
        calendar_page = init_calendar
        if not calendar_page.element_is_exist('dropdown'):
            calendar_page.select_drop_down_elem.click()

        type1 = calendar_page.itinerary_button_property
        if type1 == 'true':
            calendar_page.itinerary_elem.click()
        calendar_page.itinerary_elem.click()

        type2 = calendar_page.itinerary_button_property
        try:
            assert type2 == 'true'
            assert calendar_page.element_is_exist('schedule_layout') is True
            logger.info('打开行程主动提醒成功')
        except AssertionError as e:
            logger.error(e)
            raise e
        finally:
            calendar_page.select_drop_down_elem.click()

    @pytest.mark.run(order=3)
    @allure.feature('关闭行程主动提醒')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.close_itinerary
    def test_close_itinerary(self, init_calendar):
        """
        关闭行程主动提醒
        :param init_calendar:
        :return:
        """
        calendar_page = init_calendar
        if not calendar_page.element_is_exist('dropdown'):
            calendar_page.select_drop_down_elem.click()

        type1 = calendar_page.itinerary_button_property
        if not type1 == 'true':
            calendar_page.itinerary_elem.click()
        calendar_page.itinerary_elem.click()

        type2 = calendar_page.itinerary_button_property
        try:
            assert type2 == 'false'
            assert calendar_page.element_is_exist('schedule_layout') is False
            logger.info('关闭行程主动提醒成功')
        except AssertionError as e:
            logger.error(e)
            raise e
        finally:
            calendar_page.select_drop_down_elem.click()

    @pytest.mark.run(order=2)
    @allure.feature('新增日程-非全天提醒')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('data', title_exit_data)
    @pytest.mark.add_plan
    def test_add_new_plan(self, init_calendar, data):
        """
        新增日程-非全天提醒
        :return:
        """
        title, location = data[0], data[-1]
        calendar_page = init_calendar
        calendar_page.add_plan_elem.click()
        if title and location:
            calendar_page.add_new_plan(title, location)
        else:
            if title and not location:
                calendar_page.add_title(title)
            elif location and not title:
                calendar_page.add_location(location)
        calendar_page.save_plan_elem.click()

        add_text = calendar_page.left_title_elem.text
        try:
            assert add_text == data[0]
            logger.info('新增日程 {} 成功'.format(add_text))
        except AssertionError as e:
            logger.error(e)
            raise e

    @pytest.mark.run(order=1)
    @allure.feature('新增日程-全天提醒')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.add_all_day_reminder
    def test_add_all_day_reminder(self, init_calendar):
        """
        新增日程-全天提醒
        :param init_calendar:
        :return:
        """
        data = title_exit_data[0]
        title, location = data[0], data[1]
        calendar_page = init_calendar
        calendar_page.add_plan_elem.click()
        calendar_page.add_new_plan(title, location)
        calendar_page.all_day_mark_elem.click()
        reminder_time_pro = calendar_page.reminder_time
        calendar_page.save_plan_elem.click()
        add_text = calendar_page.left_title_elem.text
        try:
            assert add_text == data[0]
            assert reminder_time_pro == 'false'
            logger.info('新增日程 {} 成功'.format(add_text))
            logger.info('新增日程：<<{}>> 的醒时间为全天提醒成功'.format(add_text))
        except AssertionError as e:
            logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main()
