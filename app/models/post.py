from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'


    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    community_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('communities.id')))
    post_title = db.Column(db.String(255), nullable=False)
    post_body = db.Column(db.String)
    edited = db.Column(db.Boolean, default=False)
    ext_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    owner = db.relationship('User', back_populates='posts')

    community = db.relationship('Community', back_populates='posts')


    def to_dict(self):
          return {
            'id': self.id,
            'created_by': self.created_by,
            'community_id': self.community_id,
            'post_body': self.post_body,
            'edited': self.edited,
            'ext_url': self.ext_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
