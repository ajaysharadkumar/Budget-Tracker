import tkinter as tk
import customtkinter as ctk
from typing import Callable, Optional
from tkinter import ttk

def create_scrollable_frame(parent: tk.Widget) -> ctk.CTkFrame:
    """Creates a frame with a vertical scrollbar.

    Args:
        parent (tk.Widget): The parent widget.

    Returns:
        ctk.CTkFrame: The created scrollable frame.
    """
    try:
        canvas = ctk.CTkCanvas(parent)
        scrollbar = ctk.CTkScrollbar(
            parent, orientation="vertical", command=canvas.yview
        )
        scrollable_frame = ctk.CTkFrame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame
    except Exception as e:
        print(f"Error creating scrollable frame: {e}")
        return None

# create Dropdown
def create_dropdown(parent, options, default=None):
    selected_var = tk.StringVar(value=default if default else options[0])
    
    # Create the dropdown
    dropdown = ttk.Combobox(parent, textvariable=selected_var, values=options)
    dropdown.set(default if default else options[0])
    dropdown.pack(pady=10)

    return selected_var