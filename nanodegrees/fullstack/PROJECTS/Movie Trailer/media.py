# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:22:40 2017

@author: Almeida
"""

class Movie():
    """
    This Class provides a way to store movie related information
    """
    
    def __init__(self, some_movie = {}):
        """
        This constructor takes in a dictionary need to instantiate a 
        object type Movie.
           
          title (str): The title of a movie.
          poster_image_url (str): The poster URL of a movie.
          trailer_youtube_url (str): The youtube trailer of a movie.
          
        """
        self.title = some_movie.get("title","")
        self.poster_image_url  = some_movie.get("poster_image_url","")
        self.trailer_youtube_url = some_movie.get("trailer_youtube_url","")
