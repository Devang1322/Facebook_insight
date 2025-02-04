# Facebook_insight
its a website which show the data of faceboob
This project is a web scraper that fetches insights from a Facebook page (given a page username), scrapes relevant data, and stores it in MongoDB. The scraper uses Selenium for scraping the Facebook page and FastAPI for serving the data via API. The application is built using Python and relies on MongoDB for storing scraped data.

#Features
Scrapes Facebook page data (e.g., page name, followers, likes, posts, comments).
Stores the scraped data in a MongoDB database.
Exposes APIs using FastAPI to retrieve Facebook page insights:
Get page data by username.
Retrieve a list of followers or posts.
Real-time scraping: If the data isn't available in the database, it will fetch the data from Facebook using Selenium
Pagination for fetching multiple posts or followers.
Postman Collection included for easy API testing.
Prerequisites
Before running the project, 
ensure you have the following installed
Python 3.x (preferably the latest version)
MongoDB (local or hosted version)
Google Chrome (with matching ChromeDriver version)
Chromedriver for Selenium
FastAPI for serving APIs
Selenium for web scraping
