from fastapi import APIRouter
from app.database import posts_collection

router = APIRouter()

@router.get("/pages/{username}/posts")
def get_posts(username: str):
    posts = list(posts_collection.find({"username": username}))
    return posts
