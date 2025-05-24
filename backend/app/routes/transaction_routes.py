from flask import jsonify
from flask import Blueprint
from ..services.transaction import Transaction

transaction_bp = Blueprint("transactions", __name__, url_prefix="/transactions")

@transaction_bp.route("/total-by-client", methods = ["GET"])
def total_by_client():
    data = Transaction.total_by_client()
    return jsonify(data)

@transaction_bp.route("/total-by-date", methods = ["GET"])
def total_by_date():
    data = Transaction.total_by_date()
    return data

@transaction_bp.route("/daily-total-by-client", methods = ["GET"])
def daily_total_by_client():
    data = Transaction.daily_total_by_client()
    return data

@transaction_bp.route("/daily-total-by-payment-method", methods = ["GET"])
def daily_total_by_payment_method():
    data = Transaction.daily_total_by_payment_method()
    return data

@transaction_bp.route("/", methods = ["GET"])
def transactions():
    data = Transaction.get_all_transactions()
    return data