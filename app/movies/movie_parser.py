from flask_restful import fields, reqparse

movie_parser = reqparse.RequestParser()
movie_parser.add_argument('id', help='The video\s id.')
movie_parser.add_argument('title',type=str, required=True ,help='The video\s name.')


movie_fields = {
    'title': fields.String,
    'released': fields.Integer,
    'directors': fields.List(fields.String),
    'producers': fields.List(fields.String),
    'cast': fields.List(fields.String),

}