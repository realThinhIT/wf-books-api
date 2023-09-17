from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from mangum import Mangum

from app.routers import api_routers

app = FastAPI()

# Init all routers for the app
app.include_router(api_routers)

# Add CORS middleware for browser requests
app.add_middleware(CORSMiddleware, allow_origins=['*'])


# Change validation error to 400 instead of 422
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors()},
    )

# Create a handler for AWS
handler = Mangum(app, lifespan="off")
