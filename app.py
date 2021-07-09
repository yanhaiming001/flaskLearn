# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Yan haiming
# CreatDate: 2021/7/10 7:46
# Description: Flask启动脚本

from flask import Flask, make_response, redirect, jsonify, render_template
import settings

app = Flask(__name__)

# 设置配置
app.config.from_object(settings.DEV)


@app.route("/")
def index():
    return "<h1>Hello Flask</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
