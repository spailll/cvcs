import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BlackjackCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack Bet Spreading Calculator")
        self.geometry("2560x1200")
        self.setup_ui()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        self.quit()
        
    def setup_ui(self):
        self.decks_var = tk.StringVar()
        self.players_var = tk.StringVar()
        self.rules_var = tk.StringVar()
        self.rounds_var = tk.StringVar()
        self.spread_var = tk.StringVar()
        self.bankroll_var = tk.StringVar()
        self.trip_bankroll_var = tk.StringVar()
        self.hours_var = tk.StringVar()
        self.min_chip_size_var = tk.StringVar()
        self.min_bet_var = tk.StringVar()
        self.goal_win_var = tk.StringVar()
        self.hours_day_var = tk.StringVar()
        self.expenses_day_var = tk.StringVar()
        self.count_vars = [tk.StringVar() for _ in range(21)]  # Variables for the count table

        # Rules Frame
        rules_frame = ttk.LabelFrame(self, text="Rules", style="Custom.TLabelframe")
        rules_frame.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        rules_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(rules_frame, text="Decks:").grid(column=0, row=0)
        ttk.Entry(rules_frame, textvariable=self.decks_var).grid(column=1, row=0)
        
        ttk.Label(rules_frame, text="Players:").grid(column=0, row=1)
        ttk.Entry(rules_frame, textvariable=self.players_var).grid(column=1, row=1)
        
        ttk.Label(rules_frame, text="Rules:").grid(column=0, row=2)
        ttk.Entry(rules_frame, textvariable=self.rules_var).grid(column=1, row=2)

        ttk.Label(rules_frame, text="Penetr.:").grid(column=0, row=3)
        ttk.Entry(rules_frame, textvariable=tk.StringVar()).grid(column=1, row=3)

        # Betting Frame
        betting_frame = ttk.LabelFrame(self, text="Betting", style="Custom.TLabelframe")
        betting_frame.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")
        betting_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(betting_frame, text="Rounds/Hour:").grid(column=0, row=0)
        ttk.Entry(betting_frame, textvariable=self.rounds_var).grid(column=1, row=0)
        
        ttk.Label(betting_frame, text="Spread:").grid(column=0, row=1)
        ttk.Entry(betting_frame, textvariable=self.spread_var).grid(column=1, row=1)

        # Bankroll/Risk Frame
        bankroll_frame = ttk.LabelFrame(self, text="Bankroll/Risk", style="Custom.TLabelframe")
        bankroll_frame.grid(column=2, row=0, padx=10, pady=10, sticky="nsew")
        bankroll_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(bankroll_frame, text="Bankroll:").grid(column=0, row=0)
        ttk.Entry(bankroll_frame, textvariable=self.bankroll_var).grid(column=1, row=0)
        
        ttk.Label(bankroll_frame, text="Trip Bankroll:").grid(column=0, row=1)
        ttk.Entry(bankroll_frame, textvariable=self.trip_bankroll_var).grid(column=1, row=1)
        
        ttk.Label(bankroll_frame, text="Hours:").grid(column=0, row=2)
        ttk.Entry(bankroll_frame, textvariable=self.hours_var).grid(column=1, row=2)

        # Simplify Frame
        simplify_frame = ttk.LabelFrame(self, text="Simplify", style="Custom.TLabelframe")
        simplify_frame.grid(column=3, row=0, padx=10, pady=10, sticky="nsew")
        simplify_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(simplify_frame, text="Minimum Chip Size:").grid(column=0, row=0)
        ttk.Entry(simplify_frame, textvariable=self.min_chip_size_var).grid(column=1, row=0)
        
        ttk.Label(simplify_frame, text="Minimum Bet:").grid(column=0, row=1)
        ttk.Entry(simplify_frame, textvariable=self.min_bet_var).grid(column=1, row=1)
        
        ttk.Checkbutton(simplify_frame, text="Manually Adjust Min Bet").grid(column=0, row=2, columnspan=2)
        ttk.Checkbutton(simplify_frame, text="Freeze Custom Bets").grid(column=0, row=3, columnspan=2)

        # Expected Results Frame
        expected_results_frame = ttk.LabelFrame(self, text="Expected Results", style="Custom.TLabelframe")
        expected_results_frame.grid(column=4, row=0, padx=10, pady=10, sticky="nsew")
        expected_results_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(expected_results_frame, text="Win:").grid(column=0, row=0)
        ttk.Entry(expected_results_frame, textvariable=tk.StringVar(), state='readonly').grid(column=1, row=0)
        
        ttk.Label(expected_results_frame, text="Prob.").grid(column=0, row=1)
        ttk.Label(expected_results_frame, text="Results").grid(column=1, row=1)

        for i in range(3):
            ttk.Label(expected_results_frame, text="66.7").grid(column=0, row=i+2)
            ttk.Entry(expected_results_frame, textvariable=tk.StringVar(), state='readonly').grid(column=1, row=i+2)

        # Risk Frame
        risk_frame = ttk.LabelFrame(self, text="Risk", style="Custom.TLabelframe")
        risk_frame.grid(column=4, row=1, padx=10, pady=10, sticky="nsew")
        risk_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(risk_frame, text="Goal to Win:").grid(column=0, row=0, columnspan=2)
        ttk.Entry(risk_frame, textvariable=self.goal_win_var).grid(column=2, row=0)
        
        ttk.Label(risk_frame, text="Goal").grid(column=0, row=1)
        ttk.Label(risk_frame, text="Hours").grid(column=1, row=1)
        ttk.Label(risk_frame, text="Risk").grid(column=2, row=1)
        ttk.Label(risk_frame, text="Inf").grid(column=0, row=2)
        ttk.Label(risk_frame, text="10").grid(column=1, row=2)
        ttk.Label(risk_frame, text="Inf").grid(column=0, row=3)
        ttk.Label(risk_frame, text="Inf").grid(column=1, row=3)
        ttk.Label(risk_frame, text="500").grid(column=0, row=4) # GOAL TO WIN, not 500
        ttk.Label(risk_frame, text="10").grid(column=1, row=4)
        ttk.Label(risk_frame, text="500").grid(column=0, row=5)
        ttk.Label(risk_frame, text="Inf").grid(column=1, row=5)

        for i in range(4):
            ttk.Entry(risk_frame, textvariable=tk.StringVar(), state='readonly').grid(column=2, row=i+2)

        # Goals Frame
        goals_frame = ttk.LabelFrame(self, text="Goals", style="Custom.TLabelframe")
        goals_frame.grid(column=4, row=2, padx=10, pady=10, sticky="nsew")
        goals_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(goals_frame, text="Goal to Win:").grid(column=0, row=0)
        ttk.Entry(goals_frame, textvariable=self.goal_win_var).grid(column=1, row=0)

        ttk.Label(goals_frame, text="Hours").grid(column=0, row=1)
        ttk.Label(goals_frame, text="Odds of Success").grid(column=1, row=1)
        ttk.Label(goals_frame, text="5").grid(column=0, row=2)
        ttk.Label(goals_frame, text="10").grid(column=0, row=3)
        ttk.Label(goals_frame, text="20").grid(column=0, row=4)
        ttk.Label(goals_frame, text="INF").grid(column=0, row=5)

        for i in range(4):
            ttk.Entry(goals_frame, textvariable=tk.StringVar(), state='readonly').grid(column=1, row=i+2)
        # Hours to Gain Frame
        hours_to_gain_frame = ttk.LabelFrame(self, text="Hours to Gain", style="Custom.TLabelframe")
        hours_to_gain_frame.grid(column=4, row=3, padx=10, pady=10, sticky="nsew")
        hours_to_gain_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(hours_to_gain_frame, text="Hours/Day:").grid(column=0, row=0)
        ttk.Entry(hours_to_gain_frame, textvariable=self.hours_day_var).grid(column=1, row=0, columnspan=2)
        
        ttk.Label(hours_to_gain_frame, text="Expenses/Day:").grid(column=0, row=1)
        ttk.Entry(hours_to_gain_frame, textvariable=self.expenses_day_var).grid(column=1, row=1, columnspan=2)

        ttk.Label(hours_to_gain_frame, text="Gain").grid(column=0, row=2)
        ttk.Label(hours_to_gain_frame, text="Hours").grid(column=1, row=2)
        ttk.Label(hours_to_gain_frame, text="Days").grid(column=2, row=2)
        ttk.Label(hours_to_gain_frame, text="25%").grid(column=0, row=3)
        ttk.Label(hours_to_gain_frame, text="50%").grid(column=0, row=4)
        ttk.Label(hours_to_gain_frame, text="100%").grid(column=0, row=5)
        ttk.Label(hours_to_gain_frame, text="200%").grid(column=0, row=6)

        for i in range(4):
            ttk.Entry(hours_to_gain_frame, textvariable=tk.StringVar(), state='readonly', width=10).grid(column=1, row=i+3)
            ttk.Entry(hours_to_gain_frame, textvariable=tk.StringVar(), state='readonly', width=10).grid(column=2, row=i+3)


        # Count Table Frame
        count_table_frame = ttk.LabelFrame(self, text="Count Table", style="Custom.TLabelframe")
        count_table_frame.grid(column=0, row=1, padx=10, pady=10, sticky="nsew", columnspan=2, rowspan=3)
        count_table_frame.configure(borderwidth=2, relief="solid")
        
        ttk.Label(count_table_frame, text="Count").grid(column=0, row=0)
        ttk.Label(count_table_frame, text="Freq").grid(column=1, row=0)
        ttk.Label(count_table_frame, text="W/L").grid(column=2, row=0)
        ttk.Label(count_table_frame, text="StD").grid(column=3, row=0)
        ttk.Label(count_table_frame, text="Optimal Bets").grid(column=4, row=0)
        ttk.Label(count_table_frame, text="Custom Bets").grid(column=5, row=0)
        
        for i in range(21):
            ttk.Entry(count_table_frame, textvariable=self.count_vars[i],  state='readonly', width=5).grid(column=0, row=i+1)
            ttk.Entry(count_table_frame, textvariable=tk.StringVar(), state='readonly', width=5).grid(column=1, row=i+1)
            ttk.Entry(count_table_frame, textvariable=tk.StringVar(), state='readonly',  width=5).grid(column=2, row=i+1)
            ttk.Entry(count_table_frame, textvariable=tk.StringVar(), state='readonly',  width=5).grid(column=3, row=i+1)
            ttk.Entry(count_table_frame, textvariable=tk.StringVar(), state='readonly',  width=5).grid(column=4, row=i+1)
            ttk.Entry(count_table_frame, textvariable=tk.StringVar(), width=5).grid(column=5, row=i+1)

        # Penetration Charts and Results
        penetration_frame = ttk.LabelFrame(self, text="Penetration Charts", style="Custom.TLabelframe")
        penetration_frame.grid(column=2, row=1, columnspan=2, rowspan=2, padx=10, pady=10, sticky="nsew")
        penetration_frame.configure(borderwidth=2, relief="solid")

        penetration_chart_label = ttk.Label(penetration_frame, text="Penetration Chart")
        penetration_chart_label.grid(column=0, row=0)

        fig3, ax3 = plt.subplots(figsize=(10, 4))
        ax3.plot([1, 2, 3, 4], [10, 5, 2, 4])
        self.penetration_canvas = FigureCanvasTkAgg(fig3, master=penetration_frame)
        self.penetration_canvas.draw()
        self.penetration_canvas.get_tk_widget().grid(column=0, row=1)

        # Graph Area
        graph_frame = ttk.Frame(self)
        graph_frame.grid(column=3, row=3, padx=10, pady=10, sticky="nsew")
        
        graph_label = ttk.Label(graph_frame, text="Graph", style="Custom.TLabel")
        graph_label.grid(column=0, row=1)
        
        # Placeholder graph
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        mu = 0
        sigma = 1
        for i in range(1, 4): 
            ax2.axvline(x=mu + i*sigma, color='r', linestyle='--')
            ax2.axvline(x=mu - i*sigma, color='r', linestyle='--')
        ax2.set_xlim([mu -3.5*sigma, mu + 3.5*sigma])
        ax2.set_title("Actual Results Chart")

        self.graph_canvas = FigureCanvasTkAgg(fig2, master=graph_frame)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().grid(column=0, row=1)

        # Actual Results Frame
        actual_results_frame = ttk.LabelFrame(self, text="Actual Results", style="Custom.TLabelframe")
        actual_results_frame.grid(column=2, row=3, padx=10, pady=10, sticky="nsew")
        actual_results_frame.configure(borderwidth=2, relief="solid")

        ttk.Label(actual_results_frame, text="Actual Result:").grid(column=0, row=0)
        ttk.Label(actual_results_frame, text="").grid(column=1, row=0)  # Placeholder for Actual Result

        ttk.Label(actual_results_frame, text="Expected:").grid(column=2, row=0)
        ttk.Label(actual_results_frame, text="").grid(column=3, row=0)  # Placeholder for Expected

        ttk.Label(actual_results_frame, text="Std. Dev.:").grid(column=0, row=1)
        ttk.Label(actual_results_frame, text="").grid(column=1, row=1)  # Placeholder for Std. Dev.

        ttk.Label(actual_results_frame, text="Probability:").grid(column=2, row=1)
        ttk.Label(actual_results_frame, text="").grid(column=3, row=1)  # Placeholder for Probability

        # Output Frame
        output_frame = ttk.LabelFrame(self, text="Outputs", style="Custom.TLabelframe")
        output_frame.grid(column=0, row=4, columnspan=5, padx=10, pady=10, sticky="nsew")
        output_frame.configure(borderwidth=2, relief="solid")

        output_labels = [
            "Avg Bet:", "EV:", "Win/Rd:", "Win/Hr:", "Round/Hr:",
            "Win/Hr:", "Round/Hr:", "RoR:", "StD:",
            "SCORE:", "CE:", "CE/WR:", "DI:", "SD:", "Variance:"
        ]

        ttk.Label(output_frame, text="Optimal").grid(column=0, row=1, sticky="w")
        ttk.Label(output_frame, text="Custom").grid(column=0, row=2, sticky="w")


        for i, label in enumerate(output_labels):
            ttk.Label(output_frame, text=label).grid(column=i + 1, row=0, sticky="w")
            ttk.Entry(output_frame, textvariable=tk.StringVar(), state='readonly', width=10).grid(column=i + 1, row=1)
            ttk.Entry(output_frame, textvariable=tk.StringVar(), state='readonly', width=10).grid(column=i + 1, row=2)

        # Calculate Button
        ttk.Button(self, text="Calculate", command=self.update_results).grid(column=0, row=5, padx=10, pady=10, sticky="nsew", columnspan=5)

    def update_results(self):
        # Placeholder logic for calculations
        self.ev_label.config(text="Expected Value: ...")
        self.risk_label.config(text="Risk of Ruin: ...")

if __name__ == "__main__":
    # Define custom styles
    style = ttk.Style()
    style.configure("Custom.TLabelframe", background="#f0f0f0", foreground="black", font=("Helvetica", 10))
    style.configure("Custom.TLabel", background="#f0f0f0", foreground="black", font=("Helvetica", 10))

    app = BlackjackCalculatorApp()
    app.mainloop()
