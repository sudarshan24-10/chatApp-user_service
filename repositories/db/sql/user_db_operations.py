from abstract_repositories.abstract_db.sql.user_db_process import AbstractUserDB
from models.user_model import User , db



class UserDBProcess(AbstractUserDB):

    def find_by_email(self, email: str):
        try:
            return User.query.filter_by(email=email).first()
        except Exception as e:
            raise e

    def find_by_id(self, user_id: int):
        return self.users.get(user_id)

    def create(self, user_data: dict):
        print("Creating user: %s" % user_data)
        try:
            existing_user = self.find_by_email(user_data['email'])

            if existing_user:
                raise ValueError(f"User with email {user_data.get('email')} already exists.")
            
            new_user = User(**user_data)

            new_user.to_dict()
            db.session.add(new_user)
            db.session.commit()
            return new_user

        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, user):
        user_id = user.get('id')
        if user_id and user_id in self.users:
            # Update the stored user's data.
            self.users[user_id].update(user)
            return self.users[user_id]
        return None

    def delete(self, user):
        # Delete a user from the "database". The user dict should contain an 'id' key.
        user_id = user.get('id')
        if user_id and user_id in self.users:
            del self.users[user_id]
            return True
        return False
