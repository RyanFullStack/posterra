from app.models import db, CommentVote, environment, SCHEMA
from sqlalchemy.sql import text
import random


# Adds a demo user, you can add other users here if you want
def seed_comment_votes():

    user_ids = list(range(1, 15))
    comment_ids = list(range(1, 201))
    upvote_choices = [True, True, True, False]

    num_comment_votes = 1000
    comment_vote_list = []

    while len(comment_vote_list) < num_comment_votes:
        user_id = random.choice(user_ids)
        comment_id = random.choice(comment_ids)
        upvote = random.choice(upvote_choices)

        if any(entry['user_id'] == user_id and entry['comment_id'] == comment_id for entry in comment_vote_list):
            continue

        comment_vote_list.append({'user_id': user_id, 'comment_id': comment_id, 'upvote': upvote})

    for entry in comment_vote_list:
        comment_vote = CommentVote(
            user_id=entry['user_id'],
            comment_id=entry['comment_id'],
            upvote=entry['upvote']
        )
        db.session.add(comment_vote)

    # Commit the changes to the database session
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
