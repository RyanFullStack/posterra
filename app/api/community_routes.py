from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Community, Post, db
from app.forms import CommunityForm

community_routes = Blueprint('communities', __name__)


@community_routes.route('/')
def communities():
    """
    Query for all communities
    """
    communities = Community.query.all()

    if not communities:
        return {'message': 'no communities found'}

    return {'communities': [community.to_dict() for community in communities]}


@community_routes.route('/<int:id>/posts')
def community_posts(id):
    """
    Query for all posts within a community
    """
    community = Community.query.get(id)

    if not community:
        return {'message': 'community not found'}

    return {'posts': [post.to_dict() for post in community.posts]}


@community_routes.route('/new', methods=['POST'])
@login_required
def create_community():
    """
    Create a new community
    """
    form = CommunityForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        name = form.data['name']
        created_by = form.data['created_by']
        description = form.data['description']

        new_community = Community(name=name, created_by=created_by, description=description)

        new_community.members.append(current_user)
        db.session.add(new_community)
        db.session.commit()

        return new_community.to_dict(), 201

    return {'errors': form.errors}, 401

@community_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_community(id):
    """
    Delete a community by ID
    """
    community = Community.query.get(id)

    if not community:
        return {'message': 'community not found'}

    if current_user.id == community.owner.id:
        db.session.delete(community)
        db.session.commit()
        return {'message': f'{community.name} Deleted Successfully'}

    else:
        return {'message': 'not your community!'}




@community_routes.route('/<int:id>')
def community(id):
    """
    Query for a community
    """
    community = Community.query.get(id)

    if not community:
        return {'message': 'community not found'}

    return community.to_dict()
