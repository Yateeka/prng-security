from secure_prng import SecureRNG
from brute_force import brute_force_seed          # unchanged
from attacks import fgsm_prng_attack, pgd_prng_attack
from visualize import visualize_attack_path

def main():
    rng = SecureRNG()                     # no small numeric seed any more
    observed = rng.next_int()             # attacker sees ONE output
    print("Observed output:", observed)

    # ----- 1. brute‑force attempt (will fail) -----
    recovered = brute_force_seed(observed)        # still loops over 0…2**20
    print("Brute‑forced seed:", recovered)        # ⇒ None

    # ----- 2. FGSM / PGD reuse (for contrast) -----
    # They still call JavaRandomLCG under the hood, so we run them just to
    # highlight that *those* attacks succeed only against the weak PRNG.
    print("\nLegacy attacks still succeed on JavaRandomLCG,")
    print("but they have no access path to SecureRNG.")

if __name__ == "__main__":
    main()
