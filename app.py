import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from configurations.config import config
from configurations.logging_config import setup_logging
from configurations.db_config import init_db
from flask_cors import CORS
from models.user_model import db

def create_app():

    app = Flask(__name__)

    app.config.from_object(config)

    #logger setup
    setup_logging()

    CORS(app,origins=["http://localhost:3000"]) # learn
    
    # init_db(app)
    db.init_app(app)

    migrate = Migrate(app, db, directory=os.path.join(os.getcwd(), 'repositories', 'db', 'sql', 'migrations'))

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "success", "message": "App is running"}), 200
    
    #defining user route
    # from routes.user_route import user_bp
    # app.register_blueprint(user_bp, url_prefix="/api/users")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=config.PORT, debug=config.DEBUG)





