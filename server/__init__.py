from flask import Flask
from flask_cors import CORS

from .utils.config import Config

def create_app():
    config_object = Config()
    app = Flask(__name__)

    # Cross-Origin Config
    CORS(app,
        origins=[config_object.CORS_ALLOW_ORIGIN],
        supports_credentials=config_object.CORS_SUPPORTS_CREDENTIALS)

    # Flask Config
    app.config.from_object(config_object)

    from .routes import main
    app.register_blueprint(main)
    return app
