# main.py

from utils.movie_processor import fetch_movies, process_movies
from utils.graph_builder import build_movie_graph, visualize_graph

# Fetch and process movies from MongoDB
movies = fetch_movies(genre_filter="Action", min_year=2010)
process_movies(movies)

# Build and visualize graph
movie_graph = build_movie_graph(movies)
visualize_graph(movie_graph)
