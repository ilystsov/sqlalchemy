import uuid
from typing import List

from sqlalchemy import select

from homework.app.domain.services.interfaces.product import ProductInterface
from homework.app.domain.entities.product import Product
from homework.app.infrastructure.adapter.exceptions import ProductNotFound
from homework.app.infrastructure.models import ProductModel


class ProductAdapter(ProductInterface):
    """
    Адаптер для работы с продуктами.
    """

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def create(self, name: str, price: float) -> Product:
        """Создать продукт."""
        with self.session_factory() as session:
            product = ProductModel(
                id=uuid.uuid4(),
                name=name,
                price=price,
            )
            session.add(product)
            session.commit()
            return Product(id=product.id, name=name, price=price)

    def delete(self, id_: str) -> Product:
        """Удалить продукт."""
        with self.session_factory() as session:
            product = session.get(ProductModel, id_)  # str и uuid - sqlalchemy справится сам
            if product is None:
                raise ProductNotFound("There is no product with the specified id.")
            session.delete(product)
            session.commit()
            return Product(id=product.id, name=product.name, price=product.price)

    def get_all(self) -> List[Product]:
        """Получить все доступные продукты."""
        with self.session_factory() as session:
            statement = select(ProductModel)
            results = session.execute(statement).scalars().all()
            return [Product(id=product.id, name=product.name, price=product.price) for product in results]

    def update_name(self, id_: str, name: str) -> "Product":
        """Обновить имя продукта."""
        with self.session_factory() as session:
            product = session.get(ProductModel, id_)
            if product is None:
                raise ProductNotFound("There is no product with the specified id.")
            product.name = name
            session.commit()
            return Product(id=product.id, name=product.name, price=product.price)

    def update_price(self, id_: str, price: float) -> Product:
        """Обновить цену продукта."""
        with self.session_factory() as session:
            product = session.get(ProductModel, id_)
            if product is None:
                raise ProductNotFound("There is no product with the specified id.")
            product.price = price
            session.commit()
            return Product(id=product.id, name=product.name, price=product.price)

    def get_product_by_id(self, id_: str) -> "Product":
        with self.session_factory() as session:
            product = session.get(ProductModel, id_)
            if product is None:
                raise ProductNotFound("There is no product with the specified id.")
            return Product(id=product.id, name=product.name, price=product.price)
