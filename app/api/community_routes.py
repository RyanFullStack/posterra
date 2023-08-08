from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Community, Post

community_routes = Blueprint('communities', __name__)


@community_routes.route('/')
def communities():
    """
    Query for all communities
    """
    communities = Community.query.all()
    return {'communities': [community.to_dict() for community in communities]}


@community_routes.route('/<int:id>')
def community_posts(id):
    """
    Query for all posts within a community
    """
    community = Community.query.get(id)

    return {'posts': [post.to_dict() for post in community.posts]}
