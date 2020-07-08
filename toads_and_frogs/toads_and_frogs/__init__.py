from dataclasses import dataclass
from typing import List

@dataclass
class ToadsAndFrogsRow:
    '''A row in toads and frogs. 0
    represents a blank space, 1 represents
    a Toad, -1 represents a frog.'''
    
    spaces: List[int]
    
    def __post_init__(self):
        assert set(self.spaces) == {1, 0, -1}
        
    def move(self, idx):
        direction = self.spaces[idx]
        try:
            self._move(idx, idx+direction)
            return
        except AssertionError:
            assert self.spaces[idx+direction] == -direction
        
        self._move(idx, idx+2*direction)
    
    @property
    def n_spaces(self):
        return len(self.spaces)
    
    def _move(self, start_idx, end_idx):
        assert 0 <= start_idx < self.n_spaces
        assert 0 <= end_idx < self.n_spaces
        assert self.spaces[end_idx] == 0
        assert self.spaces[start_idx] in {-1, 1}
        self.spaces[start_idx], self.spaces[end_idx] = self.spaces[end_idx], self.spaces[start_idx]