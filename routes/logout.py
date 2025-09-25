from flask import Blueprint, session, url_for, redirect
from .signIn import *
from .index import index
logout_bp = Blueprint("Logout", __name__) 

@logout_bp.route('/logout')
def logout(): 
    session.pop('user',None)
    return redirect(url_for("index.index"))