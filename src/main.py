import fastapi

from src import enpoints, middleware

app = fastapi.FastAPI()

app.include_router(enpoints.router)

app.middleware("http")(middleware.track_link_creation)
