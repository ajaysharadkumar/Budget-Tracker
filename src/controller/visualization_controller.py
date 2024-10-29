def show_bar_chart(self, account_name):
    try:
        data, labels = self.get_income_data(account_name)
        plot_bar_chart(data, labels, "Income by Category", self.chart_frame)
    except Exception as e:
        self.show_notification(f"Error displaying chart: {str(e)}", "error")


def show_pie_chart(self, account_name):
    try:
        data, labels = self.get_expense_data(account_name)
        plot_pie_chart(data, labels, "Expenses by Category", self.chart_frame)
    except Exception as e:
        self.show_notification(f"Error displaying chart: {str(e)}", "error")


def show_line_chart(self, account_name):
    try:
        income_data = self.get_income_time_data(account_name)
        expense_data = self.get_expense_time_data(account_name)
        plot_line_chart(income_data, expense_data, self.chart_frame)
    except Exception as e:
        self.show_notification(f"Error displaying chart: {str(e)}", "error")