import logging
from utils.error_util import CustomError
from repositories.db.sql.user_db_operations import UserDBProcess
from usecase.registration_usecase import Registration_usecase

logger = logging.getLogger(__name__)

class User_service:
        
    def register(self,data):
        try:
            sql_db_process = UserDBProcess()
            registration_usecase = Registration_usecase(sql_db_process)
            response = registration_usecase.register(data)
            return response
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            raise e
        except CustomError as e:
            logger.error(f"Error registering user: {e}")
            raise e


