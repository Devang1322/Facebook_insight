from fastapi import FastAPI
from app.routes import pages

app = FastAPI()

# Make sure the pages router is included
app.include_router(pages.router)

for route in app.routes:
    print(f"Route: {route.path} - Methods: {route.methods}")

@app.get("/")
def home():
    return {"message": "Facebook Insights API"}
