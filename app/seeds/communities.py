from app.models import db, Community, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_communities():
    art = Community( #1
        name='Art', created_by=9, description='A place for art of all kinds.', logo_pic='/communitypics/art.png'
    )
    ask = Community( #2
        name='Ask', created_by=1, description='A place for questions.', logo_pic='/communitypics/ask.jpg'
    )
    books = Community( #3
        name='Books', created_by=2, description='Book club!', logo_pic='/communitypics/books.jpg'
    )
    food = Community( #4
        name='Food', created_by=6, description='A place for the foodies.', logo_pic='/communitypics/food.jpg'
    )
    funny = Community( #5
        name='Funny', created_by=11, description='Ironic comedy welcome!', logo_pic='/communitypics/funny.jpg'
    )
    gaming = Community( #6
        name='Gaming', created_by=14, description='ggez', logo_pic='/communitypics/gaming.jpg'
    )
    history = Community( #7
        name='History', created_by=13, description='A place to remember.', logo_pic='/communitypics/history.jpg'
    )
    movies = Community( #8
        name='Movies', created_by=4, description='A place for all things movies.', logo_pic='/communitypics/movies.jpg'
    )
    music = Community( #9
        name='Music', created_by=5, description='A place to discover new music.', logo_pic='/communitypics/music.jpg'
    )
    news = Community( #10
        name='News', created_by=8, description='A place for current events.', logo_pic='/communitypics/news.png'
    )
    pics = Community( #11
        name='Pics', created_by=10, description='A place for pictures.', logo_pic='/communitypics/pics.png'
    )
    science = Community( #12
        name='Science', created_by=12, description='Give us your best hypothesis.', logo_pic='/communitypics/science.jpg'
    )
    space = Community( #13
        name='Space', created_by=3, description='Space needs no place!', logo_pic='/communitypics/space.jpg'
    )
    sports = Community( #14
        name='Sports', created_by=7, description='A place for sports chat.', logo_pic='/communitypics/sports.jpg'
    )
    tv = Community( #15
        name='TV', created_by=4, description='A place to talk all things tv.', logo_pic='/communitypics/tv.png'
    )
    videos = Community( #16
        name='Videos', created_by=10, description='A place to share videos.', logo_pic='/communitypics/videos.png'
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
