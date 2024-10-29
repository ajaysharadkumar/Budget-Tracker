from src.utils.database import BudgetTrackerDatabase
from src.model.transaction_model import Transaction
from src.model.user_model import User

class BudgetTrackerModel:
    def __init__(self):
        self.db = BudgetTrackerDatabase()
        self.user = User(self.db)
        self.transaction = Transaction(self.db)

    def close_connection(self):
        self.db.close_connection()