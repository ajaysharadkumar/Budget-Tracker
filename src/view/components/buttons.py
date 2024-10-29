def create_button(parent: tk.Widget, text: str, command: Callable) -> ctk.CTkButton:
    """Creates a button widget.

    Args:
        parent (tk.Widget): The parent widget.
        text (str): The text displayed on the button.
        command (Callable): The function to be called when the button is clicked.

    Returns:
        ctk.CTkButton: The created button widget.
    """
    button = ctk.CTkButton(parent, text=text, command=command)
    button.pack(pady=10)
    return button