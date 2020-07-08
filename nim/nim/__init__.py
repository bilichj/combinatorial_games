from dataclasses import dataclass

@dataclass
class NimHeap:
    n: int
    
    def move(self, m):
        assert 0 < m <= self.n
        return NimHeap(self.n-m)