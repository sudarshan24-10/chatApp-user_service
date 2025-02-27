import hashlib
import logging

logger = logging.getLogger(__name__)

class HashPassword:
    def process(self, password):
        try:
            if not isinstance(password, str):
                raise TypeError("Password must be a string.")

            password_bytes = password.encode('utf-8')
 
            hash_object = hashlib.sha256()
            
            hash_object.update(password_bytes)
            
            hashed_password = hash_object.hexdigest()

            return hashed_password
        except Exception as e:
            logger.error(f"An error occurred while hashing the password: {e}")
            return None
