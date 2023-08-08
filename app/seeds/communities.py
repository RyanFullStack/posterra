from app.models import db, Community, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_communities():
    art = Community( #1
        name='Art', created_by=9, description='A place for art of all kinds.'
    )
    ask = Community( #2
        name='Ask', created_by=1, description='A place for questions.'
    )
    books = Community( #3
        name='Books', created_by=2, description='Book club!'
    )
    food = Community( #4
        name='Food', created_by=6, description='A place for the foodies.'
    )
    funny = Community( #5
        name='Funny', created_by=11, description='Ironic comedy welcome!'
    )
    gaming = Community( #6
        name='Gaming', created_by=14, description='ggez'
    )
    history = Community( #7
        name='History', created_by=13, description='A place to remember.'
    )
    movies = Community( #8
        name='Movies', created_by=4, description='A place for all things movies.'
    )
    music = Community( #9
        name='Music', created_by=5, description='A place to discover new music.'
    )
    news = Community( #10
        name='News', created_by=8, description='A place for current events.'
    )
    pics = Community( #11
        name='Pics', created_by=10, description='A place for pictures.'
    )
    science = Community( #12
        name='Science', created_by=12, description='Give us your best hypothesis.'
    )
    space = Community( #13
        name='Space', created_by=3, description='Space needs no place!'
    )
    sports = Community( #14
        name='Sports', created_by=7, description='A place for sports chat.'
    )
    tv = Community( #15
        name='TV', created_by=4, description='A place to talk all things tv.'
    )
    videos = Community( #16
        name='Videos', created_by=10, description='A place to share videos.'
    )


    db.session.add(art)
    db.session.add(ask)
    db.session.add(books)
    db.session.add(food)
    db.session.add(funny)
    db.session.add(gaming)
    db.session.add(history)
    db.session.add(movies)
    db.session.add(music)
    db.session.add(news)
    db.session.add(pics)
    db.session.add(science)
    db.session.add(space)
    db.session.add(sports)
    db.session.add(tv)
    db.session.add(videos)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the communities table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_seed_communities():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.communities RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM communities"))

    db.session.commit()
