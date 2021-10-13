from flask import Flask
from turbo_flask import Turbo


turbo = Turbo()

def create_app():
    app = Flask(__name__)

    app.config["SERVER_NAME"] = "127.0.0.1:5000"
    turbo.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
  

    return app