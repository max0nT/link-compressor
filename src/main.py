import fastapi

from src import enpoints

app = fastapi.FastAPI()

app.include_router(enpoints.router)
