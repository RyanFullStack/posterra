from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Community, Post, db
from app.forms import PostForm
from datetime import datetime
import math
import random

post_routes = Blueprint('posts', __name__)


@post_routes.route('/')
def posts():
    """
    Query for all posts
    """
    page = int(request.args.get('page', 1))

    sort = request.args.get('sort', 'newest')

    posts = Post.query.all()

    if not posts:
        return {'message': 'no posts found'}

    if sort == 'best' or not sort:
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['numvotes'], reverse=True)
    if sort == 'popular':
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['numcomments'], reverse=True)
    if sort == 'newest':
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['created_at'], reverse=True)
    if sort == 'oldest':
        sorted_posts = sorted(posts, key=lambda post: post.to_dict()['created_at'], reverse=False)
    # if sort == 'random':
    #     random_sort = list(posts)
    #     random.shuffle(random_sort)
    #     sorted_posts = random_sort


    start_idx = (page - 1) * 15
    end_idx = start_idx + 15
    paginated_posts = sorted_posts[start_idx:end_idx]


    return {'posts': [post.to_dict() for post in paginated_posts],
            'totalPages': math.ceil(len(posts) / 15)
            }

@post_routes.route('/new', methods=['POST'])
@login_required
def create_post():
    """
    Create a new post
    """
    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        post_title = form.data['post_title']
        post_body = form.data['post_body']
        created_by = form.data['created_by']
        community_id = form.data['community_id']
        ext_url = form.data['ext_url']

        new_post = Post(post_title=post_title, post_body=post_body, created_by=created_by, community_id=community_id, ext_url=ext_url)

        db.session.add(new_post)
        db.session.commit()

        return new_post.to_dict(), 201

    return {'errors': form.errors}, 401


@post_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_post(id):
    """
    Edit an exisitng post
    """
    post = Post.query.get(id)

    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        post_title = form.data['post_title']
        post_body = form.data['post_body']
        created_by = form.data['created_by']
        community_id = form.data['community_id']
        ext_url = form.data['ext_url']

        post.post_title = post_title
        post.post_body = post_body
        post.created_by = created_by
        post.community_id = community_id
        post.ext_url = ext_url
        post.updated_at = datetime.now()
        post.edited = True

        db.session.commit()

        return post.to_dict()

    return {'errors': form.errors}, 401


@post_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_post(id):
    """
    Delete a post by ID
    """
    post = Post.query.get(id)

    if not post:
        return {'message': 'post not found'}

    if current_user.id == post.owner.id:
        db.session.delete(post)
        db.session.commit()
        return {'message': f'{post.post_title} Deleted Successfully'}

    else:
        return {'message': 'not your post!'}


@post_routes.route('/<int:id>')
def post(id):
    """
    Query for single post
    """
    post = Post.query.get(id)

    if not post:
        return {'message': 'post not found'}

    return post.to_dict()
