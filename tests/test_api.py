import pytest 
from fastapi.testclient import TestClient 
from app.main import app 

client = TestClient(app)

def test_get_page():
    response = client.get("/api/pages/boat.lifestyle")
    assert response.status_code in [200, 404]

def test_get_posts():
    response = client.get("/api/pages/boat.lifestyle/posts")
    assert response.status_code in [200, 404]

def test_get_followers():
    response = client.get("/api/pages/boat.lifestyle/followers")
    assert response.status_code in [200, 404]
