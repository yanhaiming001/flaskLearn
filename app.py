# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Yan haiming
# CreatDate: 2021/7/10 7:46
# Description: Flask启动脚本

from flask import Flask, make_response, redirect, jsonify, render_template, send_file
import settings

app = Flask(__name__)

# 设置配置
app.config.from_object(settings.DEV)


@app.route("/")
def index():
    """
    直接响应 HttpResopnse
    :return:
    """
    return "<h1>Hello Flask</h1>"


@app.route("/login")
def login():
    """
    render_template 响应
    :return:
    """
    return render_template("login.html")


@app.route("/lg")
def lg():
    """
    redirect重定向响应
    :return:
    """
    return redirect("/login")


@app.route("/json")
def r_json():
    """
    返回json字符串  返回的是application/jsonfy
    :return:
    """
    return jsonify({"name": "yhm", "age": 28})


@app.route("/file")
def res_json():
    """
    传输文件
    :return:返回文件  向前端响应文件，可以是图片、视频、音频等等
    """
    return send_file("./static/street.jpg")


if __name__ == "__main__":
    # 启动服务
    app.run(host="0.0.0.0", port=8088)
