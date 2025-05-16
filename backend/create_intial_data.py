from flask import current_app as app
from backend.models import db, User, Role, UserRoles
from flask_security import Security, SQLAlchemyUserDatastore, hash_password

with app.app_context():
    # Create the database tables
    db.create_all()
        
    userdatastore: SQLAlchemyUserDatastore = app.security.datastore
    
    userdatastore.find_or_create_role(name='admin', description='superuser')
    userdatastore.find_or_create_role(name='user', description='general user')
   
    if not userdatastore.find_user(email='admin@study.iitm.ac.in'):
        userdatastore.create_user(
            username='admin',
            email='admin@study.iitm.ac.in',
            password=hash_password('pass'),
            roles=['admin']
        )
    if not userdatastore.find_user(email='user01@study.iitm.ac.in'):
        userdatastore.create_user(
            username='user',
            email='user01@study.iitm.ac.in',
            password=hash_password('pass'),
            roles=['user']
        )  # for testing purpose
    
    db.session.commit()