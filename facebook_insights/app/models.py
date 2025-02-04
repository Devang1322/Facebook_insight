from pydantic import BaseModel
from typing import List, Optional

class Post(BaseModel):
    post_id: str
    content: str
    likes: int
    shares: int
    comments: List[str]

class Page(BaseModel):
    id: str
    username: str
    name: str
    url: str
    profile_pic: str
    email: Optional[str]
    website: Optional[str]
    category: str
    followers: int
    likes: int
    created_at: str
    posts: List[str]
