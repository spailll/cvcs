import tkinter as tk
from tkinter import ttk
import numpy as np

def calculate_ev(true_count):
    # Simplified example calculation of EV
    return 0.5 * true_count  # This would be more complex in reality

def calculate_risk_of_ruin(bankroll, ev, variance):
    return np.exp(-2 * ev * bankroll / variance)

def update_results():
    decks = int(decks_var.get())
    penetration = float(penetration_var.get())
    rounds_per_hour = int(rounds_var.get())
    min_bet = float(min_bet_var.get())
    bankroll = float(bankroll_var.get())

    true_count = 1  # Example placeholder
    ev = calculate_ev(true_count)
    variance = 1  # Example placeholder
    risk_of_ruin = calculate_risk_of_ruin(bankroll, ev, variance)

    ev_label.config(text=f"Expected Value: {ev}")
    risk_label.config(text=f"Risk of Ruin: {risk_of_ruin}")

app = tk.Tk()
app.title("Blackjack Bet Spreading Calculator")

decks_var = tk.StringVar()
penetration_var = tk.StringVar()
rounds_var = tk.StringVar()
min_bet_var = tk.StringVar()
bankroll_var = tk.StringVar()

ttk.Label(app, text="Number of Decks:").grid(column=0, row=0)
ttk.Entry(app, textvariable=decks_var).grid(column=1, row=0)

ttk.Label(app, text="Deck Penetration:").grid(column=0, row=1)
ttk.Entry(app, textvariable=penetration_var).grid(column=1, row=1)

ttk.Label(app, text="Rounds per Hour:").grid(column=0, row=2)
ttk.Entry(app, textvariable=rounds_var).grid(column=1, row=2)

ttk.Label(app, text="Minimum Bet:").grid(column=0, row=3)
ttk.Entry(app, textvariable=min_bet_var).grid(column=1, row=3)

ttk.Label(app, text="Bankroll:").grid(column=0, row=4)
ttk.Entry(app, textvariable=bankroll_var).grid(column=1, row=4)

ttk.Button(app, text="Calculate", command=update_results).grid(column=0, row=5, columnspan=2)

ev_label = ttk.Label(app, text="Expected Value: ")
ev_label.grid(column=0, row=6, columnspan=2)

risk_label = ttk.Label(app, text="Risk of Ruin: ")
risk_label.grid(column=0, row=7, columnspan=2)

app.mainloop()
