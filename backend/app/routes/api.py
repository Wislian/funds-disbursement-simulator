from flask import Blueprint
from .transaction_routes import transaction_bp

api_bp = Blueprint("api",__name__,url_prefix= "/api")

api_bp.register_blueprint(transaction_bp)