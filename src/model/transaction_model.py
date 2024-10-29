def export_all_data(self, account_name):
    try:
        result = export_to_csv(account_name, self.db)
        if result:
            income_file, expenses_file, summary_file = result
            self.show_notification(
                f"Data exported successfully:\n{income_file}\n{expenses_file}\n{summary_file}",
                "success",
            )
        else:
            self.show_notification("Failed to export data.", "error")
    except Exception as e:
        self.show_notification(f"Error during export: {str(e)}", "error")


def get_income_data(self, account_name):
    account_id = get_account_id(self.db, account_name)
    if account_id is None:
        raise ValueError("Account does not exist.")
    cursor = self.db.cursor()
    cursor.execute(
        "SELECT category, SUM(amount) FROM transactions WHERE account_id = ? AND type = 'income' GROUP BY category",
        (account_id,),
    )
    results = cursor.fetchall()
    data = [row[1] for row in results]
    labels = [row[0] for row in results]
    return data, labels


def get_expense_data(self, account_name):
    account_id = get_account_id(self.db, account_name)
    if account_id is None:
        raise ValueError("Account does not exist.")
    cursor = self.db.cursor()
    cursor.execute(
        "SELECT category, SUM(amount) FROM transactions WHERE account_id = ? AND type = 'expense' GROUP BY category",
        (account_id,),
    )
    results = cursor.fetchall()
    data = [row[1] for row in results]
    labels = [row[0] for row in results]
    return data, labels


def get_income_time_data(self, account_name):
    """Get income data for line chart"""
    try:
        account_id = get_account_id(self.db, account_name)
        if account_id is None:
            raise ValueError("Account does not exist.")
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT date, SUM(amount) FROM transactions "
            "WHERE account_id = ? AND type = 'income' "
            "GROUP BY date ORDER BY date",
            (account_id,)
        )
        results = cursor.fetchall()
        if not results:
            return [], []

        # Separate dates and amounts, keeping the date format as is
        dates = [row[0] for row in results]
        amounts = [row[1] for row in results]
        return dates, amounts
    except Exception as e:
        print(f"Error getting income data: {e}")
        return [], []


def get_expense_time_data(self, account_name):
    """Get expense data for line chart"""
    try:
        account_id = get_account_id(self.db, account_name)
        if account_id is None:
            raise ValueError("Account does not exist.")
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT date, SUM(amount) FROM transactions "
            "WHERE account_id = ? AND type = 'expense' "
            "GROUP BY date ORDER BY date",
            (account_id,)
        )
        results = cursor.fetchall()
        if not results:
            return [], []

        # Separate dates and amounts, keeping the date format as is
        dates = [row[0] for row in results]
        amounts = [row[1] for row in results]
        return dates, amounts
    except Exception as e:
        print(f"Error getting expense data: {e}")
        return [], []
