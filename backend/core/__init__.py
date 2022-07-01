from flask import Flask
from flask_dapr.actor import DaprActor
from .demo_actor.demo_actor import DemoActor

from app.dashboard.views import dashboard_blueprint


def create_app():
    app = Flask(f'{DemoActor.__name__}Service')
    actor = DaprActor(app)
    actor.register_actor(DemoActor)
        
    # register new blueprint
    app.register_blueprint(dashboard_blueprint)
    
    return app
    
    