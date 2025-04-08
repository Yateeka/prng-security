from prng_simulation import JavaRandomLCG

def brute_force_seed(observed_output, max_seed=2**20):
    for seed in range(max_seed):
        rand = JavaRandomLCG(seed)
        if rand.next_int() == observed_output:
            return seed
    return None
