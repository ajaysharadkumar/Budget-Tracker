def plot_bar_chart(data: list, labels: list, title: str, parent) -> None:
    try:
        fig, ax = create_figure()

        bars = ax.bar(labels,
                      data,
                      color='#1E90FF',
                      alpha=0.7,
                      width=0.6)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.,
                    height + (max(data) * 0.02),
                    f'${height:,.0f}',
                    ha='center',
                    va='bottom',
                    color='white',
                    fontsize=10,
                    fontweight='bold')

        ax.set_ylim(0, max(data) * 1.15)

        ax.set_xlabel("Category", fontsize=14, color='white', labelpad=15)
        ax.set_ylabel("Amount (USD)", fontsize=14, color='white', labelpad=15)

        plt.xticks(rotation=30, ha="right")

        setup_figure_style(fig, ax, title)
        plt.tight_layout(pad=3)

        display_chart(fig, parent)

    except Exception as e:
        logging.error(f"Error plotting bar chart: {e}")


def plot_pie_chart(data: list, labels: list, title: str, parent) -> None:
    try:
        fig, ax = create_figure()

        # Color map with a number of distinct colors based on the data length
        num_segments = len(data)
        colors = plt.cm.tab20(np.linspace(0, 1, num_segments))

        wedges, texts, autotexts = ax.pie(data,
                                          labels=labels,
                                          colors=colors,
                                          autopct='%1.1f%%',
                                          startangle=90,
                                          pctdistance=0.75,
                                          labeldistance=1.2)

        plt.setp(autotexts, size=12, weight="bold", color="white")
        plt.setp(texts, size=12, color="white")

        # Dark center circle
        centre_circle = plt.Circle((0, 0), 0.40, fc='#1a1a1a')
        ax.add_artist(centre_circle)

        total = sum(data)
        ax.text(0, 0, f'Total\n${total:,.0f}',
                ha='center',
                va='center',
                color='white',
                fontsize=14,
                fontweight='bold')

        setup_figure_style(fig, ax, title)
        plt.tight_layout(pad=3.5)

        display_chart(fig, parent)

    except Exception as e:
        logging.error(f"Error plotting pie chart: {e}")


def plot_line_chart(income_data: tuple, expense_data: tuple, parent) -> None:
    try:
        fig, ax = create_figure()

        max_value = 0

        if income_data and len(income_data[0]) > 0:
            dates = [datetime.strptime(date, "%d/%m/%Y").date() for date in income_data[0]]
            ax.plot(dates, income_data[1],
                    label="Income",
                    color='#4ECB71',
                    linewidth=2,
                    marker='o',
                    markersize=8,
                    markerfacecolor='#4ECB71',
                    markeredgecolor='white',
                    markeredgewidth=2)

            for i, (x, y) in enumerate(zip(dates, income_data[1])):
                offset = 20 if i % 2 == 0 else 35
                ax.annotate(f'${y:,.0f}',
                            (x, y),
                            xytext=(0, offset),
                            textcoords='offset points',
                            ha='center',
                            va='bottom',
                            color='#4ECB71',
                            fontsize=10,
                            fontweight='bold')
                max_value = max(max_value, y)

        if expense_data and len(expense_data[0]) > 0:
            dates = [datetime.strptime(date, "%d/%m/%Y").date() for date in expense_data[0]]
            ax.plot(dates, expense_data[1],
                    label="Expenses",
                    color='#FF6B6B',
                    linewidth=2,
                    marker='o',
                    markersize=8,
                    markerfacecolor='#FF6B6B',
                    markeredgecolor='white',
                    markeredgewidth=2)

            for i, (x, y) in enumerate(zip(dates, expense_data[1])):
                offset = -25 if i % 2 == 0 else -40
                ax.annotate(f'${y:,.0f}',
                            (x, y),
                            xytext=(0, offset),
                            textcoords='offset points',
                            ha='center',
                            va='top',
                            color='#FF6B6B',
                            fontsize=10,
                            fontweight='bold')
                max_value = max(max_value, y)

        ax.set_ylim(0, max_value * 1.25)

        ax.set_xlabel("Date", fontsize=14, color='white', labelpad=15)
        ax.set_ylabel("Amount (USD)", fontsize=14, color='white', labelpad=15)

        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.xticks(rotation=30, ha='right')

        legend = ax.legend(facecolor='#000000',
                           edgecolor='gray',
                           fontsize=12,
                           loc='upper left',
                           bbox_to_anchor=(0.02, 0.98),
                           framealpha=0.9)
        plt.setp(legend.get_texts(), color='white')

        setup_figure_style(fig, ax, "Income and Expenses Over Time")
        plt.tight_layout(pad=3)

        display_chart(fig, parent)

    except Exception as e:
        logging.error(f"Error plotting line chart: {e}")


