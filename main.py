from prng_simulation import JavaRandomLCG
from brute_force import brute_force_seed
from attacks import fgsm_prng_attack, pgd_prng_attack
from visualize import visualize_attack_path

def main():
    original_seed = 12345
    rand = JavaRandomLCG(original_seed)
    observed_output = rand.next_int()

    print("Original Seed:", original_seed)
    print("Observed Output:", observed_output)

    recovered = brute_force_seed(observed_output)
    print("Recovered Seed:", recovered)

    fgsm_results = fgsm_prng_attack(original_seed)
    print("\nFGSM-Inspired Attack Results:")
    for seed, output in fgsm_results:
        print(f"Seed: {seed}, Output: {output}")

    pgd_path = pgd_prng_attack(original_seed)
    print("\nPGD-Inspired Attack Path:")
    for step in pgd_path:
        print(step)

    visualize_attack_path(pgd_path)

if __name__ == "__main__":
    main()
