from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING


if TYPE_CHECKING:
    from homework.app.domain.entities.cart import Cart


class CartInterface(Protocol):
    """Интерфейс для работы с корзиной."""

    @abstractmethod
    def create(self) -> "Cart":
        """Создать корзину."""

    @abstractmethod
    def delete(self, cart_id: str) -> "Cart":
        """Удалить корзину."""

    @abstractmethod
    def add_product(self, cart_id: str, product_id: str) -> "Cart":
        """Добавить продукт корзину."""

    @abstractmethod
    def change_product_quantity(self, cart_id: str, product_id: str, quantity: int) -> "Cart":
        """Изменить кол-во товаров в корзине."""

    @abstractmethod
    def get_cart_by_id(self, cart_id: str) -> "Cart":
        """Получить корзину по её id."""

