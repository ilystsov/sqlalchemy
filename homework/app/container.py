from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework.app.infrastructure.adapter.cart import CartAdapter
from homework.app.infrastructure.adapter.product import ProductAdapter
from homework.app.infrastructure.config import pg_string
from homework.app.settings.app import AppSettings


class AppContainer(DeclarativeContainer):
    database_engine = Singleton(create_engine, url=pg_string)
    session_factory = Singleton(sessionmaker, bind=database_engine)

    product_adapter: Singleton["ProductAdapter"] = Singleton(
        ProductAdapter, session_factory=session_factory
    )  # везде должны использовать один адаптер, чтобы было персистентное хранилище
    cart_adapter: Singleton["CartAdapter"] = Singleton(CartAdapter, session_factory=session_factory)
    app_settings: Singleton["AppSettings"] = Singleton(AppSettings)


APP_CONTAINER = AppContainer()
