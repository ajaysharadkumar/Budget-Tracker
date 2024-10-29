def create_labeled_entry(
    parent: tk.Widget, label_text: str, show: Optional[str] = None
) -> ctk.CTkEntry:
    """Creates a labeled entry widget.

    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The label text for the entry.
        show (Optional[str]): A character to show instead of the actual input (e.g., '*').

    Returns:
        ctk.CTkEntry: The created entry widget.
    """
    ctk.CTkLabel(parent, text=label_text).pack(pady=5)
    entry = ctk.CTkEntry(parent, show=show)
    entry.pack(pady=5)
    return entry

def create_labeled_entry(
    parent: tk.Widget, label_text: str, show: Optional[str] = None
) -> ctk.CTkEntry:
    """Creates a labeled entry widget.

    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The label text for the entry.
        show (Optional[str]): A character to show instead of the actual input (e.g., '*').

    Returns:
        ctk.CTkEntry: The created entry widget.
    """
    ctk.CTkLabel(parent, text=label_text).pack(pady=5)
    entry = ctk.CTkEntry(parent, show=show)
    entry.pack(pady=5)
    return entry


def create_textbox(
    parent: tk.Widget, height: int = 400, width: int = 500
) -> ctk.CTkTextbox:
    """Creates a read-only textbox.

    Args:
        parent (tk.Widget): The parent widget.
        height (int): The height of the textbox.
        width (int): The width of the textbox.

    Returns:
        ctk.CTkTextbox: The created textbox widget.
    """
    text_box = ctk.CTkTextbox(parent, height=height, width=width)
    text_box.pack(pady=10)
    text_box.configure(state=tk.DISABLED)
    return text_box


def clear_textbox(text_box: ctk.CTkTextbox) -> None:
    """Clears the content of a textbox.

    Args:
        text_box (ctk.CTkTextbox): The textbox to be cleared.
    """
    text_box.configure(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.configure(state=tk.DISABLED)


def update_textbox(text_box: ctk.CTkTextbox, text: str) -> None:
    """Updates the content of a textbox.

    Args:
        text_box (ctk.CTkTextbox): The textbox to be updated.
        text (str): The new text to insert into the textbox.
    """
    text_box.configure(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)
    text_box.configure(state=tk.DISABLED)

