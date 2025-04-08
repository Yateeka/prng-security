from prng_simulation import JavaRandomLCG

def fgsm_prng_attack(seed, epsilon=1):
    variations = [seed + epsilon, seed - epsilon]
    results = []
    for var_seed in variations:
        rand = JavaRandomLCG(var_seed)
        results.append((var_seed, rand.next_int()))
    return results

def pgd_prng_attack(start_seed, steps=10, step_size=1):
    current_seed = start_seed
    path = [(current_seed, JavaRandomLCG(current_seed).next_int())]
    for _ in range(steps):
        candidates = [
            current_seed + step_size,
            current_seed - step_size
        ]
        best = max(candidates, key=lambda s: JavaRandomLCG(s).next_int())
        current_seed = best
        path.append((current_seed, JavaRandomLCG(current_seed).next_int()))
    return path
