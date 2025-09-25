from flask import Blueprint, render_template, session, redirect
from models import *

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
create_user_bp = Blueprint("create_user",__name__)

class CreateUserForm(FlaskForm): 
    email = StringField(
        'Email', 
        validators=[DataRequired(), Length(max=20)])
    username = StringField('Username', 
                validators=[DataRequired(), Length(max=20)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(max=30),
                            EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')


@create_user_bp.route('/create-user')
def create_user(): 
    form = CreateUserForm()
    if form.validate_on_submit():
        user_info = { 
            'email' : form.email.data, 
            'username': form.username.data, 
            'password': form.password.data
        }
        if user_info.get('email') != '' and user_info.get('username') != '' and user_info.get('password') != '': 
            user = User(email=user_info.get('email'),username=user_info.get('username'),password=user_info.get('password'))
            db.session.add(user)
            db.session.commit()
            return redirect('/')