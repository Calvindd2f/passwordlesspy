import logging

from flask import Swagger
from flask import Flask
from flask import Marshmallow
from . import passwordless
import logging
from flask import Flask, jsonify
from logging.handlers import RotatingFileHandler
from passwordless import bp as passwordless_bp
from passwordless_api import api_bp
from config import Config, DevelopmentConfig, ProductionConfig

logging.basicConfig(encoding="utf-8", level=logging.DEBUG)




def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(config_class)
    app.config.from_prefixed_env()
    app.debug = True

    Marshmallow(app)

    Swagger(
        app,
        template_file="passwordless_api.json",
        merge=True,
        config={
            "openapi": "3.0.1",
        },
    )

    # Setup logging
    if not app.debug:
        file_handler = RotatingFileHandler('server.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Application startup')

    # Register blueprints
    app.register_blueprint(passwordless_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # Error handlers
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(error='Internal server error'), 500

    with app.app_context():
        app.register_blueprint(passwordless.bp)
        app.add_url_rule("/", "index", passwordless.index)

    return app

# In practice, these environment-specific settings should be set in your config file
app = create_app()

if __name__ == "__main__":
    app.run()
