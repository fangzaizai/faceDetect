from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, Length, NumberRange

class SendForm(Form):
	time = IntegerField('send times', validators=[Required(), NumberRange(1,90)])
	submit = SubmitField('Send')