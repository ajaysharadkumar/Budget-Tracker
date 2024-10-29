def show_notification(self, message: str, message_type: str) -> None:
    """Display a pop-up notification in the bottom-right corner."""
    # Create a Toplevel window (pop-up)
    popup = ctk.CTkToplevel(self.root)
    popup.overrideredirect(True)  # Remove window decorations (close, minimize, etc.)
    popup.configure(fg_color="#000000")  # Set background color to black

    # Create a label in the pop-up with dynamic text
    self.notification_label = ctk.CTkLabel(
        popup,
        text=message,
        text_color="white",
        fg_color="#1E90FF",  # Blue background color
        bg_color="#000000",  # Black background color
        font=("Arial", 12, "bold"),  # Font style, smaller for less height
        corner_radius=8,  # Rounded corners
        padx=10,
        pady=5  # Decreased padding to reduce overall height
    )
    color = {
        "error": "red",
        "success": "green"
    }.get(message_type, "white")
    self.notification_label.pack(expand=True, fill="both", padx=10, pady=10)
    self.notification_label.configure(text=message, text_color=color)

    size, root_x, root_y = self.root.geometry().split('+')
    root_x = int(root_x)
    root_y = int(root_y)

    root_w, root_h = size.split('x')
    root_w = int(root_w)
    root_h = int(root_h)

    # Update the popup size based on the label text
    popup.update_idletasks()  # Update "requested size" from geometry manager
    popup_width = self.notification_label.winfo_width() + 20  # Adding padding
    popup_height = self.notification_label.winfo_height() + 20  # Adding padding
    popup.minsize(250, 50)  # Set minimum size for the pop-up

    popup_y = root_y + (root_h - popup_height - popup_height // 2)  # Almost bottom
    popup_x = root_x + (root_w - (
        popup_width + 20 if popup_width >= 250 else 270))  # FIXME: why isn't popup_width the exact width?

    popup.geometry(f"{popup_width}x{popup_height}+{popup_x}+{popup_y}")

    # Automatically destroy the pop-up after a certain duration
    popup.after(3000, popup.destroy)  # Automatically close after 3 seconds

    # Bind the resize event of the main window to update the position
    def update_popup_position(event):
        popup.geometry(f"{popup_width}x{popup_height}+{popup_x}+{popup_y}")

    # Update position when the main window is resized
    self.root.bind("<Configure>", update_popup_position)


def run(self):
    self.root.mainloop()

