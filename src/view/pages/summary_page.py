def setup_summary_page(self):
    page = self.pages["Summary"]

    summary_account_entry = create_labeled_entry(page, "Account Name")
    self.summary_text = create_textbox(page)

    create_button(
        page,
        "Display Summary",
        lambda: self.update_summary(summary_account_entry.get(), self.summary_text),
    )

    create_button(
        page,
        "Export All Data",
        lambda: self.export_all_data(summary_account_entry.get()),
    )