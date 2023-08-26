from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    post_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('posts.id')))
    parent_comment_id = db.Column(db.Integer)
    comment_body = db.Column(db.String(1000))
    edited = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    owner = db.relationship('User', back_populates='comments')

    post = db.relationship('Post', back_populates='comments')

    votes = db.relationship('CommentVote', back_populates='comment', cascade='all, delete-orphan')


    def to_dict(self):
          return {
            'id': self.id,
            'created_by': self.created_by,
            'post_id': self.post_id,
            'parent_comment_id': self.parent_comment_id,
            'comment_body': self.comment_body,
            'edited': self.edited,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner': self.owner.to_dict()
        }
