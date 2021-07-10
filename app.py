# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Yan haiming
# CreatDate: 2021/7/10 7:46
# Description: Flask启动脚本

from flask import Flask, make_response, redirect, jsonify, render_template, send_file, request
import settings

app = Flask(__name__)

# 设置配置
app.config.from_object(settings.DEV)



#模拟数据
user = {
    "username": "YHM",
    "bio": "A boy who loves movies and music"
}

STUDENT = [
    {"name": "sls", "year": "1988"},
    {"name": "sht", "year": "1987"},
    {"name": "jxsd", "year": "2011"},
]


@app.route("/")
def index():
    """
    直接响应 HttpResopnse
    :return:
    """
    return "<h1>Hello Flask</h1>"


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    render_template 响应
    :return:
    """
    #
    # print(request)
    # print(request.method)
    # print(request.url)
    # print(request.form)

    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        print("==================")
        print(request.host_url)
        print(request.json)
        print(request.data)
        print(request.values)

        print(request.files)
        tup=request.files.get("JWC")
        print(tup)
        # print(tup.save(tup.filename))

        print("==================")

        # 校验  获取表单提交的数据 post表单提交的数据
        user = request.form.get("username")
        pwd = request.form.get("pwd")

        print(user)
        print(pwd)

        if user == "208191" and pwd == "nbcb,111":
            return render_template("index.html",stu=STUDENT)
        else:
            return render_template("login.html",msg="用户名或密码错误，请重新登录")

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
