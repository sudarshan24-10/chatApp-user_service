from flask_restx import Api

def init_api(app):
    api = Api(
        app,
        title='My API',
        version='1.0',
        description='user service',
        prefix='/api' 
    )
    
    return api