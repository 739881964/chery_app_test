# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：calendar_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/8
# 当前系统时间：10:08
# 用于创建文件的IDE的名称: PyCharm


from pages.base_page import BasePage, Element
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.webelement import WebElement


class CalendarPage(BasePage, Element):
    """
    日历
    """
    # locators
    add_plan_locator = (By.ID, 'com.mega.redwoodcalendar:id/add')
    save_plan_locator = (By.ID, 'com.mega.redwoodcalendar:id/save')
    back_edit_locator = (By.ID, 'com.mega.redwoodcalendar:id/back')
    continue_edit_locator = (By.ID, 'com.mega.redwoodcalendar:id/left_bt')
    confirm_exit_locator = (By.ID, 'com.mega.redwoodcalendar:id/right_bt')
    title_input_locator = (By.ID, 'com.mega.redwoodcalendar:id/title')
    address_input_locator = (By.ID, 'com.mega.redwoodcalendar:id/add_location')
    all_day_mark_locator = (By.ID, 'com.mega.redwoodcalendar:id/day_switch')
    input_second_locator = (By.ID, 'com.mega.redwoodcalendar:id/edit_input')
    save_second_locator = (By.ID, 'com.mega.redwoodcalendar:id/input_save')
    delete_second_locator = (By.ID, 'com.mega.redwoodcalendar:id/delete')
    left_title_locator = (By.ID, 'com.mega.redwoodcalendar:id/left_title')
    days_reminders_locator = (By.ID, 'com.mega.redwoodcalendar:id/reminders')
    itinerary_locator = (By.ID, 'com.mega.redwoodcalendar:id/itinerary')
    select_drop_down_locator = (By.ID, 'com.mega.redwoodcalendar:id/drop_down')
    importance_locator = (By.ID, 'com.mega.redwoodcalendar:id/important')

    # elements
    add_plan_elem = Element(locator=add_plan_locator, method='click', desc='新增日程')
    save_plan_elem = Element(locator=save_plan_locator, method='click', desc='保存')
    back_edit_elem = Element(locator=back_edit_locator, method='click', desc='退出编辑')
    continue_edit_elem = Element(locator=continue_edit_locator, method='click', desc='继续编辑')
    confirm_exit_elem = Element(locator=confirm_exit_locator, method='click', desc='确认退出')
    title_input_elem = Element(locator=title_input_locator, method='presence', desc='标题输入框')
    address_input_elem = Element(locator=address_input_locator, method='presence', desc='地址输入框')
    all_day_mark_elem = Element(locator=all_day_mark_locator, method='click', desc='全天切换按钮')
    input_second_elem = Element(locator=input_second_locator, method='presence', desc='二次输入')
    save_second_elem = Element(locator=save_second_locator, method='click', desc='二次保存')
    delete_second_elem = Element(locator=delete_second_locator, method='click', desc='删除输入框内容')
    left_title_elem = Element(locator=left_title_locator, method='presence', desc='新增日程列表title', is_elems=True,
                              one_elem=True,
                              one_from_elems=True,
                              index=-1)
    days_reminders_elem = Element(locator=days_reminders_locator, method='presence', desc='重要节日提醒')
    itinerary_elem = Element(locator=itinerary_locator, method='presence', desc='行程主动提醒')
    select_drop_down_elem = Element(locator=select_drop_down_locator, method='click', desc='提醒开关下拉选择')
    importance_elem = Element(locator=importance_locator, method='presence', desc='重要节日内容展示')

    @property
    def reminders_button_property(self):
        """
        获取重要节日提醒开关属性
        :return:
        """
        return self.days_reminders_elem.get_attribute('checked')

    @property
    def itinerary_button_property(self):
        """
        获取行程主动提醒开关属性
        :return:
        """
        return self.itinerary_elem.get_attribute('checked')

    def add_title(self, title):
        """
        新增日程标题
        :return:
        """
        self.title_input_elem.click()
        self.input_second_elem.send_keys(title)
        self.save_second_elem.click()

    def add_location(self, location):
        """
        新增日程位置
        :param location:
        :return:
        """
        self.address_input_elem.click()
        self.input_second_elem.send_keys(location)
        self.save_second_elem.click()

    def add_new_plan(self, title, location):
        """
        新增日程步骤,输入标题，地址
        :param title:
        :param location:
        :return:
        """
        self.add_title(title)
        self.add_location(location)
