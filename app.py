from flask import Flask
from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
# DB_NAME = "database.db"
app = Flask(__name__)
app.secret_key = "OGGA"
app.permanent_session_lifetime = timedelta(minutes=5)
# MYSQL DB
#app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#db.init_app(app)


from routes.index import index_bp
from routes.signIn import sign_in_bp
from WIP.wip import wip_bp
from routes.logout import logout_bp
app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(sign_in_bp)
app.register_blueprint(wip_bp)
app.register_blueprint(logout_bp)

if __name__ == "__main__": 
   # db.create_all()
    app.run(host="0.0.0.0", debug=True)