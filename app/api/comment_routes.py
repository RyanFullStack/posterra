from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Comment
from app.forms import CommentForm

comment_routes = Blueprint('comments', __name__)


@comment_routes.route('/<int:id>/new', methods=['POST'])
@login_required
def add_comment(id):
    """
    Add a comment to a post
    """
    form = CommentForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        created_by = form.data['created_by']
        post_id = id
        comment_body = form.data['comment_body']

        new_comment = Comment(created_by=created_by, post_id=post_id, comment_body=comment_body)

        db.session.add(new_comment)
        db.session.commit()

        return new_comment.to_dict(), 201

    return {'errors': form.errors}, 401


@comment_routes.route('/<int:id>')
def get_comments(id):
    """
    Query for all comments on a post by id
    """
    comments = Comment.query.filter(Comment.post_id == id).all()

    if not comments:
        return {'message': 'No comments found'}

    sort = request.args.get('sort', 'newest')

    if sort == 'newest' or not sort:
        sorted_comments = sorted(comments, key=lambda comment: comment.to_dict()['created_at'], reverse=True)

    return {'comments': [comment.to_dict() for comment in sorted_comments]}
