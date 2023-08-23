from app.models import db, CommentVote, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_comment_votes():

    comment_vote1 = CommentVote(
        user_id=1, comment_id=1, upvote=True
    )

    db.session.add(comment_vote1)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the comment_votes table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_seed_comment_votes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comment_votes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comment_votes"))

    db.session.commit()
