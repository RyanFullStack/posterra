from .db import db, environment, SCHEMA, add_prefix_for_prod

community_members = db.Table(
    'community_members',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('community_id', db.Integer, db.ForeignKey(add_prefix_for_prod('communities.id'))),
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
)

if environment == "production":
    community_members.schema = SCHEMA
