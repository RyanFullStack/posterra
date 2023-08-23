from app.models import db, PostVote, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_post_votes():

    post_vote1 = PostVote(
        user_id=1, post_id=1, upvote=True
    )

    db.session.add(post_vote1)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the post_votes table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_seed_post_votes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.post_votes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM post_votes"))

    db.session.commit()
