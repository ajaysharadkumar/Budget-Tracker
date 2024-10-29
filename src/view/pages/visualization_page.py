def setup_visualization_page(self):
    page = self.pages["Visualization"]

    page.grid_columnconfigure(0, weight=1)
    page.grid_rowconfigure(3, weight=2)

    header_frame = ctk.CTkFrame(page, fg_color="transparent")
    header_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20, 5))

    header_frame.grid_columnconfigure(0, weight=1)

    title_label = ctk.CTkLabel(
        header_frame,
        text="Financial Visualization",
        font=ctk.CTkFont(family="Arial", size=-24, weight="bold"),
        text_color="white"
    )
    title_label.pack(anchor="w")

    self.cards_frame = ctk.CTkFrame(page, fg_color="transparent")
    self.cards_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=5)

    self.cards_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="card")
    self.cards_frame.grid_rowconfigure(0, minsize=100)

    self.active_chart_var = ctk.StringVar(value="bar")
    charts = [
        ("Bar Chart", "Income Distribution", self.show_bar_chart),
        ("Pie Chart", "Expense Distribution", self.show_pie_chart),
        ("Line Chart", "Income vs Expenses", self.show_line_chart)
    ]

    for i, (title, desc, command) in enumerate(charts):
        card = self.create_responsive_chart_card(
            self.cards_frame,
            title,
            desc,
            command,
            chart_type=title.split()[0].lower()
        )
        card.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

    input_frame = ctk.CTkFrame(page, fg_color="#1a1a1a")
    input_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=5)

    input_frame.grid_columnconfigure(0, weight=1)
    input_frame.grid_columnconfigure(1, weight=0)
    input_frame.grid_rowconfigure(0, minsize=70)

    self.viz_account_entry = ctk.CTkEntry(
        input_frame,
        placeholder_text="Enter Account Name",
        height=35,
        font=ctk.CTkFont(family="Arial", size=-12)
    )
    self.viz_account_entry.grid(row=0, column=0, padx=(20, 10), pady=17, sticky="ew")

    update_btn = ctk.CTkButton(
        input_frame,
        text="Update Chart",
        command=self.update_chart_with_debounce,
        height=35,
        width=120,
        font=ctk.CTkFont(family="Arial", size=-12, weight="bold")
    )
    update_btn.grid(row=0, column=1, padx=(0, 20), pady=17)

    self.chart_frame = ctk.CTkFrame(
        page,
        fg_color="#000000",
        corner_radius=15
    )
    self.chart_frame.grid(row=3, column=0, sticky="nsew", padx=20, pady=(5, 10))

    self.chart_frame.grid_columnconfigure(0, weight=2)
    self.chart_frame.grid_rowconfigure(0, weight=2)

    def on_resize(event):
        if hasattr(self, 'current_chart'):
            self.update_chart_with_debounce()

    self.chart_frame.bind('<Configure>', on_resize)


def create_figure() -> Tuple[Figure, Any]:
    """Create a figure with DPI-aware sizing"""
    fig = plt.figure(figsize=(12, 7), dpi=100)
    ax = fig.add_subplot(111)
    return fig, ax


def setup_figure_style(fig: Figure, ax: Any, title: str) -> None:
    background_color = "#000000"
    text_color = "white"
    grid_color = "gray"

    ax.set_facecolor(background_color)
    fig.patch.set_facecolor("#000000")  # Changed to black background

    ax.set_title(title,
                 fontsize=18,
                 color=text_color,
                 pad=15,
                 loc='center',
                 fontweight='bold')

    for spine in ax.spines.values():
        spine.set_color(grid_color)
        spine.set_linewidth(0.5)

    ax.grid(True,
            linestyle='--',
            alpha=0.2,
            color=grid_color,
            which='both')

    ax.tick_params(colors=text_color,
                   which='both',
                   length=5,
                   width=0.5)


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