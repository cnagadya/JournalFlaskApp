from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, CreateForm, EditForm
from .models import User, Article
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
    articles = user.articles
    return render_template('index.html',
                           title='Home',
                           user=user,
                           articles=articles)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    user = g.user
    articles = []
    form = CreateForm()

    if request.method == "POST":
        title = request.form['title']
        bodytxt = request.form['bodytxt']
        tags = request.form['tags']

        article = Article(title=form.title.data,
                          bodytxt=form.bodytxt.data,
                          tags = form.tags.data,
                          date = datetime.now(), 
                          user_id = g.user.id) 

        
        db.session.add(article)
        db.session.commit()
        flash('You have successfully added a new article.')  
    
      
    return render_template('create.html', action="Add",
                           title='New Article',
                           user=user,
                           articles=articles,
                           form=form)


@app.route('/edit/', methods=['GET', 'POST'])
@login_required
def edit():
    user = g.user
    #articles =[]
    form = EditForm()
    article = db.session.query(Article).filter(Article.id==id).first()
    if request.method == "POST":
        title = request.form['title']
        bodytxt = request.form['bodytxt']
        tags = request.form['tags']

        article = Article(title=form.title.data,
                          bodytxt=form.bodytxt.data,
                          tags = form.tags.data,
                          #date = datetime.now(), 
                          user_id = g.user.id) 

        
        db.session.commit()
        flash('Changes have successfully been made.')  
    
      
    return render_template('edit.html', action="edit",
                           id=id,
                           title='Edit Article',
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

@app.route('/ https://login.yahoo.com/config/login?logout=1')
def logout():
    logout_user()
    return redirect(url_for('index'))



