from fastapi import FastAPI, APIRouter

from app.routers import api_routers

app = FastAPI()

# Init all routers for the app
app.include_router(api_routers)
