import uuid
from sqlalchemy.dialects.postgresql import UUID
from configurations.db_config import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    # Define the columns for the user table
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # UUID as primary key
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile_number = db.Column(db.String(15), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    two_fa_authenticated = db.Column(db.Boolean, default=False)  # Track if 2FA is enabled
    profile_pic = db.Column(db.String(255), nullable=True)  # URL or file path for profile pic
    status_message = db.Column(db.String(255), nullable=True)  # User's status message
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # When the user was created
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # When the user was last updated

    def to_dict(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "mobile_number": self.mobile_number,
            "two_fa_authenticated": self.two_fa_authenticated,
            "profile_pic": self.profile_pic,
            "status_message": self.status_message,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __repr__(self):
        return f'<User {self.id} - {self.first_name} {self.last_name}>'
