# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Yan haiming
# CreatDate: 2021/7/10 7:50
# Description: flask项目的配置文件

class DEV():
    """
    开发环境
    """
    ENV = "development"
    DEBUG = True


class PRO():
    """
    生产环境
    """
    ENV = "production"
    DEBUG = False
