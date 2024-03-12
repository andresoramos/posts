from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as routes_router

def create_app():
    app = FastAPI()

    # Allow Cross-Origin Resource Sharing (CORS)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

    # Register routes
    app.include_router(routes_router)

    return app

# Define DEBUG variable here
DEBUG = True if __name__ == "__main__" else False
