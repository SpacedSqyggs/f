from flask import Blueprint, render_template, session, redirect, url_for
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
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
# email field 
    email = StringField('Email')
#remember me field
    remember_me = BooleanField('Remember me')
#Sign in button 
    submit = SubmitField('Sign in')


@sign_in_bp.route('/sign-in', methods=['GET', 'POST'])
def sign_in(): 
    if 'user' in session:
        session.permanent = True
        return redirect(url_for("signIn.user_info"))
#creating variable form to be linked to creation of class LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        user_data = {
        'username': form.username.data,
        'password' : form.password.data,
        'email' : form.email.data
        }
        session['user'] = user_data
        return redirect(url_for("signIn.user_info"))
        #return f"<p>username={username}, password={password}, email={email}</p>"
        #return render_template('base.html',title="Signed in")
   
    return render_template('sign_in.html', title='Sign in', form=form)


@sign_in_bp.route('/user-info')
def user_info(): 
    if  "user" in session: 
        user_data = session['user']
        return f"<h1>Username:{user_data.get('username')}</h1><p>password:{user_data.get('password')}</p><p>email:{user_data.get('email')}</p>"
    else: 
        return redirect(url_for("signIn.sign_in"))
    