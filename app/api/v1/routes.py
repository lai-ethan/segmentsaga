from fastapi import APIRouter
from app.api.v1.customers import router as customers_router 

# --- Create the main API router object ---
router = APIRouter()

# mount customer endpoints
router.include_router(customers_router)

@router.get("/")
def read_root():
    return {"message": "Welcome to SegmentSaga API"}
@router.get("/health")
def health_check():
    return {"status": "OK"}