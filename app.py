from flask import Flask,escape,render_template,request,flash,redirect,url_for

import sys
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user

if __name__ == '__main__':
    app.run(debug=True)
