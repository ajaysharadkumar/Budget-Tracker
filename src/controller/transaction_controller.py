def add_income(self, account_name, category, amount, date):
    try:
        if not account_name or not category or not amount or not date:
            raise ValueError("All fields are required.")
        amount = float(amount)
        account_id = get_account_id(self.db, account_name)
        if account_id is None:
            raise ValueError("Account does not exist.")
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO transactions (account_id, type, category, amount, date) VALUES (?, 'income', ?, ?, ?)",
            (account_id, category, amount, date),
        )
        self.db.commit()
        self.show_notification("Income added successfully.", "success")
    except ValueError as ve:
        self.show_notification(str(ve), "error")
    except Exception as e:
        self.show_notification(f"An error occurred: {str(e)}", "error")


def add_expense(self, account_name, category, amount, date):
    try:
        if not account_name or not category or not amount or not date:
            raise ValueError("All fields are required.")
        amount = float(amount)
        account_id = get_account_id(self.db, account_name)
        if account_id is None:
            raise ValueError("Account does not exist.")
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO transactions (account_id, type, category, amount, date) VALUES (?, 'expense', ?, ?, ?)",
            (account_id, category, amount, date),
        )
        self.db.commit()
        self.show_notification("Expense added successfully.", "success")
    except ValueError as ve:
        self.show_notification(str(ve), "error")
    except Exception as e:
        self.show_notification(f"An error occurred: {str(e)}", "error")
