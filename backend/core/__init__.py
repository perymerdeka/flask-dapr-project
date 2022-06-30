from flask import Flask
from flask_dapr.actor import DaprActor
from demo_actor import DemoActor


def create_app():
    app = Flask(f'{DemoActor.__name__}Service')
    actor = DaprActor(app)
    actor.register_actor(DemoActor)
    
    return app
    
    