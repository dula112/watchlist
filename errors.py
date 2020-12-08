# 错误处理函数
from wqatchlist import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    # return render_template('404.html',user=user),404 # 返回模板和状态码
    return render_template('404.html'),404 # 返回模板和状态码

