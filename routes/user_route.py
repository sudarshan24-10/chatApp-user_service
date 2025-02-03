
from flask import Blueprint, request, jsonify
from service.user_service import User_service
from utils.error_util import CustomError
from schema.signup.signup_request_schema import signup_schema
class UserRoute:
    bp = Blueprint("user", __name__)  
    @bp.route("/signup", methods=["POST"])
    def register():
        try:
            user_data = request.get_json()
            validated_data = signup_schema.validate(user_data)
            user_service = User_service()  
            registered_user = user_service.register(validated_data)  # get the response back from user service
            return jsonify({"message": "User registered successfully", "user": registered_user}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        except CustomError as e:
            raise e
