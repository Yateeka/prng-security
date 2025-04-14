def fgsm_secure_attack(rng, trials=2):
    """
    Dummy ‘attack’ for a cryptographic RNG.
    It just samples a few outputs; no gradient trick can work here.
    """
    return [rng.next_int() for _ in range(trials)]
