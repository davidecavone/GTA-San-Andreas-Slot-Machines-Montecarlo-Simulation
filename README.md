# GTA-San-Andreas-Slot-Machines-Montecarlo-Simulation
Monte Carlo simulation of the GTA San Andreas slot machine in Python: expected value, variance and balance trajectories.

## Context

The very popular Grand Theft Auto San Andreas videogame has slot machines inside the game itself.

<img width="1280" height="1024" alt="immagine" src="https://github.com/user-attachments/assets/b2b58efe-3628-4266-8a52-a52c0777b5d9" />

We are interested to see what is the expected value of the balance change, from a theorical and empirical point of view.
But before that, let's dig into how do slot machines actually work.

## Slot machine symbols and their multipliers

Just like real life slot machines, you win if a sequence of three same symbols appears, and the prize is proportional to your bet.
The slot machine symbols are: cherries, grapes, 69, bells, 1 gold bar and 2 gold bar.
Each of these symbol has its own multiplier:
- Cherries: x25
- Grape: x100
- 69: x250
- bells: x500
- 1 gold bar: x1000
- 2 gold bar: x5000

## Bets

You can bet $1, $5, $10, $20, or $50. For simplicity, the value is fixed on $1.

## Mathematical approach

$$
\mathbb{E}[\Delta C] = \left( \sum_{i=1}^{6} b \cdot m_i \cdot p_i \right) - (b \cdot l)
$$

Where:
* $C$: current balance
* $b$: bet amount
* $m_i$: multiplier for the $i$-th symbol, where $i \in \{1, \dots, 6\}$
* $p_i$: probability of the $i$-th symbol, where $i \in \{1, \dots, 6\}$
* $l$: loss probability

## Result

<img width="633" height="507" alt="immagine" src="https://github.com/user-attachments/assets/1731f584-6e0f-4159-80b6-2b176fb38b7a" />



