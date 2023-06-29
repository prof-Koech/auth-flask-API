from flask import Flask



def create_app(config_name):
    """"create the app with desired environment"""

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])






    return create_app