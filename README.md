# GTA-San-Andreas-Slot-Machines-Montecarlo-Simulation
Monte Carlo simulation of the GTA San Andreas slot machine in Python: expected value, variance and balance trajectories.

## Context

The very popular Grand Theft Auto San Andreas videogame has slot machines inside the game itself.

<img width="1280" height="1024" alt="immagine" src="https://github.com/user-attachments/assets/b2b58efe-3628-4266-8a52-a52c0777b5d9" />

We are interested to see what is the expected value of the balance change, from a theorical and empirical point of view.
But before that, let's dig into how do slot machines actually work.

## Bets

You can bet $1, $5, $10, $20, or $50. For simplicity, the value is fixed on $1.

## Expected Capital Variation ($E[\Delta C]$)

The general formula for the expected capital variation per spin is:

$$E[\Delta C] = \left( \sum_{i=1}^{6} (b \cdot m_i \cdot p_i) \right) - (b \cdot l)$$

Where:
* $b = 1$ is the unit bet.
* $m_i$ is the payout multiplier for the $i$-th symbol.
* $p_i = \frac{1}{216}$ is the probability of hitting the winning combination for the $i$-th symbol.
* $l = \frac{210}{216}$ is the loss probability.

| Index ($i$) | Symbol | Multiplier ($m_i$) | Probability ($p_i$) |
| :---: | :--- | :---: | :---: |
| 1 | `cherries` | $25$ | $1/216$ |
| 2 | `grape` | $100$ | $1/216$ |
| 3 | `69` | $250$ | $1/216$ |
| 4 | `bells` | $500$ | $1/216$ |
| 5 | `1gold` | $1000$ | $1/216$ |
| 6 | `2gold` | $5000$ | $1/216$ |

#### Calculation for $b = 1$

Substituting the values into the formula:

$$E[\Delta C] = \left[ \left(1 \cdot 25 \cdot \frac{1}{216}\right) + \left(1 \cdot 100 \cdot \frac{1}{216}\right) + \left(1 \cdot 250 \cdot \frac{1}{216}\right) + \left(1 \cdot 500 \cdot \frac{1}{216}\right) + \left(1 \cdot 1000 \cdot \frac{1}{216}\right) + \left(1 \cdot 5000 \cdot \frac{1}{216}\right) \right] - \left(1 \cdot \frac{210}{216}\right)$$

Factoring out the common denominator $\frac{1}{216}$ in the summation:

$$E[\Delta C] = \frac{25 + 100 + 250 + 500 + 1000 + 5000}{216} - \frac{210}{216}$$

$$E[\Delta C] = \frac{6875}{216} - \frac{210}{216} = \frac{6665}{216} \approx +30.86$$

## Result

<img width="633" height="507" alt="immagine" src="https://github.com/user-attachments/assets/1731f584-6e0f-4159-80b6-2b176fb38b7a" />



