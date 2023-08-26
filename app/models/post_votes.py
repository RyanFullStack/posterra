from .db import db, environment, SCHEMA, add_prefix_for_prod


class PostVote(db.Model):
    __tablename__ = 'post_votes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    post_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('posts.id')))
    upvote = db.Column(db.Boolean)

    owner = db.relationship('User', back_populates='post_votes')

    post = db.relationship('Post', back_populates='votes')



    def to_dict(self):
          return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'upvote': self.upvote
        }
