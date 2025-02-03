import logging
from utils.error_util import CustomError
logger = logging.getLogger(__name__)

class User_service:
    

    def register(self,data):
        try:
            logger.info(f"registering user: {data}")
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            raise e
        except CustomError as e:
            logger.error(f"Error registering user: {e}")
            raise e


