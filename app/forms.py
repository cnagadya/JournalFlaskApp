from flask_wtf import Form
from wtforms import StringField, BooleanField,TextAreaField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class CreateForm(Form):
	"""Form to create / edit journal article
	"""
	title = StringField('title', validators=[DataRequired()])
	tags = StringField('tags')
	bodytxt = TextAreaField('bodytxt',validators=[DataRequired()])

	# date = d
	