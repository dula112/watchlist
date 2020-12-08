# 模型类
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from watchlist import app,db

class User(db.Model, UserMixin):  # 表名为user(自动生成小写) 继承UserMixin,判断认证状态
    id = db.Column(db.INTEGER,primary_key=True)  # 主键
    name = db.Column(db.String(20)) #姓名
    username = db.Column(db.String(20))
    # password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))  #密码散列值

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def valid_password(self,password):
        return check_password_hash(self.password_hash,password)

class Movie(db.Model): #表名为movie
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份