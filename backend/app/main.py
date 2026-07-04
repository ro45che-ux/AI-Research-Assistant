from fastapi import FastAPI
from app.api.upload import router as upload_router
app = FastAPI(
    title="AI Research Assistant",
    description="Backend API for a Production RAG Application",
    version="1.0.0"
)
app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Research Assistant 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }