import matplotlib.pyplot as plt

def visualize_attack_path(path):
    seeds, outputs = zip(*path)
    plt.plot(seeds, outputs, marker='o')
    plt.title("PGD-Inspired Seed Attack Path")
    plt.xlabel("Seed")
    plt.ylabel("PRNG Output")
    plt.grid(True)
    plt.show()
