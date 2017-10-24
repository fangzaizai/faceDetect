from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, Length

class SendForm(Form):
	time = IntegerField('send times', validators=[Required(), Length(1,32)])
	submit = SubmitField('Send')