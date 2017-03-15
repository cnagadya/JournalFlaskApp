import os
basedir = os.path.abspath(os.path.dirname(__file__))

# activation of cross-site request forgery prevention 
CSRF_ENABLED = True
SECRET_KEY = 'my-big-secreT-!' #creates a cryptographic token

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #creating sqlite db
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
