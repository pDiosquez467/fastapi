from dependencies.dependencies import init_dep
from seed import seed
from fastapi import FastAPI
from routes.routes import api_router


def main():
    init_dep()
    seed()


app = FastAPI()
app.include_router(api_router)


main()
