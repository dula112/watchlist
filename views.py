# 视图函数
from watchlist import app,db
from flask import request,render_template,redirect,flash,url_for
from models import Movie,User
from flask_login import current_user,login_required,logout_user,login_user


@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        title = request.form.get("title")
        year = request.form.get("year")
        if not title or not year or len(year)>4 or len(title) >60:
            flash("Invalid input.")
            return redirect(url_for("index"))
        movie = Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        flash("添加成功！")
        return redirect(url_for('index'))
    # user = User.query.first()  #读取第一个用户记录
    movies = Movie.query.all()  #读取所有电影记录
    # return render_template('index.html',user=user,movies=movies)
    return render_template('index.html',movies=movies)

@app.route('/movie/edit/<int:movie_id>',methods=["POST","GET"])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == "POST":
        title = request.form["title"]
        year = request.form["year"]
        if not title or not year or len(year) >4 or len(title) >60:
            flash("Invalid input.")
            return redirect(url_for("index"))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for("index"))
    return render_template("edit.html",movie=movie)

@app.route('/movie/delete/<int:movie_id>',methods=["POST"])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("删除成功.")
    return redirect(url_for("index"))




@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            flash("Invalid Input.")
            return redirect(url_for('login'))

        user = User.query.first()
        if username == user.username and user.valid_password(password):
            login_user(user)
            flash("Login success.")
            return redirect(url_for('index'))
        flash("Invalid username or password.")
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Goodbye.")
    return redirect(url_for('index'))

@app.route('/settings',methods=["GET","POST"])
def settings():
    if request.method == "POST":
        name = request.form["name"]

        if not name or len(name)>20:
            flash("Invalid Input.")
            return redirect(url_for('settings'))
        current_user.name = name
        db.session.commit()
        flash("Settings updated.")
        return redirect(url_for('index'))

    return render_template('settings.html')