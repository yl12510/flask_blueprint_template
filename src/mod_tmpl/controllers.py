from flask import Blueprint, render_template

mod_tmpl = Blueprint('tmpl', __name__, url_prefix='/tmpl')

@mod_tmpl.route('/')
def tmpl():
    return render_template('tmpl/tmpl.html')
    
