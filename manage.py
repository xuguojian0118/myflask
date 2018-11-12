from flask import Flask,session
#实现状态保持session信息的存储
from flask_session import Session

#导入redis实例
from redis import StrictRedis

app = Flask(__name__)

#设置密钥
app.config['SECRET_KEY'] = '1234'

#使用Flask_session配置的信息
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = StrictRedis
app.config['SESSION_USE_SIGNER'] = True
# redis数据库中session的有效期
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
#Session初始化，和程序实例关联
Session(app)

@app.route('/')
def index():
    # 操作redis数据库。存储session信息
    session['itcast'] = '2018'
    return '你好，世界2018'



if __name__ == '__main__':
	app.run(debug=True)