# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：get_configs.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/26
# 当前系统时间：10:16
# 用于创建文件的IDE的名称: PyCharm

from configparser import ConfigParser
from config import CONFS_FILE_PATH


class ConfigClass(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.config = ConfigParser()
        self.config.read(self.file_path, encoding='utf-8')

    def get_value(self, sess, opt):
        return self.config.get(sess, opt)

    def get_int(self, sess, opt):
        return self.config.getint(sess, opt)

    def get_float(self, sess, opt):
        return self.config.getfloat(sess, opt)

    def get_eval(self, sess, opt):
        return eval(self.get_value(sess, opt))

    def get_boolean(self, sess, opt):
        return self.config.getboolean(sess, opt)

    @staticmethod
    def write_in_cfg(data, fp):
        configs = ConfigParser()
        for key in data:
            configs[key] = data[key]

        with open(fp, 'w') as f:
            configs.write(f)


config = ConfigClass(CONFS_FILE_PATH)

if __name__ == '__main__':
    pass
    # config = ConfigClass('cfg.cfg')
    # datas = {'excel': {'res': 6}}
    # config.write_in_cfg(datas, 'cfg.cfg')
    # a = config.get_value('excel', 'res_col')
    # print(a)
