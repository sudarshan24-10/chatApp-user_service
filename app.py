import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from configurations.config import config
from configurations.logging_config import setup_logging
from configurations.db_config import init_db
from flask_cors import CORS
from routes.user_route import UserRoute
from utils.error_util import CustomError
# from configurations.swagger_config import init_api
def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # Logger setup
    setup_logging()

    CORS(app, origins=["http://localhost:3000"])  # Enable CORS for frontend app (React, for example)
    
    # Initialize database
    db = init_db(app)
    
    # Initialize Flask-RESTX API
    # api=init_api(app)

    migrate = Migrate(app, db, directory=os.path.join(os.getcwd(), 'repositories', 'db', 'sql', 'migrations'))

    # Registering error handler
    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        response = jsonify({"error": error.message})
        response.status_code = error.status_code
        return response

    # Health check route
    @app.route("/", methods=["GET"])
    def health_check():
        return jsonify({"status": "success", "message": "App is running"}), 200

    # Register User routes with Namespace, not Blueprint here
    app.register_blueprint(UserRoute.bp,url_prefix="/api/users")

    return app

if __name__ == "__main__":
    app = create_app()
    print(f"Server running on port http://localhost:{config.PORT}")
    app.run(port=config.PORT, debug=config.DEBUG)
