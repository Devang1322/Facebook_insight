from fastapi import APIRouter, HTTPException
from app.database import pages_collection
from app.scraper import scrape_facebook_page

router = APIRouter()

@router.get("/pages/{username}")
def get_page(username: str):
    print(f"Fetching page data for: {username}")  
    
    page = pages_collection.find_one({"username": username})
    if page:
        return page

    print(f"Scraping data for: {username}")  
    page_data = scrape_facebook_page(username)
    
    print(f"Scraped page data: {page_data}")  
    if page_data:
        pages_collection.insert_one(page_data)
        return page_data

    raise HTTPException(status_code=404, detail="Page not found")
