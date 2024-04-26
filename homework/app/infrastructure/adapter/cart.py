import uuid

from homework.app.domain.entities.cart import Cart
from homework.app.domain.entities.product import ProductQuantity
from homework.app.domain.services.interfaces.cart import CartInterface
from homework.app.infrastructure.adapter.exceptions import CartNotFound, ProductNotFound
from homework.app.infrastructure.models import CartModel, ProductModel


class CartAdapter(CartInterface):
    """
    Адаптер для работы с корзинами продуктов.
    """

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def create(self) -> "Cart":
        """Создать корзину."""
        with self.session_factory() as session:
            cart = CartModel(
                id=uuid.uuid4(),
            )
            session.add(cart)
            session.commit()
            return Cart(id=cart.id, products=[])

    def delete(self, cart_id: str) -> "Cart":
        """Удалить корзину."""
        with self.session_factory() as session:
            cart = session.get(CartModel, cart_id)
            domain_cart = self.get_cart_by_id(cart_id)
            if cart is None:
                raise CartNotFound("There is no cart with the specified id.")
            session.delete(cart)
            session.commit()
            return domain_cart

    def add_product(self, cart_id: str, product_id: str) -> "Cart":
        """Добавить продукт в корзину."""
        with self.session_factory() as session:
            cart = session.get(CartModel, cart_id)
            product = session.get(ProductModel, product_id)

            if cart is None:
                raise CartNotFound("There is no cart with the specified id.")
            if product is None:
                raise ProductNotFound("There is no product with the specified id.")

            existing_association = next(
                (cpa for cpa in cart.cart_product_associations if cpa.product_id == product_id), None
            )
            if existing_association is not None:
                existing_association.quantity += 1
            else:
                cart.products.append(
                    product
                )  # association proxy позволяет добавить продукт в корзину настолько просто :)
            session.commit()
            return self.get_cart_by_id(cart_id)

    def change_product_quantity(self, cart_id: str, product_id: str, quantity: int) -> "Cart":
        """Изменить количество товара в корзине."""
        with self.session_factory() as session:
            cart = session.get(CartModel, cart_id)
            if cart is None:
                raise CartNotFound("There is no cart with the specified id.")
            association = next((cp for cp in cart.cart_product_associations if cp.product_id == product_id), None)
            if association is None:
                raise ProductNotFound("Product not in cart.")

            association.quantity = quantity
            session.commit()
            return self.get_cart_by_id(cart_id)

    def get_cart_by_id(self, cart_id: str) -> "Cart":
        """Получить корзину по её ID"""

        with self.session_factory() as session:
            cart = session.get(CartModel, cart_id)
            if not cart:
                raise CartNotFound("There is no cart with the specified id.")
            products_quantities = [
                ProductQuantity(product=cp.product, quantity=cp.quantity) for cp in cart.cart_product_associations
            ]
            return Cart(id=str(cart.id), products=products_quantities)
