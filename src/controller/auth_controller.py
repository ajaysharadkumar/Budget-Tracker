
def setup_authentication_page(self):
    page = self.pages["User Authentication"]

    username_entry = create_labeled_entry(page, "Username")
    password_entry = create_labeled_entry(page, "Password", show="*")

    create_button(
        page,
        "Register",
        lambda: self.register(username_entry.get(), password_entry.get()),
    )

    create_button(
        page,
        "Login",
        lambda: self.login(username_entry.get(), password_entry.get()),
    )

    def is_valid_input(self, username: str, password: str) -> bool:
        """
        Validates the input for the username and password.
        Ensures that neither is empty and that they meet other criteria (if any).
        """
        if not username or not password:
            self.show_notification("Username and password are required.", "error")
        return True

    def register(self, username: str, password: str) -> None:
        """Register a new user with the given username and password."""
        if not self.is_valid_input(username, password):
            return

        try:
            create_user_account(self, self.db, username, password)
            self.show_notification("Registration successful!", "success")
        except ValueError as ve:
            self.show_notification(str(ve), "error")
        except RuntimeError as re:
            self.show_notification(str(re), "error")
        except Exception as e:
            self.show_notification(str(e), "error")

    def login(self, username, password):
        if not username or not password:
            self.show_notification("Username and password are required.", "error")
            return
        if validate_user(self.db, username, password):
            self.show_notification("Login successful!", "success")
            self.update_sidebar_buttons("Income")  # Enable all buttons after login
            self.show_page("Income")  # Show Income page after successful login
        else:
            self.show_notification("Invalid username or password.", "error")
