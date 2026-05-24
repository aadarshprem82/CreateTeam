from fastapi import FastAPI

app = FastAPI(
    title="Cricket Management API",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "message": "Cricket API is running",
    }