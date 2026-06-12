class Report:
    def __init__(self, db):
        self.db = db

    def total_by_category(self):
        return self.db.query("""
            SELECT category, SUM(amount) as total
            FROM expenses GROUP BY category ORDER BY total DESC
        """)

    def total_by_month(self):
        return self.db.query("""
            SELECT strftime('%Y-%m', date) as month, SUM(amount) as total
            FROM expenses GROUP BY month ORDER BY month
        """)
