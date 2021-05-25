from flask_restful import Resource, abort, fields, marshal_with

from . import movies_api

from .models import movie_crud
from .movie_parser import movie_parser, movie_fields


class Movie(Resource):
    @marshal_with(movie_fields)
    def get(self):
  
        return movie_crud.return_all_movies()

    @marshal_with(movie_fields)
    def post(self):
        args = movie_parser.parse_args()
        data = args
        if data['title']:
            return movie_crud.search_and_return_movie(data['title'])

movies_api.add_resource(Movie, '/')