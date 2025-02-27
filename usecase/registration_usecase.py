from abstract_repositories.abstract_db.sql.user_db_process import AbstractUserDB
import logging
logger = logging.getLogger(__name__)

class Registration_usecase():
    def __init__(self,repository:AbstractUserDB):
        self.repository = repository

    def register(self,data):
        try:
            response = self.repository.create(data)
            return response
        except Exception as e:
            raise e
        
