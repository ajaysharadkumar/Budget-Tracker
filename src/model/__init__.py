from .database import BudgetTrackerDatabase
from .transaction import Transaction
from .user import User

class BudgetTrackerModel:
    def __init__(self):
        self.db = BudgetTrackerDatabase()
        self.user = User(self.db)
        self.transaction = Transaction(self.db)

    def close_connection(self):
        self.db.close_connection()