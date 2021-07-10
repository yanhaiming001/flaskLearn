# flaskLearn
Flask学习点滴

# [fl001 Flask体验]
1.常见的WEB框架
    Django web  大而全，适合大型项目
    Flask web   小而精，很丰富的第三方组件
    tornado web 异步IO非阻塞，原生的websocket
2、response的三种返回方式
    1）HttpResponse
    2) render_template
    3) redirect
    
    jsonfy:返回json
    send_file:上传文件
3、flask中的request请求对象
    request.method 请求方法
    request.form   存储所有FormData中的所有数据
    request.args   存放所有url中的所有数据
    request.json
    request.url     请求地址
    request.host_url    主机地址转换成httpurl
    request.host    主机地址
    request.path
    
    
    request.json 
    request.data     

