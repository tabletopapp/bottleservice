from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import v1_router


def load_all_models() -> None:
    """Load all models so that they are registered with SQLAlchemy.
    Import them for the app as well so that they are registered with FastAPI.
    """

    # Converts absolute path of a file ending in `models.py` to an import
    def path_to_import(p):
        return p[p.find("app") :].split(".py")[0].replace("/", ".")

    # Sort to get rid of circular imports
    model_paths = Path(__file__).parent.glob("api/v1/**/models.py")
    model_paths = list(model_paths)
    model_paths.sort()

    for p in model_paths:
        import_str = path_to_import(str(p))
        __import__(import_str)


app = FastAPI(
    title="bottle_service",
    description="The TableTop Backend",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

load_all_models()

allowed_origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    v1_router,
    prefix="/v1",
    tags=["v1"],
)


def get_app() -> FastAPI:
    app = FastAPI(
        title="bottle_service",
        description="The TableTop Backend",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
    )

    load_all_models()

    allowed_origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        v1_router,
        prefix="/v1",
        tags=["v1"],
    )

    return app
