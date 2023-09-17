from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mangum import Mangum

from app.routers import api_routers

app = FastAPI()

# Init all routers for the app
app.include_router(api_routers)

# Add CORS middleware for browser requests
app.add_middleware(CORSMiddleware, allow_origins=['*'])

# Create a handler for AWS
handler = Mangum(app, lifespan="off")
