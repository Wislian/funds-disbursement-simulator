from ..db.database import Database 
import psycopg2

db = Database()


class Transaction:
    
    @staticmethod
    def info_by_client():
        query = """
            SELECT 
                c.name, 
                t.amount, 
                t.date, 
                p.name AS payment_method
            FROM transactions t
            JOIN clients c ON t.client_id = c.client_id
            JOIN payment_methods p ON t.payment_method_id = p.payment_method_id
            ORDER BY t.date DESC;
        """
        try:
            return db.fetch_all(query), None
        except Exception as e:
            print(f"Postgres error in info_by_client: {e} ")
            return None, "DATABASE_ERROR"
    
    @staticmethod
    def info_by_client_id(client_id):
        try:
            client_exists_query = "SELECT client_id FROM clients WHERE client_id = %s"
            client = db.fetch_one(client_exists_query,(client_id,))
            if not client:
                 return None, "CLIENT_NOT_FOUND"
            else:
                query = """
                    SELECT 
                        c.client_id, 
                        c.name, 
                        t.id as transaction_id,
                        t.amount, 
                        t.date, 
                        p.name as payment_method
                    FROM transactions t
                    JOIN clients c ON t.client_id = c.client_id
                    JOIN payment_methods p ON t.payment_method_id = p.payment_method_id
                    WHERE c.client_id = %s
                    ORDER BY t.date DESC;
                """
                result = db.fetch_all(query,(client_id,))
                if not result:
                    return [], "NO_TRANSACTIONS_FOUND"
                return result, None
        except psycopg2.Error as e:
            print(f"Postgres error in info_by_client_id (ID: {client_id}):{e}")
            return None, "DATABASE_ERROR"

    @staticmethod
    def get_all_transactions():
        query = """
                    SELECT 
                        t.date,
                        t.amount,
                        p.name AS payment_method
                    FROM transactions t
                    JOIN payment_methods p ON t.payment_method_id = p.payment_method_id;
                """
        try:
            return db.fetch_all(query), None
        except psycopg2.Error as e:
            print(f"Postgres error in get_all_transactions: {e}")
            return None, "DATABASE_ERROR"