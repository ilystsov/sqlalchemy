import uvicorn

from homework.app.container import APP_CONTAINER
from homework.app.maker import get_app

if __name__ == '__main__':
    app = get_app()
    app_settings = APP_CONTAINER.app_settings()

    uvicorn.run(app, host=app_settings.host, port=app_settings.port)
