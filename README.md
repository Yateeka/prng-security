# Breaking and Defending PRNGs: An Adversarial Approach

This project simulates Java’s Linear Congruential Generator (LCG) and demonstrates brute-force and adversarial (FGSM & PGD-inspired) attacks on it.

## Files

- `prng_simulation.py`: Java-style PRNG generator using LCG.
- `brute_force.py`: Script to brute-force seed recovery.
- `attacks.py`: Implements FGSM and PGD-style attacks.
- `visualize.py`: Plot the attack paths.
- `main.py`: Runs all logic and displays results.
- `requirements.txt`: Dependencies.

## To Run

```bash
python -m venv venv
source venv/bin/activate      # Or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python main.py
