from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from app.routes.chat import chat_bp
    from app.routes.diagnosis import diagnosis_bp
    from app.routes.planner import planner_bp

    # Register routes
    app.register_blueprint(chat_bp)
    app.register_blueprint(diagnosis_bp)
    app.register_blueprint(planner_bp)

    return app
