from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Community, Post

post_routes = Blueprint('posts', __name__)


@post_routes.route('/')
def posts():
    """
    Query for all posts
    """
    posts = Post.query.all()

    if not posts:
        return {'message': 'no posts found'}

    return {'posts': [post.to_dict() for post in posts]}

@post_routes.route('/<int:id>')
def post(id):
    """
    Query for single post
    """
    post = Post.query.get(id)

    if not post:
        return {'message': 'post not found'}

    return post.to_dict()
