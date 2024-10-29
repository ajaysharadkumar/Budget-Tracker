def setup_budget_analysis_page(self):
    page = self.pages["Budget Analysis"]

    analysis_account_entry = create_labeled_entry(page, "Account Name")
    self.analysis_text = create_textbox(page)

    create_button(
        page,
        "Calculate Budget Analysis",
        lambda: self.budget_analysis(
            analysis_account_entry.get(), self.analysis_text
        ),
    )