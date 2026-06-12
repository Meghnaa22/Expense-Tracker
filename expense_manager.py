from datetime import datetime

class ExpenseManager:
    def __init__(self, db):
        self.db = db

    def add_expense(self, date, category, amount, description=""):
        if isinstance(date, str):
            date = datetime.fromisoformat(date).date()
        self.db.insert_expense(date, category.strip().title(), float(amount), description.strip())

    def get_all(self):
        return self.db.query("SELECT * FROM expenses ORDER BY date")
