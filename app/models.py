from app import db

class User(db.Model):
	"""class for the user table"""
	id = db.Column(db.Integer, primary_key=True )
	nickname = db.Column(db.String, index=True, unique=True)
	email = db.Column(db.String, index=True, unique=True)
	articles =  db.relationship('Article', backref='user',lazy='dynamic')

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id) 
		except NameError:
			return str(self.id)  

	def __repr__(self):
		return '<User %r' % (self.nickname)


class Article(db.Model):
	"""Table for the journey articles"""
	 # __searchable__ = ['tags','bodytxt','title'] #to use later for the search
	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True )
	title = db.Column(db.String, index=True, unique=True)
	tags = db.Column(db.String, index=True, unique=True)
	bodytxt = db.Column(db.String, index=True, unique=True)
	date = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Article %r' % (self.bodyTxt)