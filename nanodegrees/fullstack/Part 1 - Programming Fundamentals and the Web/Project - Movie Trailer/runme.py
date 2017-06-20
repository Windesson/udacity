# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:23:29 2017

The main file to run the movies website.

@author: Almeida
"""
import media
import moviedb
import fresh_tomatoes 

# hold a list of object type media.Movies. 
movies = []

# loop throught each movie in the database.
for m in moviedb.data:
    movies.append(media.Movie(m))

# creat static HTML file and display movies.
fresh_tomatoes.open_movies_page(movies)