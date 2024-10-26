import customtkinter as ctk
from src.model import BudgetTrackerModel
from src.view import BudgetTrackerView
from src.controller import BudgetTrackerController

def main():
    root = ctk.CTk()
    model = BudgetTrackerModel()
    view = BudgetTrackerView(root)
    controller = BudgetTrackerController(model, view)
    view.run()

if __name__ == "__main__":
    main()