import random
import matplotlib.pyplot as plt
import numpy as np

# Initialize the balance for the simulation
balance = 1000

# Number of simulations to run
num_games = 100
num_simulations = 500

# Define the bet amount for each spin
bet_amount = 1

# Define the symbols and their corresponding multiplier values and probabilities
symbols = {
    "ciliegie": (25, 1/216),
    "uva": (100, 1/216),
    "69": (250, 1/216),
    "campane": (500, 1/216),
    "1oro": (1000, 1/216),
    "2oro": (5000, 1/216),
}

# Define the loss probability for each spin
loss_probability = 1 - sum(prob for _, prob in symbols.values())

# Define the expected balance variance after a single spin
expected_value = sum(bet_amount * multiplier * prob for multiplier, prob in symbols.values()) - (bet_amount * loss_probability)

# Simulate the slot machine spin. For simplicity, it's assumed that every symbol has the same probability of appearing.
# Return True if the player wins, False otherwise.
def spin_slot_machine():
    symbol1 = random.choice(list(symbols.keys()))
    symbol2 = random.choice(list(symbols.keys()))
    symbol3 = random.choice(list(symbols.keys()))

    
    if symbol1 == symbol2 == symbol3:
        spin_result = (True, symbol1)
    else:
        spin_result = (False, symbol1)
    return spin_result

# Create balance vs iteration plot
end_balances = []
fig = plt.figure()
plt.xlabel("Iteration")
plt.ylabel("Balance [$]")
plt.xlim(0, num_games)
plt.yscale("log")
plt.xticks(np.arange(0, num_games + 1, 100))

# Run the simulation for the specified number of iterations
def simulate_game():
    history = [balance]
    for i in range(num_games):
        win, symbol = spin_slot_machine()
        if win:
            history.append(history[-1] + bet_amount * symbols[symbol][0])
        else:
            history.append(history[-1] - bet_amount)

    end_balances.append(history[-1])
    plt.plot(range(num_games + 1), history)


# Run the simulation multiple times to observe the balance over iterations
for i in range(num_simulations):
    simulate_game()

plt.title(f"GTA San Andreas Slot Machine ({num_simulations} simulation runs)")
plt.show()


