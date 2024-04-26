from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from homework.app.domain.entities.product import Product


class ProductInterface(Protocol):
    """Интерфейс для работы с продуктами."""

    @abstractmethod
    def create(self, name: str, price: float) -> "Product":
        """Создать продукт."""

    @abstractmethod
    def delete(self, id_: str) -> "Product":
        """Удалить продукт."""

    @abstractmethod
    def get_all(self) -> List["Product"]:
        """Получить все доступные продукты."""

    @abstractmethod
    def update_name(self, id_: str, name: str) -> "Product":
        """Обновить имя продукта."""

    @abstractmethod
    def update_price(self, id_: str, price: float) -> "Product":
        """Обновить цену продукта."""

    @abstractmethod
    def get_product_by_id(self, id_: str) -> "Product":
        """Получить продукт по его id."""
