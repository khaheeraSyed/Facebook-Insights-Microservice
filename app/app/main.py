from fastapi import FastAPI
from app.routes import pages

app = FastAPI()

app.include_router(pages.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Facebook Insights Microservice"}
