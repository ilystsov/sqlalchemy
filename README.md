[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/4NzADN_L)
## Базы данных
### Типы бд
* Реляционные базы данных (**Relational databases**): Это самый распространенный тип баз данных, который использует реляционную модель данных. В реляционных базах данных данные организованы в виде таблиц, состоящих из строк (кортежей) и столбцов (атрибутов). Примеры реляционных баз данных включают MySQL, PostgreSQL, Oracle, Microsoft SQL Server.
* Объектно-ориентированные базы данных (**Object-oriented databases**): В этом типе баз данных данные организованы в объекты, которые могут иметь свои атрибуты и методы. Это позволяет хранить и работать с объектами, а не только с таблицами и строками. Примеры объектно-ориентированных баз данных включают MongoDB, Apache Cassandra.
* Графовые базы данных (**Graph databases**): Графовые базы данных предназначены для хранения и обработки данных, организованных в виде графов. Они полезны при работе с данными, где важны связи и отношения между объектами. Примеры графовых баз данных включают Neo4j, Amazon Neptune.
* Ассоциативные базы данных (**Key-value databases**): В этом типе баз данных данные хранятся в виде пар ключ-значение. Ключ уникален и используется для поиска и доступа к соответствующему значению. Примеры ключ-значение баз данных включают Redis, Riak.
* Документ-ориентированные базы данных (**Document databases**): Это тип баз данных, в котором данные хранятся в виде документов, таких как JSON или XML. Каждый документ может содержать набор полей и значений. Примеры документ-ориентированных баз данных включают MongoDB, Couchbase.

### Плюсы и минусы разных типов БД
<details>
<summary><h4>Реляционные базы данных</h4></summary>

Плюсы реляционных баз данных:

* **Структурированность данных**: Реляционные базы данных имеют четкую структуру, которая позволяет устанавливать взаимосвязи между таблицами и обеспечивает удобное хранение и доступ к данным.
* **Поддержание целостности данных**: Реляционные базы данных обеспечивают возможность задания правил для поддержания целостности данных (уникальность, ссылочная целостность, ограничения целостности) и обеспечения консистентности данных.
* **Удобный язык запросов**: SQL является стандартным языком запросов для реляционных баз данных. Он предоставляет широкие возможности для создания сложных запросов и аналитических операций.
* **Надежность и безопасность**: Реляционные базы данных имеют механизмы для обеспечения сохранности данных, резервного копирования, восстановления и контроля доступа, что делает их надежными и безопасными для хранения и обработки критически важных данных.


Минусы реляционных баз данных:

* **Фиксированная схема**: Реляционные базы данных требуют определения схемы данных заранее, и изменение схемы может быть сложным и затратным, особенно при работе с большими объемами данных.
* **Необходимость нормализации**: Хорошая производительность и структурированность данных требуют нормализации, что может привести к сложности в проектировании запросов при работе с большим количеством связанных таблиц.
* **Сложность масштабируемости**: Реляционные базы данных могут столкнуться с ограничениями производительности и масштабируемости при обработке больших объемов данных или при работе с распределенными системами.
* **Избыточность данных**: Из-за нормализации и связей между таблицами некоторые данные могут быть дублированы в нескольких таблицах, что может привести к избыточности данных и увеличению размера базы данных.
</details>

<details>
<summary><h4>Документ-ориентированные базы данных</h4></summary>

Плюсы документ-ориентированных баз данных:

* **Отсутствие схемы**: Документ-ориентированные базы данных не требуют предварительного определения схемы данных. Это означает, что вы можете легко добавлять или изменять поля в документах без необходимости модификации всей базы данных.
* **Хранение и обработка сложных данных**: Документы позволяют хранить сложные иерархические данные, включая вложенные массивы и другие документы. Это упрощает работу с данными, имеющими разные структуры или содержащими необработанные данные.
* **Высокая производительность чтения**: Документ-ориентированные базы данных обычно предоставляют быстрый доступ к данным с помощью индексирования и использования ключей или идентификаторов документов для поиска и обновления.
* **Горизонтальное масштабирование**: Документ-ориентированные базы данных обеспечивают легкое горизонтальное масштабирование (добавление дополнительных узлов), что позволяет обрабатывать большие объемы данных и обеспечивать хорошую производительность.

Минусы документ-ориентированных баз данных:

* **Ограниченные возможности сложных запросов**: Поскольку документы хранятся отдельно и не имеют прямых связей с другими документами, выполнение сложных запросов, которые включают соединения между документами или агрегатные вычисления, может быть сложным и медленным.
* **Ограниченные возможности транзакций**: Некоторые документ-ориентированные базы данных не предоставляют полноценную поддержку транзакций, особенно при работе с распределенными системами, что может быть проблемой для бизнес-процессов, требующих атомарности и согласованности данных.
* **Избыточность данных**: При использовании документов вместо отношений и связей данные могут быть дублированы в нескольких документах, что может привести к избыточности и несогласованности данных.
* **Ограниченная поддержка структуры данных**: Документ-ориентированные базы данных предлагают гибкость в хранении неструктурированных или полуструктурированных данных, но они могут быть менее подходящими для приложений, требующих сложных связей или схем данных с фиксированными отношениями.
</details>

### ДЗ
Сделать Postgresql базу данных для Graphql сервиса. 
* Разработать модели объектов в БД (2)
* Написать миграцию на alembic (2)
* Написать новый адаптеры с ProductInterface, но использующий модель из бд (3)
* Написать новый адаптеры с CartInterface, но использующий модель из бд (3)

Для выполнения задания возьмите свое решение из ДЗ 5 и дополните его. Положите исходники в директорию _homework_.

#### Рекомендации
* Python 3.9
* Придерживаться правил чистой архитектуры
* Логирование
* За основу взять СУБД Postgresql
* Основным фреймворком для работы с бд считать SQLAlchemy
* Работа с зависимостями через poetry

##### Полезные команды
Запуск postgres

```docker run --name seminar-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres```

Alembic:

```alembic init migration``` - инициализировать alembic

```alembic revision --autogenerate -m "message"``` - создать сгенерированную миграцию

```alembic upgrade head``` - запустить миграцию до последней версии

```alembic downgrade -1``` - откатить миграцию на версию назад



