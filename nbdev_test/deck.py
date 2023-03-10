# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 1
from .card import *

# %% ../nbs/01_deck.ipynb 3
class Deck:
    def __init__(self) -> None:
        self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]
    
    def __str__(self) -> str:
        return ';'.join(map(str(self.cards)))

    def __repr__(self) -> str:
        return ';'.join(map(str, self.cards))
