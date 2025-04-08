class JavaRandomLCG:
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)
        self.multiplier = 0x5DEECE66D
        self.addend = 0xB
        self.mask = (1 << 48) - 1

    def next(self, bits):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed >> (48 - bits)

    def next_int(self):
        return self.next(32)
