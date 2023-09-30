from typing import Any, Dict

from prometheus_client import make_asgi_app
from fastapi import FastAPI

from promlab.resources import router
from prometheus_fastapi_instrumentator import Instrumentator


def create_application() -> FastAPI:
    application = FastAPI()
    configure_healthcheck(application)
    configure_routes(application)
    configure_telemetry(application)
    return application


def configure_routes(application: FastAPI) -> None:
    application.include_router(router)


def configure_telemetry(application: FastAPI) -> None:
    metrics_app = make_asgi_app()
    application.mount("/metrics", metrics_app)
    Instrumentator().instrument(application).expose(application)




def configure_healthcheck(app: FastAPI) -> None:
    @app.get("/")
    async def healthcheck() -> Dict[str, Any]:
        return {
            "application": "WebLab Service",
            "healthy": True,
        }


app = create_application()
