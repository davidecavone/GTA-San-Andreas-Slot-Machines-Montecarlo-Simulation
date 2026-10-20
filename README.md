# GTA-San-Andreas-Slot-Machines-Montecarlo-Simulation
Monte Carlo simulation of the GTA San Andreas slot machine in Python: expected value, variance and balance trajectories.

## Context

The very popular Grand Theft Auto San Andreas videogame has slot machines inside the game itself.

<img width="1280" height="1024" alt="immagine" src="https://github.com/user-attachments/assets/b2b58efe-3628-4266-8a52-a52c0777b5d9" />

## How do slot machines work

Just like real life slot machines, you win if a sequence of three same symbols appears, and the prize is proportional to your bet.
In GTA SA, you can bet $1, $5, $10, $20, or $50.
The slot machine symbols are: cherries, grapes, 69, bells, 1 gold bar and 2 gold bar.
Each of these symbol has its own multiplier:
- Cherries: x25
- Grape: x100
- 69: x250
- bells: x500
- 1 gold bar: x1000
- 2 gold bar: x5000

# Probability
We can assume that each symbol has the same probability of appearance. This means that every symbol has the same probability of appearance, or $\frac{1}{6}$.


