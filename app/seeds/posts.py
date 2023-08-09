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
        created_by=1, community_id=2, post_title='What if God came down one day and said', post_body="'Its pronounced Jod' then left?"
    )
    post4 = Post(
        created_by=2, community_id=2, post_title="Bill Gates said, 'I will always choose a lazy person to do a difficult job because a lazy person will find an easy way to do it.'", post_body='Whats a real-life example of this?'
    )
    post5 = Post(
        created_by=2, community_id=3, post_title='Illinois House passes bill prohibiting book bans', ext_url='https://www.wgem.com/2023/03/23/illinois-house-passes-bill-prohibiting-book-bans/'
    )
    post6 = Post(
        created_by=6, community_id=3, post_title='Textbook costs have risen nearly 1000 percent since the 70s', ext_url='https://www.vox.com/the-goods/2019/3/6/18252322/college-textbooks-cost-expensive-pearson-cengage-mcgraw-hill'
    )
    post7 = Post(
        created_by=6, community_id=4, post_title='[I ate] a taco box', post_body='Soo good!', ext_url='/images/taco.jpg'
    )
    post8 = Post(
        created_by=11, community_id=4, post_title="[Pro/Chef] 'Raspbaby Yoda' Raspberry Pie", ext_url='/images/yodapie.jpg'
    )
    post9 = Post(
        created_by=11, community_id=5, post_title='Sheep in Human Clothing', ext_url='/images/sheep.png'
    )
    post10 = Post(
        created_by=10, community_id=5, post_title='UPDATE. EA announces plans for next gen controller.', post_body='As expected.', ext_url='/images/ea.jpg'
    )
    post11 = Post(
        created_by=14, community_id=6, post_title='Minesweeper 99 x 99, 1500 mines. Took me about 2.5 hours to finish, nerve-wracking.', post_body='No one might care, but just wanted to share this.', ext_url='/images/mines.png'
    )
    post12 = Post(
        created_by=4, community_id=6, post_title='Jerry', ext_url='/images/jerry.jpg'
    )
    post13 = Post(
        created_by=13, community_id=7, post_title='3,000-year-old underwater castle discovered in Turkeys largest lake', ext_url='https://inhabitat.com/3000-year-old-underwater-castle-discovered-in-turkeys-largest-lake/'
    )
    post14 = Post(
        created_by=2, community_id=7, post_title='700 year old Knights Templar cave discovered in England', ext_url='https://www.bbc.com/news/uk-england-39193347'
    )
    post15 = Post(
        created_by=4, community_id=8, post_title="Tom Hanks as Mister Rogers on the set of 'You Are My Friend'", post_body='We miss you, Mister Rogers!', ext_url='/images/tom.jpg'
    )
    post16 = Post(
        created_by=8, community_id=8, post_title="This 'Deadpool 2' poster", post_body='My favorite poster by far. What do you think?', ext_url='/images/deadpool.jpg'
    )
    post17 = Post(
        created_by=5, community_id=9, post_title='A song I wrote just for Posterra', post_body='Enjoy!', ext_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    )
    post18 = Post(
        created_by=14, community_id=9, post_title="Jamie Lee Curtis leading the charge for earlier concerts: 'I want to hear Coldplay at 1PM'", ext_url='https://www.audacy.com/1053davefm/news/jamie-lee-curtis-leading-the-charge-for-earlier-concerts'
    )
    post19 = Post(
        created_by=8, community_id=10, post_title='Campbell will acquire Raos premium sauces parent company for $2.7 billion', ext_url='https://abcnews.go.com/GMA/Food/campbell-acquire-raos-premium-sauces-parent-company-27/story?id=102071512'
    )
    post20 = Post(
        created_by=1, community_id=10, post_title='Volunteer divers find 32 submerged cars in Doral lake, possibly linked to missing persons cold cases', post_body='More details to be released soon.', ext_url='https://wsvn.com/news/local/miami-dade/volunteer-divers-find-32-submerged-cars-in-doral-lake-possibly-linked-to-missing-persons-cold-cases/'
    )
    post21 = Post(
        created_by=10, community_id=11, post_title='Oregon wildfires making it look straight apocalyptic', ext_url='/images/oregon.jpg'
    )
    post22 = Post(
        created_by=9, community_id=11, post_title='Meeting Keanu Reeves at a traffic light', ext_url='/images/keanu.jpg'
    )
    post23 = Post(
        created_by=12, community_id=12, post_title="Scientists believe that the function of zebras' stripes are to deter insects", post_body='A team of researchers painted black and white stripes on cows. They found that it reduced the number of biting flies landing on the cows by more than 50%.', ext_url='https://www.realclearscience.com/quick_and_clear_science/2019/10/07/painting_zebra_stripes_on_cows_wards_off_biting_flies.html'
    )
    post24 = Post(
        created_by=3, community_id=12, post_title='In Seattle, Washington, delaying the start time of two high schools by nearly an hour lengthened students daily sleep by more than half an hour, and was associated with reduced sleepiness and increased academic performance.', ext_url='https://www.eurekalert.org/news-releases/528060'
    )
    post25 = Post(
        created_by=3, community_id=13, post_title='First full-colour Image of deep space from the James Webb Space Telescope revealed by NASA (in 4k)', post_body='We are so small.', ext_url='/images/space.jpg'
    )
    post26 = Post(
        created_by=13, community_id=13, post_title='I took nearly 50,000 images of the night sky to make an 81 Megapixel image of the moon.', ext_url='/images/moon.jpg'
    )
    post27 = Post(
        created_by=7, community_id=14, post_title='The Monterrey Stadium. Mexico.', post_body='My favorite place to go!', ext_url='/images/stadium.jpg'
    )
    post28 = Post(
        created_by=3, community_id=14, post_title='What 10,000 horsepower does to a drag tire at launch', ext_url='/images/tire.jpg'
    )
    post29 = Post(
        created_by=4, community_id=15, post_title="Stranger Things 5: Will Takes 'Center Stage' in final Season", ext_url='https://tvline.com/previews/stranger-things-season-5-spoilers-will-vecna-connection-1235024449/'
    )
    post30 = Post(
        created_by=7, community_id=15, post_title='Giving Back', post_body="'The Office' Star Leslie David Baker Is Giving Back $110,000 Worth of Fan Donations for Stalled Stanley Spinoff, Says Funds Were Never Used for Personal Matters", ext_url='https://variety.com/2023/tv/news/the-office-actor-returns-fan-donations-stnaley-spinoff-1235687187/'
    )
    post31 = Post(
        created_by=10, community_id=16, post_title='This is what happens when one company owns dozens of local news stations', post_body='Uncanny valley vibes...', ext_url='https://www.youtube.com/watch?v=hWLjYJ4BzvI&feature=youtu.be'
    )
    post32 = Post(
        created_by=9, community_id=16, post_title="Roughly the first five seconds of 'Never Gonna Give You Up' is now a silent Sony Music title card that displays copyright and licensing information, essentially ruining Rick Rolling", ext_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
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
