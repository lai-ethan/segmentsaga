from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(title="SegmentSaga")

app.include_router(router)