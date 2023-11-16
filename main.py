import uvicorn

from app.app import app
from app.config import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        # "app.app:get_app",
        app,
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        factory=True,
        timeout_keep_alive=60,
    )


if __name__ == "__main__":
    main()
