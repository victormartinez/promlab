from typing import Any, Dict

from fastapi import FastAPI

from promlab.resources import router


def create_application() -> FastAPI:
    application = FastAPI()
    configure_healthcheck(application)
    configure_routes(application)
    configure_telemetry(application)
    return application


def configure_routes(application: FastAPI) -> None:
    application.include_router(router)


def configure_telemetry(application: FastAPI) -> None:
    pass


def configure_healthcheck(app: FastAPI) -> None:
    @app.get("/")
    async def healthcheck() -> Dict[str, Any]:
        return {
            "application": "WebLab Service",
            "healthy": True,
        }


app = create_application()
