from flask_wtf import Form
from wtforms import  StringField, DateField, validators, SubmitField, IntegerField


class userForm(Form):

    user_name = StringField('name: ',[validators.DataRequired('Please enter user_name.')])
    user_year = IntegerField('user_year: ',[validators.DataRequired('Please enter user_year.')])
    submit = SubmitField('Submit')