from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: str
    quantity: int


class Batch:
    def __init__(
        self, ref: str, sku: str, quantity: int, eta: Optional[date]
    ) -> None:
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = quantity

    def allocate(self, line: OrderLine) -> None:
        self.available_quantity -= line.quantity