def display_chart(fig: Figure, parent) -> None:
    try:
        for widget in parent.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()

        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill="both", expand=True, padx=15, pady=15)

        def on_resize(event):
            if abs(event.width - fig.get_size_inches()[0] * fig.dpi) > 50 or \
                    abs(event.height - fig.get_size_inches()[1] * fig.dpi) > 50:
                width = event.width / fig.dpi
                height = event.height / fig.dpi
                fig.set_size_inches(width, height)
                canvas.draw_idle()

        canvas_widget.bind('<Configure>', on_resize)

    except Exception as e:
        logging.error(f"Error displaying chart: {e}")
        error_label = ctk.CTkLabel(
            parent,
            text=f"Error displaying chart: {str(e)}",
            text_color="red"
        )
        error_label.pack(pady=20)

        def create_responsive_chart_card(self, parent, title, description, command, chart_type):
            card = ctk.CTkFrame(
                parent,
                fg_color="#1a1a1a",
                corner_radius=10,
                border_width=2,
                border_color="#2a2a2a"
            )

            card.grid_columnconfigure(0, weight=1)
            card.grid_rowconfigure((0, 1), weight=1)

            card.name = chart_type

            def on_click(event=None):
                if self.active_chart_var.get() != chart_type:
                    self.active_chart_var.set(chart_type)
                    self.update_card_styles()
                    self.update_chart_with_debounce()

            card.bind("<Button-1>", on_click)

            title_label = ctk.CTkLabel(
                card,
                text=title,
                font=ctk.CTkFont(family="Arial", size=-16, weight="bold"),
                text_color="white"
            )
            title_label.bind("<Button-1>", on_click)
            title_label.grid(row=0, column=0, padx=15, pady=(15, 5), sticky="w")

            desc_label = ctk.CTkLabel(
                card,
                text=description,
                font=ctk.CTkFont(family="Arial", size=-11),
                text_color="gray"
            )
            desc_label.bind("<Button-1>", on_click)
            desc_label.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="w")

            return card

    def update_card_styles(self):
        active_type = self.active_chart_var.get()
        for child in self.cards_frame.winfo_children():
            if isinstance(child, ctk.CTkFrame):
                is_active = child.name == active_type
                child.configure(
                    border_color="#1E90FF" if is_active else "#2a2a2a",
                    fg_color="#162032" if is_active else "#1a1a1a"
                )

    def update_chart_with_debounce(self, *args):
        if hasattr(self, '_update_timer'):
            self.root.after_cancel(self._update_timer)

        self._update_timer = self.root.after(300, lambda: self.update_active_chart(self.viz_account_entry.get()))

    def update_active_chart(self, account_name):
        if not account_name:
            self.show_notification("Please enter an account name", "error")
            return

        try:
            chart_type = self.active_chart_var.get()
            for widget in self.chart_frame.winfo_children():
                widget.destroy()
            loading_label = ctk.CTkLabel(
                self.chart_frame,
                text="Loading...",
                font=("Arial", 14),
                text_color="white"
            )
            loading_label.pack(expand=True)
            self.chart_frame.update()
            if chart_type == "bar":
                self.show_bar_chart(account_name)
            elif chart_type == "pie":
                self.show_pie_chart(account_name)
            elif chart_type == "line":
                self.show_line_chart(account_name)

        except Exception as e:
            self.show_notification(f"Error updating chart: {str(e)}", "error")
        finally:
            if 'loading_label' in locals():
                loading_label.destroy()
