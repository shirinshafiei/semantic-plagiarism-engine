import random
import hashlib


class MinHash:
    def __init__(self, num_perm=128, seed=42):
        self.num_perm = num_perm
        self.seed = seed

        random.seed(seed)

        self.prime = 2**61 - 1

        self.hash_funcs = [
            (
                random.randint(1, self.prime - 1),
                random.randint(0, self.prime - 1)
            )
            for _ in range(num_perm)
        ]

    def _shingle_to_int(self, shingle: str) -> int:
        return int(
            hashlib.md5(shingle.encode("utf-8")).hexdigest(),
            16
        ) % self.prime


    def _hash(self, x, a, b):
        return (a * x + b) % self.prime


    def signature(self, shingles):

        if not shingles:
            return [self.prime] * self.num_perm

        shingle_ids = [self._shingle_to_int(s) for s in shingles]

        signature = []

        for a, b in self.hash_funcs:
            min_value = float("inf")

            for x in shingle_ids:
                h = self._hash(x, a, b)
                if h < min_value:
                    min_value = h

            signature.append(min_value)

        return signature


    def similarity(self, sig1, sig2):
        if len(sig1) != len(sig2):
            raise ValueError("Signature length mismatch")

        matches = 0

        for i in range(len(sig1)):
            if sig1[i] == sig2[i]:
                matches += 1

        return matches / len(sig1)