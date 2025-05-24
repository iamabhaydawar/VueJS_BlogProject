from flask import Flask
from flask_login import login_required
from backend.config import LocalDevelopmentConfig
from backend.models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore,auth_required
#for instanciating cacheing
from flask_caching import Cache
from backend.celery.celery_factory import celery_init_app
import flask_excel as excel


def create_app():
    app = Flask(__name__ , template_folder='frontend',static_folder='frontend', static_url_path='/static')
    app.config.from_object(LocalDevelopmentConfig)
    
    
    #model initialization
    db.init_app(app)
    
    #cache initialization
    cache=Cache(app)



    
    #flask_security initialization and setup
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.cache = cache  # Add this line
  
    #  adding a security instance to the app
    app.security = Security(app, datastore=datastore, register_blueprint=False) #register_blueprint=False to disable the default login routes
    app.app_context().push()

    #After pushing app context then we can intiate the api
    from backend.resources import api
    
    #flask-restful init
    api.init_app(app)

    return app

# celery instance is in global space in order to run it separately
app = create_app()
celery_app = celery_init_app(app)

import backend.create_intial_data
import backend.routes

#flask-excel
excel.init_excel(app)


if(__name__ == '__main__'): 
        app.run()
