from ..db.database import Database 

db = Database()


class Transaction:

    @staticmethod
    def total_by_client():
        query = """
                 SELECT c.client_id, c.name, SUM(t.amount) as total
                 FROM transactions t
                 JOIN clients c ON t.client_id = c.client_id
                 GROUP BY c.client_id, c.name;
                 """
        return db.fetch_all(query)
    
    @staticmethod
    def total_by_date():
        query = """
                SELECT t.date, SUM(t.amount) as total
                FROM transactions t
                GROUP BY t.date
                ORDER BY t.date;
            """
        return db.fetch_all(query)
    
    @staticmethod
    def average_by_client():
        query = """
                SELECT c.client_id, c.name, AVG(t.amount) as average
                FROM transactions t
                JOIN clients c ON t.client_id = c.client_id
                GROUP BY c.client_id, c.name;
                """
        return db.fetch_all(query)
    
    @staticmethod
    def average_by_date():
        query =  """
                SELECT t.date, AVG(t.amount) as average
                FROM transactions t
                GROUP BY t.date
                ORDER BY t.date;
            """
        return db.fetch_all(query)
    
    @staticmethod
    def daily_total_by_client():
        query ="""
                SELECT
                    c.name AS client,
                    t.date,
                    SUM(t.amount) AS total_disbursed
                FROM transactions t
                JOIN clients c ON t.client_id = c.client_id
                GROUP BY c.name, t.date
                ORDER BY c.name, t.date;
                """
        return db.fetch_all(query)
    
    @staticmethod
    def daily_total_by_payment_method():
        query = """
                SELECT
                    p.name AS payment_method,
                    t.date,
                    SUM(t.amount) AS total_disbursed
                FROM transactions t
                JOIN payment_methods p ON t.payment_method_id = p.payment_method_id
                GROUP BY p.name, t.date
                ORDER BY p.name, t.date;
                """
        return db.fetch_all(query)
    
    @staticmethod
    def get_all_transactions():
        query = """
                    SELECT 
                        t.id AS transaction_id,
                        t.date,
                        c.client_id AS client_id,
                        c.name AS client_name,
                        t.amount,
                        p.name AS payment_method
                    FROM transactions t
                    JOIN clients c ON t.client_id = c.client_id
                    JOIN payment_methods p ON t.payment_method_id = p.payment_method_id;
                """
        return db.fetch_all(query)