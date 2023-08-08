from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_posts():
    post1 = Post(
        created_by=9, community_id=1, post_title='The New American Gothic', post_body='Oil on canvas, 2017, Criselda Vesquez', ext_url='/images/gothic.jpg'
    )
    post2 = Post(
        created_by=10, community_id=1, post_title='The Making of the Perfect Martini', post_body='Lithography, 2000, Guy Buffet', ext_url='/images/martini.jpg'
    )
    post3 = Post(
        created_by=1, community_id=2, post_title='What if God came down one day and said "Its pronounced Jod" then left?'
    )
    post4 = Post(
        created_by=2, community_id=2, post_title='Bill Gates said, "I will always choose a lazy person to do a difficult job because a lazy person will find an easy way to do it." Whats a real-life example of this?'
    )
    post5 = Post(
        created_by=2, community_id=3, post_title='Illinois House passes bill prohibiting book bans', ext_url='https://www.wgem.com/2023/03/23/illinois-house-passes-bill-prohibiting-book-bans/'
    )
    post6 = Post(
        created_by=6, community_id=3, post_title='Textbook costs have risen nearly 1000 percent since the 70s', ext_url='https://www.vox.com/the-goods/2019/3/6/18252322/college-textbooks-cost-expensive-pearson-cengage-mcgraw-hill'
    )
    post7 = Post(
        created_by=6, community_id=4, post_title='[I ate] a taco box', ext_url='/images/taco.jpg'
    )
    post8 = Post(
        created_by=11, community_id=4, post_title='[Pro/Chef] “Raspbaby Yoda” Raspberry Pie', ext_url='images/yodapie.jpg'
    )
    post9 = Post(
        created_by=11, community_id=5, post_title='', post_body='', ext_url=''
    )
    post10 = Post(
        created_by=10, community_id=5, post_title='', post_body='', ext_url=''
    )
    post11 = Post(
        created_by=14, community_id=6, post_title='', post_body='', ext_url=''
    )
    post12 = Post(
        created_by=4, community_id=6, post_title='', post_body='', ext_url=''
    )
    post13 = Post(
        created_by=13, community_id=7, post_title='', post_body='', ext_url=''
    )
    post14 = Post(
        created_by=2, community_id=7, post_title='', post_body='', ext_url=''
    )
    post15 = Post(
        created_by=4, community_id=8, post_title='', post_body='', ext_url=''
    )
    post16 = Post(
        created_by=8, community_id=8, post_title='', post_body='', ext_url=''
    )
    post17 = Post(
        created_by=5, community_id=9, post_title='', post_body='', ext_url=''
    )
    post18 = Post(
        created_by=14, community_id=9, post_title='', post_body='', ext_url=''
    )
    post19 = Post(
        created_by=8, community_id=10, post_title='', post_body='', ext_url=''
    )
    post20 = Post(
        created_by=1, community_id=10, post_title='', post_body='', ext_url=''
    )
    post21 = Post(
        created_by=10, community_id=11, post_title='', post_body='', ext_url=''
    )
    post22 = Post(
        created_by=9, community_id=11, post_title='', post_body='', ext_url=''
    )
    post23 = Post(
        created_by=12, community_id=12, post_title='', post_body='', ext_url=''
    )
    post24 = Post(
        created_by=3, community_id=12, post_title='', post_body='', ext_url=''
    )
    post25 = Post(
        created_by=3, community_id=13, post_title='', post_body='', ext_url=''
    )
    post26 = Post(
        created_by=13, community_id=13, post_title='', post_body='', ext_url=''
    )
    post27 = Post(
        created_by=7, community_id=14, post_title='', post_body='', ext_url=''
    )
    post28 = Post(
        created_by=3, community_id=14, post_title='', post_body='', ext_url=''
    )
    post29 = Post(
        created_by=4, community_id=15, post_title='', post_body='', ext_url=''
    )
    post30 = Post(
        created_by=7, community_id=15, post_title='', post_body='', ext_url=''
    )
    post31 = Post(
        created_by=10, community_id=16, post_title='', post_body='', ext_url=''
    )
    post32 = Post(
        created_by=9, community_id=16, post_title='', post_body='', ext_url=''
    )


    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.add(post16)
    db.session.add(post17)
    db.session.add(post18)
    db.session.add(post19)
    db.session.add(post20)
    db.session.add(post21)
    db.session.add(post22)
    db.session.add(post23)
    db.session.add(post24)
    db.session.add(post25)
    db.session.add(post26)
    db.session.add(post27)
    db.session.add(post28)
    db.session.add(post29)
    db.session.add(post30)
    db.session.add(post31)
    db.session.add(post32)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the posts table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_seed_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
