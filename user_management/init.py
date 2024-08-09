from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
urls_blueprint = None  # Оставляем как None, чтобы избежать циклического импорта


def create_app():
    from flask import Flask  # Импортируем Flask здесь, чтобы избежать циклического импорта
    from config import Config  # Импортируем Config здесь, чтобы избежать циклического импорта
    from urls import urls_blueprint  # Импортируем urls_blueprint здесь, чтобы избежать циклического импорта

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Инициализируем db внутри create_app

    app.register_blueprint(urls_blueprint)

    return app
