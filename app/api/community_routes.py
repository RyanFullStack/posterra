from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Community, Post, db
from app.forms import CommunityForm
from datetime import datetime
import random
import math

community_routes = Blueprint('communities', __name__)


@community_routes.route('/')
def communities():
    """
    Query for all communities
    """
    communities = Community.query.all()

    if not communities:
        return {'message': 'no communities found'}

    sorted_communities = sorted(communities, key=lambda community: community.to_dict()['name'].lower(), reverse=False)

    return {'communities': [community.to_dict() for community in sorted_communities]}


@community_routes.route('/<int:id>/posts')
def community_posts(id):
    """
    Query for all posts within a community
    """
    page = int(request.args.get('page', 1))

    sort = request.args.get('sort', 'newest')

    community = Community.query.get(id)

    if not community:
        return {'message': 'community not found'}

    posts = community.posts

    if sort == 'best' or not sort:
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['numvotes'], reverse=True)
    if sort == 'popular':
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['numcomments'], reverse=True)
    if sort == 'newest':
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['created_at'], reverse=True)
    if sort == 'oldest':
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['created_at'], reverse=False)

    start_idx = (page - 1) * 10
    end_idx = start_idx + 10
    paginated_posts = sorted_posts[start_idx:end_idx]


    return {'posts': [post.to_dict() for post in paginated_posts],
            'totalPages': math.ceil(len(posts) / 10)
            }


@community_routes.route('/new', methods=['POST'])
@login_required
def create_community():
    """
    Create a new community
    """
    form = CommunityForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        name = form.data['name'].title()
        created_by = form.data['created_by']
        description = form.data['description']

        new_community = Community(name=name, created_by=created_by, description=description)

        new_community.members.append(current_user)
        db.session.add(new_community)
        db.session.commit()

        return new_community.to_dict(), 201

    return {'errors': form.errors}, 401


@community_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_community(id):
    """
    Edit an exisitng community
    """
    community = Community.query.get(id)

    form = CommunityForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        name = form.data['name']
        description = form.data['description']
        logo_pic = form.data['logo_pic']
        banner_pic = form.data['banner_pic']

        community.name = name
        community.description = description
        community.logo_pic = logo_pic
        community.banner_pic = banner_pic
        community.updated_at = datetime.now()

        db.session.commit()

        return community.to_dict()

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
