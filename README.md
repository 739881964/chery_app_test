# 基于pytest的自动化测试插件

本项目为APP自动化测试模板项目

**将模板项目克隆到本地**

```bash
git clone https://github.com/739881964/chery_app_test.git
```

# 1.相关目录

    ├── configs
    │   ├── test.cfg
    ├── data
    ├── logs
    │   ├── imgs
    │     ├── xxx.png
    │   ├── log.txt
    ├── pages
    │   ├── xxx_page.py
    │   ├── xxx_dir
    │     ├── xxx_page.py
    ├── reports
    │     ├── allure_report
    │           └── xxx.txt
    ├── scripts
    │     └── xxx.py
    ├── tests
    │     ├── test_xxx.py
    │     ├── test_xxx dir
    │           └── test_xxx.py
    ├── Pipfile
    ├── pytest.ini
    └── README.md
    └── main.py
    └── cap.yaml
    └── conftest.py
    └── config.py

configs：log配置信息  
data：存放业务测试用例数据  
logs: 存放错误截图及文本log实时信息记录  
pages: po模式针对每个页面进行元素单独封装  
reports: allure测试报告  
tests: 存放业务测试用例执行文件    
scripts: app设备信息获取、配置、日志等脚本封装  
pytest.ini: pytest配置文件  
cap.yaml: app设备信息存放  
config: 根目录下日志、截图、配置等文件path  
conftest.py: 启动app前/后置脚本  
main.py: 运行该项目所有测试用例py文件  
Pipfile: 默认的Pipfile文件 (多个项目共用)

# 2.环境配置

该项目使用Pipenv进行虚拟环境管理，Pipfile为依赖模块管理文件

## 2.1 在Pycharm内配置虚拟环境 （多个项目使用同一虚拟环境）

在Pycharm内配置虚拟环境的方式有多种，本文只介绍其中较常用的一种

1. 在根目录下执行pipenv命令创建虚拟环境
    ```bash
    pipenv install # 根据根目录下的Pipfile创建一个新环境
    
    pipenv --venv # 查看虚拟环境路径
    
    /Users/用户/.local/share/virtualenvs/pytest-nioauto-RXKZTr3r # 创建的虚拟环境地址
    ```
2. 在Pycharm中指定虚拟环境

   进入设置：File->Settings->Project:->Project Interpreter
   ![](docs/virtua.jpg)

   Existing Interpreter填写虚拟环境下的Python程序所在的路径，如：
    ```bash
    /Users/用户/.local/share/virtualenvs/pytest-nioauto-RXKZTr3r/bin/python3.6
    ```   
   点击OK，环境就已经配置好了    
   ![](docs/pycharm_show.jpg)
3. Pipfile文件配置说明
    ```bash

    [[source]]
    url = "https://github.com/739881964/chery_app_test/tree/master"
    verify_ssl = false name = "pypi"
    
    [packages]
    pytest = "==7.3.1"
    allure-pytest = "==2.13.1"
    selenium = "==4.9.0"
    PyYAML = "==6.0"
    Appium-Python-Client = "==2.8.0"
    pytest-yaml = "==1.2.1"
    
    [requires]
    python_version = "3.10"

    ```

## 2.2 在Pycharm内配置虚拟环境 （多个项目使用不同的虚拟环境）

1. 在根目录下执行pipenv命令创建虚拟环境   
   通过终端进入项目根路径，首先cd pipfiles/dawn 下创建第一个虚拟环境
   ![](docs/pipenv_dawn.jpg)    
   接下来，cd pipfile/remote_vehicle 下创建第二个虚拟环境   
   ![](docs/pipenv_remote.jpg)
2. 在Pycharm中分别配置两个虚拟环境，重复操作两次以下步骤 进入设置：File->Settings->Project:->Project Interpreter
   ![](docs/virtua.jpg)

   Existing Interpreter填写虚拟环境下的Python程序所在的路径，如：
    ```bash
    # 第一次
    /Users/ying.chen.o/.local/share/virtualenvs/dawn-r37wP3lh/bin/python3.6
    
    # 第二次
    /Users/ying.chen.o/.local/share/virtualenvs/remote_vehicle-G8aFyfB9/bin/python3.6
    ```
3. 在Pycharm里选择要使用的虚拟环境
   ![](docs/pipenv_check.jpg)

# 3.如何写测试用例


## 3. data目录下创建测试数据

采用python格式 参考下面的格式：

```python
  # 驾驶模式测试数据用例
drive_data = [
('节能', 'true'),
('舒适', 'true'),
('运动', 'true'),
('雪地', 'true'),
('越野', 'true'),
('个性化', 'true'),
]

```

