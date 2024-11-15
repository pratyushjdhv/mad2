from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

# Define the User model
class User(db.Model, UserMixin):
    __tablename__ = 'user'  # Explicit table name for clarity
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)

    # Flask-Security stuff
    fs_uniquifier = db.Column(db.String, nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)
    roles = db.relationship('Role', secondary='user_roles', backref='users')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# Define the Role model
class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'  # Explicit table name for clarity
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

# Association table for User and Role
class UserRoles(db.Model):
    __tablename__ = 'user_roles'  # Explicit table name for clarity
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

    def __repr__(self):
        return f"<UserRoles(user_id={self.user_id}, role_id={self.role_id})>"
