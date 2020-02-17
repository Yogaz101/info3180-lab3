from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired('Name is required!')])
    email = TextField('Email Address', validators=[DataRequired('Email address is required!'), Email('Please enter an appropriate email address.')])
    subject = TextField('Subject', validators=[DataRequired('Subject is required!')])
    message = TextAreaField('Message', validators=[DataRequired('A message is required!')])

    
