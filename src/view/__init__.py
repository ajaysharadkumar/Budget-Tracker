from .main_view import MainView
from .authentication_view import AuthenticationView
from .income_view import IncomeView
from .expense_view import ExpenseView
from .visualization_view import VisualizationView
from .summary_view import SummaryView
from .budget_analysis_view import BudgetAnalysisView

class BudgetTrackerView:
    def __init__(self, root):
        self.root = root
        self.main_view = MainView(root)
        self.auth_view = AuthenticationView(self.main_view.pages["User Authentication"])
        self.income_view = IncomeView(self.main_view.pages["Income"])
        self.expense_view = ExpenseView(self.main_view.pages["Expenses"])
        self.visualization_view = VisualizationView(self.main_view.pages["Visualization"])
        self.summary_view = SummaryView(self.main_view.pages["Summary"])
        self.budget_analysis_view = BudgetAnalysisView(self.main_view.pages["Budget Analysis"])

    def run(self):
        self.root.mainloop()