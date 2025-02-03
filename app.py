import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from configurations.config import config
from configurations.logging_config import setup_logging
from configurations.db_config import init_db
from flask_cors import CORS
from models.user_model import db
<<<<<<< Updated upstream
from flask_restx import Api
=======
from routes.user_route import UserRoute
from utils.error_util import CustomError
>>>>>>> Stashed changes

def create_app():

    app = Flask(__name__)

    app.config.from_object(config)

    #logger setup
    setup_logging()

    CORS(app,origins=["http://localhost:3000"]) # learn
    
    # init_db(app)
    db.init_app(app)

    api = Api(app, version=1.0, title= "user_service api documentation", description="user service documentation")

    migrate = Migrate(app, db, directory=os.path.join(os.getcwd(), 'repositories', 'db', 'sql', 'migrations'))

    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        response = jsonify({"error": error.message})
        response.status_code = error.status_code
        return response
    
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "success", "message": "App is running"}), 200
    
    # from routes.user_route import user_bp
    app.register_blueprint(UserRoute.bp, url_prefix="/api/users")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=config.PORT, debug=config.DEBUG)





