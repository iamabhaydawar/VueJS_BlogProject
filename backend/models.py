from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    # flask_security specific fields
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return f'<User {self.username}>'
    
    
class Role(db.Model,RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'
    
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    # user = db.relationship('User', backref=db.backref('user_roles', lazy=True))
    # role = db.relationship('Role', backref=db.backref('user_roles', lazy=True))

    def __repr__(self):
        return f'<UserRoles {self.user.username} - {self.role.name}>'    
#Blog model
class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String)
    caption=db.Column(db.String)
    image_url=db.Column(db.String)
    timestamp=db.Column(db.DateTime,index=True, default=datetime.now())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    