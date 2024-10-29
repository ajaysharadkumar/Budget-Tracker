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