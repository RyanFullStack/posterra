from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, PostVote


vote_routes = Blueprint('votes', __name__)


@vote_routes.route('/<int:id>')
def votes(id):
    """
    Query for all votes on a post
    """
    votes = PostVote.query.filter(PostVote.post_id == id).all()

    if not votes:
        return {'message': 'no votes found'}

    return {'votes': [vote.to_dict() for vote in votes]}
