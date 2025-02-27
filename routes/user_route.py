from flask import Blueprint, request, jsonify
from service.user_service import User_service
from utils.error_util import CustomError
from schema.signup.signup_request_schema import signup_schema
from marshmallow.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

class UserRoute:
   
    bp = Blueprint("user", __name__)  

    @bp.route("/signup", methods=["POST"])
    def register():

        try:
            user_data = request.get_json()
            validated_data = signup_schema.load(user_data)
            user_service = User_service()  
            registered_user = user_service.register(validated_data)  
            return jsonify({"message": "User registered successfully", "user": registered_user}), 201
        except ValidationError as ve:
            logger.error("User registration failed: %s", ve.messages)
            return jsonify({"error": "Validation error", "message": ve.messages}), 400
        except CustomError as e:
            logger.error(f"User registration failed with CustomError : {e.message} and code: {e.status_code}")
            raise e
        except Exception as e:
            logger.error("Unexpected error: %s", str(e))
            return jsonify({"error": "UnexpectedError", "message": str(e)}), 500
