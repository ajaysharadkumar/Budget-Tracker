def setup_income_page(self):
    page = self.pages["Income"]

    income_account_entry = create_labeled_entry(page, "Account Name")
    income_category_entry = create_labeled_entry(page, "Category")
    income_amount_entry = create_labeled_entry(page, "Amount")
    income_date_entry = create_labeled_entry(page, "Date (YYYY-MM-DD)")

    create_button(
        page,
        "Add Income",
        lambda: self.add_income(
            income_account_entry.get(),
            income_category_entry.get(),
            income_amount_entry.get(),
            income_date_entry.get(),
        ),