from sqlalchemy import ForeignKey
from uuid import UUID
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm.collections import attribute_keyed_dict

from homework.app.infrastructure.models.base import BaseModel


class ProductModel(BaseModel):
    __tablename__ = 'products'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(default=0, nullable=False)


class CartModel(BaseModel):
    __tablename__ = 'carts'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    cart_product_associations: Mapped[dict[UUID, 'CartProductAssociationModel']] = relationship(
        back_populates='cart',
        collection_class=attribute_keyed_dict("product_id"),
    )

    products: AssociationProxy[dict[UUID, int]] = association_proxy(
        target_collection='cart_product_associations',
        attr='quantity',
        creator=lambda product_id, quantity: CartProductAssociationModel(product_id=product_id, quantity=quantity)
    )


class CartProductAssociationModel(BaseModel):
    __tablename__ = "product_cart_association"

    cart_id: Mapped[UUID] = mapped_column(ForeignKey("carts.id", ondelete="CASCADE"), primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)

    cart: Mapped[CartModel] = relationship(back_populates='cart_product_associations')
    product: Mapped[ProductModel] = relationship()
