from .db import db, environment, SCHEMA, add_prefix_for_prod


class CommentVote(db.Model):
    __tablename__ = 'comment_votes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    comment_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('comments.id')))
    upvote = db.Column(db.Boolean)

    owner = db.relationship('User', back_populates='comment_votes')

    comment = db.relationship('Comment', back_populates='votes')



    def to_dict(self):
          return {
            'id': self.id,
            'user_id': self.user_id,
            'comment_id': self.comment_id,
            'upvote': self.upvote,
            'owner': self.owner.to_dict()
        }
