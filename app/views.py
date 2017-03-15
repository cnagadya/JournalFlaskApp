from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, CreateForm
from .models import User
from datetime import datetime

#load user from db so that user can be used by Flask-Login
@lm.user_loader
def load_user(id):
    return User.query.get(int(id)) #coversion to int bse Flask-login used unicode strs

#check for currrent user & runs before the view for each received request
@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required

def index():
    user = g.user
    articles = []
    return render_template('index.html',
                           title='Home',
                           user=user,
                           articles=articles)

@app.route('/create')
@login_required
def create():
    
    user = g.user
    articles = []
    form = CreateForm()
    if form.validate_on_submit(): 
        g.user.title = form.title.data
        g.user.bodyTxt = form.bodyTxt.data
        g.user.tags = form.tags.data
        g.user.date = datetime.utcnow()
        db.session.add(g.article)
        db.session.commit()
        flash('Your changes have been saved.')   
    return render_template('create.html',
                           title='New Article',
                           user=user,
                           articles=articles,
                           form=form)


#Login view function
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler #informs flask that it is the login view
def login():
    # if g.user is not None and g.user.is_authenticated:
    #     return redirect(url_for('index')) #to load index instead of requested
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
        #trigger authentication through open id
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


#to handle what happens after login
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



