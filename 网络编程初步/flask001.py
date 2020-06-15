from flask import Flask

# 创建Flask对象- Httpd WEB服务对象
app = Flask(__name__)  # __name__可以是任意的小写字母，表示Flask应用对象名称
# 声明web服务的请求资源（指定资源访问的路径）
@app.route('/hello',methods=['GET','POST'])
def hello():
    from flask import request
    # request是请求对象（HttpRequest),包含请求资源的路径、请求方法，请求头，上传的表单数据，文件等信息
    # 获取请求中的查询参数（username,password)
    name = request.args.get('username')
    password = request.args.get('password')
    
    # 返回生成的html网页内容
    if request.method == 'GET':
        return '''
        <h1>用户登录页面</h1>
        <form action="/hello" method="post">
            <input name="name" placeholder="用户名"><br>
            <input name="pwd" placeholder="口令"><br>
            <button>提交</button>
        </form>
        '''
    else:
        # 获取表单参数
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        if name == 'zhao' and pwd == '123':
            return '''
                <h2 style="color:blue;">登录成功</h2>
            '''
        else:
            return '''
                <h2 style="color:red;">登录失败,<a href="/hello">重试</a></h2>
            '''
#启动 flask的web服务器
app.run(host="localhost",port=5000)
