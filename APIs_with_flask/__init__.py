from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jose@localhost:5432/Flask-SQLAlchemy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    from . import models
    from flask_migrate import Migrate
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def index():
        return 'hello'

    return app



