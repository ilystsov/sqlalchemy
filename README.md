## ДЗ 7. Документация о проделанной работе 
### Создание моделей объектов
Корзины и продукты связаны отношением
"many to many". Так как в одной корзине может
быть несколько одинаковых продуктов, нужно
создать [**Association Object**]('https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#association-object').

Чтобы использовать **orm** по максимуму,
будем использовать 
[**Association Proxy**]('https://docs.sqlalchemy.org/en/20/orm/extensions/associationproxy.html').
Использование этого сложного объекта позволит нам 
очень удобно доступаться к одним объектам через другие,
не используя таблицу ассоциации:
```python
cart.products.append(product)
```
### Миграции с alembic


Прежде всего запустим контейнер `postgres`:
```bash
docker run --name seminar-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```
Схема по умолчанию в Postgres -
public. Туда заносятся все таблицы,
если не объявить свою схему.
Создадим свою схему `homework`:
```python
from homework.app.infrastructure.config import SCHEMA_NAME

BaseModel = declarative_base(metadata=MetaData(schema=SCHEMA_NAME))
```
После этого нужно не забыть 
создать схему `homework`
в базе. Например, через
интерфейс **PyCharm**/**DBeaver**.

В каталоге `infrastructure` проинициализируем 
alembic:
```bash
alembic init migration
```

В `alembic.ini` укажем строку подключения к нашей БД:
```
sqlalchemy.url = postgresql://postgres:mysecretpassword@localhost/postgres
```

Если не хотим, чтобы 
таблица версий alembic
хранилась в схеме public,
укажем нашу в `env.py`:

```python
def include_name(name, type_, _):
    if type_ == "schema":
        return name in [SCHEMA_NAME]
    else:
        return True
    
def run_migrations_online() -> None:
...
    
  with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=target_metadata.schema,
            include_schemas=True,
            include_name=include_name,
        )
...
```

Импортируем модели в `models/__init__.py`.
Так alembic сможет увидеть наши модели.
> *Примечание:* также можно
было сделать эти импорты в `env.py`

Подскажем alembic'у, где искать 
скрипты, написав в `alembic.ini`
следующее:
```
script_location = homework/app/infrastructure/migration
```
После этого можно сгенерировать
миграцию! 
Из корня проекта запустим:
```bash
alembic -c homework/app/infrastructure/alembic.ini revision --autogenerate -m "init"
```
Выполним миграцию:
```bash
alembic -c homework/app/infrastructure/alembic.ini upgrade head
```
Таким образом создадутся таблицы `carts`, `products` и `product_cart_association`.

### Новые адаптеры
Будем передавать `sessionmaker` в адаптеры, а они уже будут изнутри создавать сессии:
```python
class AppContainer(DeclarativeContainer):
    database_engine = Singleton(create_engine, url=pg_string)
    session_factory = Singleton(sessionmaker, bind=database_engine)

    product_adapter: Singleton["ProductAdapter"] = Singleton(ProductAdapter, session_factory=session_factory) # везде должны использовать один адаптер, чтобы было персистентное хранилище
    cart_adapter: Singleton["CartAdapter"] = Singleton(CartAdapter, session_factory=session_factory)
    app_settings: Singleton["AppSettings"] = Singleton(AppSettings)
```

### Запуск приложения
Для запуска выполним следующую команду:
```bash
poetry run python3.10 -m homework.manage
```