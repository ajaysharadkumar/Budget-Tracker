def __init__(self, root):
    self.root = root
    self.root.title("Budget Tracker")
    self.root.geometry("1000x600")

    self.root.iconbitmap("Icon.ico")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    try:
        self.db = create_or_open_database("budget_tracker.db")
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return

    self.setup_ui()

    def setup_ui(self):
        # Create main layout
        self.sidebar = ctk.CTkFrame(self.root, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)

        self.main_content = ctk.CTkFrame(self.root)
        self.main_content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Create sidebar buttons
        self.sidebar_buttons = {}
        for page in self.PAGES:
            btn = ctk.CTkButton(
                self.sidebar, text=page, command=lambda p=page: self.show_page(p)
            )
            btn.pack(pady=10, padx=20)
            self.sidebar_buttons[page] = btn

        # Disable all buttons except User Authentication initially
        self.update_sidebar_buttons("User Authentication")

        # Create pages
        self.pages = {}
        for page in self.PAGES:
            self.pages[page] = ctk.CTkFrame(self.main_content)

        # Setup individual pages
        self.setup_authentication_page()
        self.setup_income_page()
        self.setup_expense_page()
        self.setup_visualization_page()
        self.setup_summary_page()
        self.setup_budget_analysis_page()

        # Show initial page
        self.show_page("User Authentication")

        # Create a label for notifications
        self.notification_label = ctk.CTkLabel(self.root, text="", text_color="white")
        self.notification_label.pack(side="bottom", pady=5)

        def show_page(self, page_name):
            for page in self.pages.values():
                page.pack_forget()
            self.pages[page_name].pack(fill="both", expand=True)