## 3.2 tests目录下创建测试脚本

- 通过`@pytest.mark.parametrize`读取对应的测试数据文件。

```python
# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：test_drive.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/30
# 当前系统时间：16:30
# 用于创建文件的IDE的名称: PyCharm

import pytest

from data.drive_data import drive_data
from scripts.logger import logger
from time import sleep


class TestDrive:
    """
    测试驾驶功能
    """

    @pytest.mark.parametrize('data', drive_data)
    @pytest.mark.select_drive_1
    def test_select_drive(self, init_drive, data):
        """
        选择不同的驾驶模式
        :return:
        """
        drive_page = init_drive

        mode = data[0]
        pass

```

需要在Pycharm中指定Python Template，模板格式：

```python
# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：drive_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/30
# 当前系统时间：16:26
# 用于创建文件的IDE的名称: PyCharm
```

## 3.3 conftest.py驱动文件

```python
# 获取设备信息cap
def get_device_caps(cap: str):
    """
    获取不同app对应的caps配置信息
    :param cap:
    :return:
    """
    with open(DEVICE_INFO, 'r', encoding='utf8') as f:
        info = yaml.load(f, Loader=yaml.FullLoader)
        # print(caps)

    app_activity = info['appActivity']
    app_package = info['appPackage']

    info['appActivity'] = app_activity[cap]
    info['appPackage'] = app_package[cap]

    return info


def base_driver(app_name='car_settings', url=URL, **kwargs):
    caps = get_device_caps(app_name)
    for k, v in kwargs.items():
        caps[k] = v

    logger.info('启动app参数为: {}'.format(caps))
    driver = Remote(command_executor=url, desired_capabilities=caps)

    return driver


@pytest.fixture(scope='class')
def init_drive():
    """
    初始化驾驶驱动
    :return:
    """
    driver = base_driver()
    logger.info('{} 成功'.format(init_sound.__doc__))
    drive_page = DrivePage(driver)
    yield drive_page
    logger.info('正在关闭驱动')
    driver.quit()
    logger.info('关闭驱动成功！')

```

## 3.4 pages-xxx_page.py页面元素封装

1、定位出页面中的元素，使用(By.xx, locator)的形式当作类变量  
2、针对每个元素定位进行二次封装成属性方法-webelement，方便调用  
3、可以在page添加测试步骤，方便tests下测试用例脚本调用

```python
class DrivePage(BasePage):
    """
    驾驶
    """

    drive_locator = (By.ID, 'com.mega.carsettings:id/menu_drive')

    def drive_list_select_elem(self, value) -> WebElement:
        """
        不同的驾驶模式选择
        :param value:
        :return:
        """
        return self.wait_click_element((By.XPATH, f'//android.widget.RadioButton[contains(@content-desc, "{value}")]'))

    @property
    def drive_elem(self):
        return self.wait_click_element(self.drive_locator)

    def select_drive_mode(self, value):
        """
        选择驾驶模式操作
        :return:
        """
        self.drive_elem.click()
        self.drive_list_select_elem(value)

```

# 4 执行测试用例

1、测试类/方法文件执行  
鼠标右击-run/run pytest

2、命令行在当面项目根目录下执行 pytest

```bash
pytest
pytest -v -s tests/xxx.py
```

3、点击类、方法、main左边的绿色箭头也可执行  
点击class -运行当前类下面所有测试用例  
点击def -运行当前方法下面所有测试用例  
点击main -运行当前文件下面所有测试用例

、、、
![img.png](img.png)
、、、

# 5.断言

直接使用assert 断言，会自动输入日志和测试报告。

```python
class TestDrive:
    """
    测试驾驶功能
    """

    @pytest.mark.parametrize('data', drive_data)
    @pytest.mark.select_drive_1
    def test_select_drive(self, init_drive, data):
        """
        选择不同的驾驶模式
        :return:
        """
        drive_page = init_drive

        mode = data[0]
        logger.info('选择的驾驶模式为: {}'.format(mode))
        drive_page.select_drive_mode(mode)

        sleep(3)

        checked = drive_page.drive_list_select_elem(mode).get_attribute('checked')
        logger.info('选择的驾驶模式bool值是: {}'.format(checked))

        try:
            assert checked == data[-1]
            logger.info('drive mode checked is: {}'.format(checked))
        except AssertionError as e:
            logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main()

```

# 6.测试报告
main.py运行的测试结果存放在reports/allure-report下

切换到测试报告目录下，在命令行模式下执行
```bash
allure serve ./
```