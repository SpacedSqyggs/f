from flask import Blueprint, render_template

wip_bp = Blueprint('wip', __name__, template_folder="templates")

@wip_bp.route('/wip-home')
def wip_home(): 
    return render_template('wipbase.html')