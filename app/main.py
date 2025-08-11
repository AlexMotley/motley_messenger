from fastapi import FastAPI, APIRouter
from app.api.api import api_router


def main():
    app = FastAPI(
        title="Messanger API"
    )
    router = APIRouter(prefix="/app")
    router.include_router(api_router)

    app.include_router(router)

    return app
    
    
if __name__ == "__main__":
    main()
    