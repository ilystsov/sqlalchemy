# Определение класса корневой мутации
from typing import Optional

import strawberry

from homework.app.container import APP_CONTAINER
from homework.app.domain.entities.cart import Cart
from homework.app.domain.entities.product import Product, ProductInput
from homework.app.infrastructure.adapter.exceptions import ProductNotFound, CartNotFound


@strawberry.type
class Mutation:
    # Метод для создания продукта
    @strawberry.mutation
    def create_product(self, product_info: ProductInput) -> Product:
        """Логика создания продукта"""
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.create(name=product_info.name,
                                      price=float(product_info.price) if product_info.price else 0)

    @strawberry.mutation
    def update_product_info(self, id_: str, product_info: ProductInput) -> Optional[Product]:
        """Обновить данные о продукте."""
        product_adapter = APP_CONTAINER.product_adapter()
        try:
            product_adapter.update_name(id_, product_info.name)
            product_adapter.update_price(id_, product_info.price)
        except ProductNotFound:
            return None
        updated_product = product_adapter.get_product_by_id(id_)
        return updated_product

    @strawberry.mutation
    def create_cart(self) -> Cart:
        """Логика создания корзины"""
        cart_adapter = APP_CONTAINER.cart_adapter()
        return cart_adapter.create()

    @strawberry.mutation
    def add_to_cart(self, cart_id: str, product_name: str, quantity: int) -> str:
        """Метод добавления товара в корзину"""
        product_adapter = APP_CONTAINER.product_adapter()
        cart_adapter = APP_CONTAINER.cart_adapter()
        product_id: Optional[str] = None
        all_products = product_adapter.get_all()
        for product in all_products:                # пока считаем, что имя
            if product.name == product_name:        # однозначно задаёт ID.
                product_id = product.id
                break
        try:
            cart_adapter.add_product(cart_id, product_id)
            cart_adapter.change_product_quantity(cart_id, product_id, quantity)
        except (CartNotFound, ProductNotFound) as e:
            return f'Error occurred: {str(e)}'
        return f'Product {product_name} added to cart {cart_id}'