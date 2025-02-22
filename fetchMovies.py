# utils/movie_processor.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

# MongoDB Connection
client = MongoClient(mongo_uri)
db = client['sample_mflix']
collection = db['movies']

# Function to fetch movie data based on specific criteria
def fetch_movies(genre_filter=None, min_year=2000):
    query = {"year": {"$gte": min_year}}
    if genre_filter:
        query["genres"] = genre_filter
    
    movies = list(collection.find(query, {"title": 1, "genres": 1, "year": 1, "directors": 1, "_id": 0}))
    return movies

# Example of processing and printing movie info
def process_movies(movies):
    for movie in movies:
        title = movie.get("title")
        year = movie.get("year")
        genres = movie.get("genres")
        directors = movie.get("directors")
        print(f"Title: {title} | Year: {year} | Genres: {genres} | Directors: {directors}")
