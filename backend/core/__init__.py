from flask import Flask
# from flask_dapr.actor import DaprActor
# from demo_actor import DemoActor

from app.dashboard.views import dashboard_blueprint


def create_app():
    app = Flask(__name__)
    
    # register new blueprint
    app.register_blueprint(dashboard_blueprint)
    
    return app
    
    