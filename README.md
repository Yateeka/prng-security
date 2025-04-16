# Breaking and Defending PRNGs: An Adversarial Approach

This project investigates the vulnerabilities of Java's `java.util.Random`, which relies on a Linear Congruential Generator (LCG). Through brute-force and adversarial attacks inspired by FGSM and PGD, we demonstrate how predictable and insecure this PRNG can be when used in security-critical applications.

We then introduce and validate a cryptographically secure alternative based on SHA-256, highlighting the importance of using proper entropy sources in software security.

📄 **Full paper:** [Cyber_Security.pdf](https://github.com/Yateeka/prng-security/blob/main/Cyber_Security.pdf)

---

## 🔍 Project Overview

- Simulates Java’s internal PRNG (`java.util.Random`) using an LCG-based Python class.
- Demonstrates seed recovery via:
  - Brute-force attack
  - FGSM-inspired perturbation
  - PGD-inspired iterative attack
- Visualizes attack paths and shows the ease of predictability.
- Implements and evaluates a secure SHA-256-based PRNG alternative (`SecureRNG`).

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `prng_simulation.py` | Java-style PRNG generator using LCG logic |
| `brute_force.py` | Brute-force seed recovery script |
| `attacks.py` | Implements FGSM and PGD-style attack logic |
| `visualize.py` | Plots seed-path evolution during PGD attack |
| `main.py` | Central script to run all attacks and print results |
| `secure_rng.py` | SHA-256-based cryptographically secure PRNG |
| `main_secured.py` | Tests `SecureRNG` and compares its behavior to LCG |
| `requirements.txt` | Python dependencies |

---

## ▶️ To Run

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py                  # Runs attacks on java.util.Random clone
python main_secured.py         # Runs defense test using SecureRNG
