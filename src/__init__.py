from flask import Flask, redirect, url_for
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

# toolbar = DebugToolbarExtension(app)
# db = SQLAlchemy(app)
# db.create_all()

from mod_tmpl.controllers import mod_tmpl as tmpl_module

app.register_blueprint(tmpl_module)


@app.route('/')
def index():
    return redirect(url_for('tmpl.tmpl'))
