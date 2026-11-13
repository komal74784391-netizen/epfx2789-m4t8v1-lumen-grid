"""Column packing engine for Lumen Grid."""

from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass
class Card:
    key: str
    height: int
    payload: dict = field(default_factory=dict)


def pack(cards: Iterable[Card], columns: int = 3, gap: int = 16) -> List[List[Card]]:
    """Distribute cards over the shortest column available."""
    if columns < 1:
        raise ValueError("columns must be >= 1")
    buckets: List[List[Card]] = [[] for _ in range(columns)]
    heights = [0 for _ in range(columns)]
    for card in cards:
        target = min(range(columns), key=lambda i: heights[i])
        buckets[target].append(card)
        heights[target] += card.height + gap
    return buckets
