# !/usr/bin/python
# -*- coding: utf-8 -*-
# file_name: main.py
# time: 2023/5/26 2:20 下午
# author: xiang.yu
# create_by: PyCharm

import pytest
import shutil
import os
import logging

from config import IMG_PATH


def remove_dir(a_list: list = 'file_dir'):
    """remove all files what you input"""
    for _ in a_list:
        if os.path.exists(_):
            all_files = os.listdir(_)
            if all_files:
                for file in all_files:
                    path = os.path.join(_, file)
                    if os.path.isfile(path):
                        os.remove(path)
                        logging.warning('正在删除缓存文件：%s', path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                        logging.warning('正在删除缓存目录：%s', path)


if __name__ == '__main__':
    cache_dir = '.pytest_cache'
    allure_reports = 'reports/allure-report'
    remove_dir([cache_dir, allure_reports, IMG_PATH])

    # run test
    pytest.main([  # './tests/car_settings/test_show.py::TestShow::test_clear_screen',
        '-vs',
        f'--alluredir={allure_reports}',
    ])
