from pydantic import BaseModel, Field
from typing import List, Optional

class Page(BaseModel):
    page_name: str
    page_url: str = Field(..., alias="url")
    facebook_id: str
    profile_pic: str
    email: Optional[str]
    website: Optional[str]
    category: str
    followers_count: int = Field(..., alias="followers")
    likes_count: int = Field(..., alias="likes")
    creation_date: str

class Post(BaseModel):
    post_id: str
    content: str
    created_time: str 
    likes_count: int 
    comments_count: int 

class Follower(BaseModel):
    follower_id: str 
    name: str 
    profile_pic: str 
