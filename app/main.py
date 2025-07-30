from fastapi import FastAPI
from app.api.v1.routes import router

# Create an instance of FastAPI
# This is the main entry point for the FastAPI application
app = FastAPI(title="SegmentSaga")

# Include the router from the app.api.v1.routes module
# This allows the application to handle requests defined in the router
# The router contains the API endpoints and their corresponding handlers
app.include_router(router)