from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

logger = logging.getLogger(__name__)

db = SQLAlchemy() 
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return db
