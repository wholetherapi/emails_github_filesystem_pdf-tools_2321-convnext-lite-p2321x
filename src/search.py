"""Latency-aware architecture search used for the WACV tables."""

from dataclasses import dataclass


@dataclass
class SearchSpace:
    depths: tuple = (2, 3, 4)
    widths: tuple = (48, 64, 80)
    expansion: int = 4

    def candidates(self):
        for depth in self.depths:
            for width in self.widths:
                yield {"depth": depth, "width": width, "expansion": self.expansion}
