from fastapi import APIRouter, HTTPException, Depends
from app.database import db 
from app.models import Page, Post, Follower 
from app.scraper import scrape_facebook_page

router = APIRouter()

@router.get("/api/pages/{username}", response_model=Page)
async def get_page(username: str):
    page = db.pages.find_one({"page_url": f"https://www.facebook.com/{username}"})
    
    if not page:
        page_data = scrape_facebook_page(username)
        
        if not page_data:
            raise HTTPException(status_code=404, detail="Page not found")
        
        db.pages.insert_one(page_data)
        return page_data
    
    return page

@router.get("/api/pages/{username}/posts", response_model=List[Post])
async def get_posts(username: str):
    posts = list(db.posts.find({"username": username}))
    
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    
    return posts[:15]  # Return recent posts

@router.get("/api/pages/{username}/followers", response_model=List[Follower])
async def get_followers(username: str):
    followers = list(db.followers.find({"username": username}))
    
    if not followers:
        raise HTTPException(status_code=404, detail="No followers found")
    
    return followers 
