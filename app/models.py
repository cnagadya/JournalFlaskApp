from app import db

class User(db.Model):
	"""class for the user table"""
	
	id = db.Column(db.Integer, primary_key=True )
	username = db.Column(db.String, index=True, unique=True)
	email = db.Column(db.String, index=True, unique=True)
	articles =  db.relationship('Article', backref='user',lazy='dynamic')



class Article(db.Model):
	"""Table for the journey articles"""
	
	id = db.Column(db.Integer, primary_key=True )
	title = db.Column(db.String, index=True, unique=True)
	tags = db.Column(db.String, index=True, unique=True)
	bodyTxt = db.Column(db.String, index=True, unique=True)
	date = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Article %r' % (self.bodyTxt)