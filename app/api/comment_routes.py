from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Comment

comment_routes = Blueprint('comments', __name__)


@comment_routes.route('/<int:id>')
def get_comments(id):
    """
    Query for all comments on a post by id
    """
    comments = Comment.query.filter(Comment.post_id == id).all()

    if not comments:
        return {'message': 'No comments found'}

    return {'comments': [comment.to_dict() for comment in comments]}
