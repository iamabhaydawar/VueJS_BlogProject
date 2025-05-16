from flask import Flask
from backend.config import LocalDevelopmentConfig
from backend.models import db, User, Role, UserRoles
from flask_security import Security, SQLAlchemyUserDatastore,auth_required
from backend.resources import api

def create_app():
    app = Flask(__name__ , template_folder='frontend',static_folder='frontend', static_url_path='/static')
    app.config.from_object(LocalDevelopmentConfig)
    
    
    #model initialization
    db.init_app(app)
    
    #flask-restful init
    api.init_app(app)
    
    #flask_security initialization and setup
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    #  adding a security instance to the app
    app.security = Security(app, datastore=datastore, register_blueprint=False) #register_blueprint=False to disable the default login routes
    app.app_context().push()

    return app  
   
app = create_app()
import backend.create_intial_data
import backend.routes

if(__name__ == '__main__'): 
        app.run()
