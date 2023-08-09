from flask import Blueprint, request
from flask_login import login_required
from app.models import Community, Post, db
from app.forms import PostForm

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

@post_routes.route('/<int:id>')
def post(id):
    """
    Query for single post
    """
    post = Post.query.get(id)

    if not post:
        return {'message': 'post not found'}

    return post.to_dict()
