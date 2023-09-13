from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, PostVote, CommentVote


vote_routes = Blueprint('votes', __name__)


@vote_routes.route('/comments/<int:id>')
def get_comment_votes(id):
    """
    Query for all votes on a comment by id
    """
    votes = CommentVote.query.filter(CommentVote.comment_id == id).all()

    if not votes:
        return {'message': 'no votes found'}

    return {'votes': [vote.to_dict() for vote in votes]}


@vote_routes.route('/<int:id>/addupvote')
@login_required
def add_upvote(id):
    """
    Add an upvote to a post
    """
    new_vote = PostVote(user_id=current_user.id, post_id=id, upvote=True)
    db.session.add(new_vote)
    db.session.commit()

    return {'vote': 'upvote added'}


@vote_routes.route('/comments/<int:id>/addupvote')
@login_required
def add_comment_upvote(id):
    """
    Add an upvote to a comment
    """
    new_vote = CommentVote(user_id=current_user.id, comment_id=id, upvote=True)
    db.session.add(new_vote)
    db.session.commit()

    return {'vote': 'upvote added'}


@vote_routes.route('/<int:id>/adddownvote')
@login_required
def add_downvote(id):
    """
    Add a downvote to a post
    """
    new_vote = PostVote(user_id=current_user.id, post_id=id, upvote=False)
    db.session.add(new_vote)
    db.session.commit()

    return {'vote': 'downvote added'}

@vote_routes.route('/comments/<int:id>/adddownvote')
@login_required
def add_comment_downvote(id):
    """
    Add a downvote to a comment
    """
    new_vote = CommentVote(user_id=current_user.id, comment_id=id, upvote=False)
    db.session.add(new_vote)
    db.session.commit()

    return {'vote': 'downvote added'}


@vote_routes.route('/<int:id>/deletevote')
@login_required
def delete_vote(id):
    """
    Delete a vote on a post
    """
    vote = PostVote.query.filter((PostVote.post_id == id) & (PostVote.user_id == current_user.id)).first()
    db.session.delete(vote)
    db.session.commit()

    return {'vote': 'vote deleted'}

@vote_routes.route('/comments/<int:id>/deletevote')
@login_required
def delete_comment_vote(id):
    """
    Delete a vote on a comment
    """
    vote = CommentVote.query.filter((CommentVote.comment_id == id) & (CommentVote.user_id == current_user.id)).first()
    db.session.delete(vote)
    db.session.commit()

    return {'vote': 'vote deleted'}


@vote_routes.route('/<int:id>')
def votes(id):
    """
    Query for all votes on a post
    """
    votes = PostVote.query.filter(PostVote.post_id == id).all()

    if not votes:
        return {'message': 'no votes found'}

    return {'votes': [vote.to_dict() for vote in votes]}
