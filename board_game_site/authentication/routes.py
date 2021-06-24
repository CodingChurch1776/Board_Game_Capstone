from flask import Blueprint, render_template, request, redirect, flash, url_for
from board_game_site.forms import UserLoginForm
from board_game_site.models import User, db, check_password_hash



from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            username = form.username.data
            print(email,password, username)

            user = User(email, password = password, username = username)
            db.session.add(user)
            db.session.commit()

            flash(f'Welcome to MeeplePeople {email}', 'user-created')

            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid form Data: Please check your form')
            

    return render_template('signup.html', form = form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    try:
        if request.method =='POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            username = form.username.data
            print(email, password, username)

            logged_user = User.query.filter(User.email == email).first()
            named_user = User.query.filter(User.username == username).first()

            if logged_user and named_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successful logged in: Via Email/Password/Username', 'auth-success')
                return redirect(url_for('site.home'))
            else:
                flash('Your Email/Password is incorrect', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid form Data: Please check your form')

    return render_template('signin.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))