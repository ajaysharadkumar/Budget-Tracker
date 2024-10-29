def setup_expense_page(self):
    page = self.pages["Expenses"]

    expense_account_entry = create_labeled_entry(page, "Account Name")
    expense_category_entry = create_labeled_entry(page, "Category")
    expense_amount_entry = create_labeled_entry(page, "Amount")
    expense_date_entry = create_labeled_entry(page, "Date (YYYY-MM-DD)")

    create_button(
        page,
        "Add Expense",
        lambda: self.add_expense(
            expense_account_entry.get(),
            expense_category_entry.get(),
            expense_amount_entry.get(),
            expense_date_entry.get(),
        ),
    )
