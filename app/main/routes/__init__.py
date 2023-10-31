# import resprctive blueprints and flask REstful resources
from .blueprint_test import bp
from .worker_routes import worker
from .user_routes import user
from .booking_routes import booking


def add_resources(app):
    """
    Method to add resources to app context
    
    Args:
        app (object): object of Flask representing the app in context
    """
    pass

def register_blueprints(app):
    """
    Method to add blueprints to app context
    
    Args:
        app (object): object of Flask representing the app in context
    """
    app.register_blueprint(bp)
    app.register_blueprint(worker)
    app.register_blueprint(user)
    app.register_blueprint(booking)
    
