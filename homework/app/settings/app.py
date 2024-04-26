from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # Хост приложения
    host: str = "localhost"
    # Порт приложения
    port: int = 8000
