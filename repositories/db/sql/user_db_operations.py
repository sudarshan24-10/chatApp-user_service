from abstract_repositories.abstract_db.sql.user_db_process import AbstractUserDB
from models.user_model import User , db
from usecase.password_hashing_usecase import HashPassword
import json

class UserDBProcess(AbstractUserDB):

    def find_by_email(self, email: str):
        try:
            return User.query.filter_by(email=email).first()
        except Exception as e:
            raise e

    def find_by_id(self, user_id: int):
        pass

    def create(self, user_data: dict):
        try:
            existing_user = self.find_by_email(user_data['email'])

            if existing_user:
                raise ValueError(f"User with email {user_data.get('email')} already exists.")
            
            hash_password = HashPassword()
            user_data['password'] = hash_password.process(user_data['password'])
            
            new_user = User(**user_data)

            db.session.add(new_user)

            db.session.commit()

            data=new_user.to_dict()
            return data

        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, user):
        pass

    def delete(self, user):
        pass
