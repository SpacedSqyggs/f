from flask import Flask
from routes.index import index_bp
from routes.signIn import sign_in_bp


app = Flask(__name__)
app.secret_key = "OGGA"

app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(sign_in_bp)


if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)