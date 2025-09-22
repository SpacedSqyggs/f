from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from .index import *
sign_in_bp = Blueprint("signIn",__name__)



# 5 different Fields essentially 6 different types of inputs 
# 1. StringField = textbox where characters are not hidden
# 2. PasswordField = password box where characters are hidden 
# 3. IntegerField = Field for whole numbers
# 4. FloatField = field for decimal numbers
# 5. BooleanField = Checkbox 
# 6. SubmitField = Submit button

#wtforms.validators, imports Data required which is a validator that makes a field required to have data in 

#Creating Login Form from Flask_WTF using FlaskForm
class LoginForm(FlaskForm): 
#username field
    username = StringField('Username', validators=[DataRequired()])
#password field
    password = PasswordField('Password', validators=[DataRequired()])
#remember me field
    remember_me = BooleanField('Remember me')
#Sign in button 
    submit = SubmitField('Sign in')


@sign_in_bp.route('/sign-in', methods=['GET', 'POST'])
def sign_in(): 
#creating variable form to be linked to creation of class LoginForm
    form = LoginForm()
    if form.validate_on_submit(): 
        user = form.username.data
        return render_template('base.html',title="Signed in", user=f"{user}")
    else: 
        return render_template('sign_in.html', title='Sign in', form=form)
    