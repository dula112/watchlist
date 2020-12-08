# 创建程序实例
from flask_sqlalchemy import SQLAlchemy   #导入扩展类
import os,sys
from flask import Flask,escape,render_template,request,flash,redirect,url_for
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path)

WIN = sys.platform.startswith('win')
if WIN:   # 如果是windows系统，使用三条斜线
    prefix = 'sqlite:///'
else:    # 否则使用四条斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = prefix +os.path.join(os.path.dirname(app.root_path),os.getenv('DATABASE_FILE','data.db'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False   # 关闭对模型修改的监控
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY','dev')

db = SQLAlchemy(app) # 初始化扩展，传入程序实例app
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户id作为参数
    from models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'

"""
模板上下文处理函数
"""
@app.context_processor
def inject_user():
    from models import User
    user = User.query.first()
    return dict(user=user)  #返回{"user":user}