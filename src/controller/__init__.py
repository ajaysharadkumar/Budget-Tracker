from src.controller.auth_controller import AuthenticationController
from src.controller.transaction_controller import TransactionController
from src.controller.visualization_controller import VisualizationController


class BudgetTrackerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.auth_controller = AuthenticationController(model.user, view.auth_view)
        self.transaction_controller = TransactionController(model.transaction, view.income_view, view.expense_view)
        self.visualization_controller = VisualizationController(model.transaction, view.visualization_view)
        self.summary_controller = SummaryController(model.transaction, view.summary_view)

        self.setup_event_handlers()

    def setup_event_handlers(self):
        # Sidebar
        for page, button in self.view.main_view.sidebar_buttons.items():
            button.configure(command=lambda p=page: self.view.main_view.show_page(p))

        # Other event handlers are set up in individual controllers