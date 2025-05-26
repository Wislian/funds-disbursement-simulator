from flask import jsonify
from flask import Blueprint
from flask import request
from ..services.transaction import Transaction

transaction_bp = Blueprint("transactions", __name__, url_prefix="/transactions")

@transaction_bp.route("/info-by-client", methods = ["GET"])
def info_by_client():
    client_id = request.args.get("client_id",type = int)
    if client_id is not None:
        data, error_code = Transaction.info_by_client_id(client_id)
        if data is not None:
            return jsonify(data)
        elif error_code == "CLIENT_NOT_FOUND":
            return jsonify({
                "error":{
                    "message":"Client not found",
                    "code": error_code
                }
            }),404
        elif error_code == "NO_TRANSACTIONS_FOUND":
            return jsonify([]),200
        elif error_code == "DATABASE_ERROR":
            return jsonify({
                "error": {
                    "message":"Database connection error",
                    "code": error_code,
                    "details": "Try later"
                }
            }), 500
        else:
            return jsonify({"Error:":{
                "message":"Unknown error",
                "code":"UNKNOWN_ERROR"
                }
            }), 500
    else:
        data, error_code = Transaction.info_by_client()
        if data is not None:
            return jsonify(data)
        elif error_code == "DATABASE_ERROR":
            return jsonify({
                "error":{
                    "message":"Database connection error",
                    "code":error_code,
                    "details":"Try later"
                }
            }),500
        else:
            return jsonify({
                "error":{
                    "message":"Failed to retrieve the list of clients",
                    "code":"CLIENT_FETCH_ERROR"
                }
            }), 500   

@transaction_bp.route("/", methods = ["GET"])
def transactions():
    data, error_code = Transaction.get_all_transactions()
    if data is not None:
        return jsonify(data)
    elif error_code == "DATABASE_ERROR":
        return jsonify({
            "error":{
                "message":"Database connection error",
                "code": error_code,
                "details":"Try later"
            }
        }), 500
    else:
        return jsonify({
            "error":{
                "massage": "Failed to retrieve the list of transactions",
                "code":"TRANSACTION_FETCH_ERROR"
            }
        }), 500

