from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)
app.secret_key = "OGGA"
# MYSQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


from routes.index import index_bp
from routes.signIn import sign_in_bp
from WIP.wip import wip_bp
app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(sign_in_bp)
app.register_blueprint(wip_bp)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)