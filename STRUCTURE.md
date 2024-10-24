```#markdown
# Project Structure
project-root/
├── .github/                     # GitHub specific configurations
├── .venv/                       # Python virtual environment
├── data/                        # Data directory
│   └── budget_tracker.db        # SQLite database file
├── src/                         # Source code directory
│   ├── assets/                  # Asset files
│   │   ├── icon.ico             # Application icon (ICO format)
│   │   └── icon.png             # Application icon (PNG format)
│   ├── model/                  # Data models
│   │   ├── init.py
│   │   ├── account_model.py
│   │   ├── transaction_model.py
│   │   └── user_model.py
│   ├── view/                   # UI components
│   │   ├── init.py
│   │   ├── components/          # Reusable UI components
│   │   │   ├── init.py
│   │   │   ├── buttons.py
│   │   │   ├── entries.py
│   │   │   ├── charts.py
│   │   │   └── notifications.py
│   │   ├── pages/               # Application pages
│   │   │   ├── init.py
│   │   │   ├── auth_page.py
│   │   │   ├── income_page.py
│   │   │   ├── expense_page.py
│   │   │   ├── visualization_page.py
│   │   │   ├── summary_page.py
│   │   │   └── analysis_page.py
│   │   └── main_view.py
│   ├── controller/            # Business logic
│   │   ├── init.py
│   │   ├── auth_controller.py
│   │   ├── transaction_controller.py
│   │   ├── visualization_controller.py
│   │   └── export_controller.py
│   └── utils/                  # Utility functions
│       ├── init.py
│       ├── database.py
│       └── currency_converter.py
├── .gitignore                  # Git ignore file
├── CODE_OF_CONDUCT.md          # Code of conduct
├── CONTRIBUTING.md             # Contribution guidelines
├── main.py                     # Application entry point
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── STRUCTURE.md                # Project structure documentation
```
