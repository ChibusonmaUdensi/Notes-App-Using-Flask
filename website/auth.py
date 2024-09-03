from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
# from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__ )
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    if request.method == 'POST':
        email = request.form.get('email')
        password= request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            
        # if check_password_hash(user.password, password):
           flash('Login successful!', category='success')
           login_user(user, remember=True)
           return redirect(url_for('views.home'))
        else:
            flash('Incorrect password', category='error')

    return render_template("login.html", text="testing", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',  methods=['GET', 'POST'])
def signUp():
    if request.method=='POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category='error')
        elif len(email) < 4: 
            flash("Email must be greater than 4 characters", category='error')
        elif len(first_name) < 2:
            flash("First name must be greater than 2 characters", category='error')
        elif password!= password2:
            flash("Passwords do not match", category='error')
        elif len(password) < 7:
            flash("Password must be at least 7 characters", category='error')
        else:
        #    new_user= User(email=email, password=generate_password_hash(password, method='pbkdf2:sha256'), first_name=first_name)
             hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
             new_user = User(first_name=first_name, email=email, password_hash=hashed_password)
      
             db.session.add(new_user)
             db.session.commit()
             flash("Account created", category="success")
             return redirect(url_for("views.home"))
    return render_template("sign_up.html", user=current_user)
