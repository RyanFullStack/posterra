from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .community_members import community_members


class Community(db.Model):
    __tablename__ = 'communities'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String(255))
    logo_pic = db.Column(db.String, default='/communitypic.png')
    banner_pic = db.Column(db.String, default='/bannerpic.png')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    owner = db.relationship('User', back_populates='owned_communities')

    members = db.relationship('User', secondary=community_members, back_populates='communities')

    posts = db.relationship('Post', back_populates='community', cascade='all, delete-orphan')


    def to_dict(self):
          return {
            'id': self.id,
            'name': self.name,
            'created_by': self.created_by,
            'description': self.description,
            'logo_pic': self.logo_pic,
            'banner_pic': self.banner_pic,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner': self.owner.to_dict()
        }
