from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import pages

app = FastAPI()

# Serve static files from the 'frontend' directory
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

app.include_router(pages.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Facebook Insights Microservice"}

