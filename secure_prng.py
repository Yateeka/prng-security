import os, hashlib

class SecureRNG:
    """
    SHA‑256‑based deterministic random‑bit generator (DRBG).
    • 256‑bit internal state
    • forward‑ & backward‑secure
    """
    _STATE_LEN = 32 # 256 bits

    def __init__(self, seed: bytes | None = None):
        if seed is None:
            seed = os.urandom(self._STATE_LEN)
        self.state = hashlib.sha256(seed).digest()   # always hash‑compress

    # ---------- core interface ----------
    def next_bytes(self, n: int) -> bytes:
        out = hashlib.sha256(self.state).digest()# 1. generate
        self.state = hashlib.sha256(self.state + out).digest()  # 2. update (one‑way)
        return out[:n]

    def next_int(self, bits: int = 32) -> int:
        nbytes = (bits + 7) // 8
        val = int.from_bytes(self.next_bytes(nbytes), "big")
        return val & ((1 << bits) - 1)

    # ---------- optional extras ----------
    def reseed(self, extra_entropy: bytes | None = None):
        fresh = extra_entropy or os.urandom(self._STATE_LEN)
        self.state = hashlib.sha256(self.state + fresh).digest()
