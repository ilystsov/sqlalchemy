# Определение класса товара
from typing import Optional

import strawberry


@strawberry.type
class Product:
    id: str
    name: str
    price: float = 0.


@strawberry.input
class ProductInput:
    """
    Хорошим тоном в GraphQL является
    использование таких Input классов.
    Отделяем сущность бизнес-логики Product от сущности,
    которую присылает пользователь.
    """
    name: str
    price: Optional[float] = None


@strawberry.type
class ProductQuantity:
    product: Product
    quantity: int
