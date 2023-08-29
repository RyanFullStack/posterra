from app.models import db, PostVote, environment, SCHEMA
from sqlalchemy.sql import text
import random



def seed_post_votes():

    user_ids = list(range(1, 15))
    post_ids = list(range(1, 81))
    upvote_choices = [True, True, True, False]

    num_post_votes = 600
    post_vote_list = []

    while len(post_vote_list) < num_post_votes:
        user_id = random.choice(user_ids)
        post_id = random.choice(post_ids)
        upvote = random.choice(upvote_choices)

        if any(entry['user_id'] == user_id and entry['post_id'] == post_id for entry in post_vote_list):
            continue

        post_vote_list.append({'user_id': user_id, 'post_id': post_id, 'upvote': upvote})

    for entry in post_vote_list:
        post_vote = PostVote(
            user_id=entry['user_id'],
            post_id=entry['post_id'],
            upvote=entry['upvote']
        )
        db.session.add(post_vote)

    # Commit the changes to the database session
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
