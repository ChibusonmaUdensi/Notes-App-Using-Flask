from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone= True), default =func.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(150), nullable=False)
    notes = db.relationship("Note", backref='user')
    
    def __init__(self, first_name, email, password, password_hash):
        self.first_name = first_name
        self.email = email
        self.password_hash = password_hash
    def set_password(self, password):
        """Generate a hashed password and set the password_hash."""
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the hashed password."""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password) 