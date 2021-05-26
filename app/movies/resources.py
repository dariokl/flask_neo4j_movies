from flask_restful import Resource, abort, fields, marshal_with

from . import movies_api

from .service import movie_crud
from .movie_parser import movie_parser, movie_fields


class GetMovieByTitle(Resource):
    @marshal_with(movie_fields)
    def post(self):
        args = movie_parser.parse_args()
        data = args
        title = data['title']

        return movie_crud.search_and_return_movie(title)

class Movie(Resource):
    @marshal_with(movie_fields)
    def post(self):
        args = movie_parser.parse_args()
        data = args

        return movie_crud.add_and_return_movie(data['title'], data['released'])
    
    def delete(self):
        args = movie_parser.parse_args()
        data = args

        return movie_crud.delete_movie(data['title'])
        

class GetAllMovies(Resource):
    @marshal_with(movie_fields)
    def get(self):

        return movie_crud.return_all_movies()


movies_api.add_resource(Movie, '/movie/')
movies_api.add_resource(GetMovieByTitle, '/get/movie')
movies_api.add_resource(GetAllMovies,'/')
