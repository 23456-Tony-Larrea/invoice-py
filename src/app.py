from flask import Flask
from models.user_model import db
from routes.user_routes import user_bp
from routes.login_register_routes import login_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/invoice'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp)
    app.register_blueprint(login_bp)

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    