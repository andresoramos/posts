from fastapi import FastAPI
from app import create_app

if __name__ == '__main__':
    app = create_app()
    # Run the FastAPI application
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)