import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from homework.app.presentation.mutation import Mutation
from homework.app.presentation.query import Query


def _get_graphql_app() -> GraphQL:
    """Создание схемы strawberry с параметрами."""
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQL(schema)
    return graphql_app


def get_app() -> FastAPI:
    """Создание экземпляра FastAPI"""

    graphql_app = _get_graphql_app()

    app = FastAPI()
    app.add_route('/graphql', graphql_app)
    app.add_websocket_route('/graphql', graphql_app)

    return app
