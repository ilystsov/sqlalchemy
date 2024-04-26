# Определение класса корневого запроса
from typing import List, Optional

import strawberry

from homework.app.container import APP_CONTAINER
from homework.app.domain.entities.cart import Cart
from homework.app.domain.entities.product import Product
from homework.app.infrastructure.adapter.exceptions import CartNotFound


@strawberry.type
class Query:
    @strawberry.field
    def products(self) -> List[Product]:
        """Логика для получения списка товаров"""
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.get_all()

    @strawberry.field
    def cart(self, id_: str) -> Optional[Cart]:
        """Логика для получения корзины товаров по id"""
        cart_adapter = APP_CONTAINER.cart_adapter()
        try:
            cart = cart_adapter.get_cart_by_id(id_)
        except CartNotFound:
            return None
        return cart
