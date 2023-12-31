from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text
from faker import Faker
from datetime import datetime
fake = Faker()
start_date = datetime(year=2023, month=9, day=2)
end_date = datetime.now()


def seed_comments():

    comment1 = Comment(
    created_by=1, post_id=1, comment_body='I love this post!',
    created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment2 = Comment(
        created_by=10, post_id=1, comment_body="This content is fantastic!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment3 = Comment(
        created_by=4, post_id=1, comment_body="Impressive work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment4 = Comment(
        created_by=7, post_id=1, comment_body="Thanks for sharing your insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment5 = Comment(
        created_by=6, post_id=1, comment_body="I'm learning something new!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment6 = Comment(
        created_by=12, post_id=1, comment_body="Great perspective!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment7 = Comment(
        created_by=5, post_id=2, comment_body="This is so helpful.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment8 = Comment(
        created_by=13, post_id=3, comment_body="Spot on!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment9 = Comment(
        created_by=9, post_id=4, comment_body="Appreciate the valuable content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment10 = Comment(
        created_by=1, post_id=4, comment_body="Well done!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment11 = Comment(
        created_by=11, post_id=4, comment_body="Your insights are enlightening.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment12 = Comment(
        created_by=14, post_id=5, comment_body="Thumbs up!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment13 = Comment(
        created_by=3, post_id=5, comment_body="Impressed with your work.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment14 = Comment(
        created_by=8, post_id=6, comment_body="You've nailed it!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment15 = Comment(
        created_by=2, post_id=6, comment_body="Great job!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment16 = Comment(
        created_by=4, post_id=7, comment_body="This resonates with me.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment17 = Comment(
        created_by=10, post_id=7, comment_body="Loving the insights!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment18 = Comment(
        created_by=13, post_id=8, comment_body="Pure gold.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment19 = Comment(
        created_by=6, post_id=8, comment_body="You're on fire!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment20 = Comment(
        created_by=1, post_id=8, comment_body="This is valuable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment21 = Comment(
        created_by=12, post_id=8, comment_body="Kudos!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment22 = Comment(
        created_by=7, post_id=9, comment_body="Epic content!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment23 = Comment(
        created_by=3, post_id=9, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment24 = Comment(
        created_by=5, post_id=9, comment_body="Feeling inspired!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment25 = Comment(
        created_by=14, post_id=9, comment_body="You rock!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment26 = Comment(
        created_by=11, post_id=9, comment_body="Top-notch insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment27 = Comment(
        created_by=2, post_id=10, comment_body="A fan of your work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment28 = Comment(
        created_by=4, post_id=10, comment_body="Pure genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment29 = Comment(
        created_by=8, post_id=11, comment_body="You're making a difference!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment30 = Comment(
        created_by=10, post_id=11, comment_body="Impactful content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment31 = Comment(
        created_by=12, post_id=11, comment_body="You're awesome!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment32 = Comment(
        created_by=1, post_id=12, comment_body="Keep up the good work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment33 = Comment(
        created_by=7, post_id=13, comment_body="Incredible insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment34 = Comment(
        created_by=13, post_id=13, comment_body="Learning a lot from this.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment35 = Comment(
        created_by=6, post_id=13, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment36 = Comment(
        created_by=3, post_id=13, comment_body="Golden content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment37 = Comment(
        created_by=9, post_id=14, comment_body="You're a game changer.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment38 = Comment(
        created_by=2, post_id=14, comment_body="Grateful for this!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment39 = Comment(
        created_by=4, post_id=14, comment_body="Appreciate your impact.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment40 = Comment(
        created_by=14, post_id=14, comment_body="Insightful thoughts.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment41 = Comment(
        created_by=5, post_id=15, comment_body="You're inspiring.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment42 = Comment(
        created_by=12, post_id=15, comment_body="Value-packed content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment43 = Comment(
        created_by=11, post_id=16, comment_body="On point!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment44 = Comment(
        created_by=10, post_id=16, comment_body="A gem of a post.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment45 = Comment(
        created_by=1, post_id=17, comment_body="Enlightening insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment46 = Comment(
        created_by=8, post_id=17, comment_body="Thought-provoking!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment47 = Comment(
        created_by=9, post_id=18, comment_body="A visionary perspective.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment48 = Comment(
        created_by=7, post_id=18, comment_body="Exceptional insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment49 = Comment(
        created_by=6, post_id=18, comment_body="Trailblazing content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment50 = Comment(
        created_by=3, post_id=18, comment_body="Game-changing thoughts.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment51 = Comment(
        created_by=13, post_id=19, comment_body="A thought leader!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment52 = Comment(
        created_by=2, post_id=19, comment_body="Impactful sharing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment53 = Comment(
        created_by=4, post_id=19, comment_body="Changing perspectives.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment54 = Comment(
        created_by=5, post_id=19, comment_body="Revolutionary content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment55 = Comment(
        created_by=12, post_id=19, comment_body="Mind-blowing insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment56 = Comment(
        created_by=11, post_id=20, comment_body="Awe-inspiring content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment57 = Comment(
        created_by=14, post_id=20, comment_body="You're a star!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment58 = Comment(
        created_by=1, post_id=20, comment_body="Top-level insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment59 = Comment(
        created_by=9, post_id=21, comment_body="Exceptional work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment60 = Comment(
        created_by=10, post_id=21, comment_body="Outstanding insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment61 = Comment(
        created_by=6, post_id=21, comment_body="Phenomenal content!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment62 = Comment(
        created_by=7, post_id=22, comment_body="Groundbreaking insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment63 = Comment(
        created_by=3, post_id=22, comment_body="You're on fire!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment64 = Comment(
        created_by=9, post_id=22, comment_body="Remarkable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment65 = Comment(
        created_by=2, post_id=23, comment_body="You're a trailblazer!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment66 = Comment(
        created_by=4, post_id=23, comment_body="Thanks for sharing!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment67 = Comment(
        created_by=13, post_id=24, comment_body="Insightful content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment68 = Comment(
        created_by=5, post_id=24, comment_body="Appreciate your thoughts.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment69 = Comment(
        created_by=11, post_id=25, comment_body="This is great!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment70 = Comment(
        created_by=7, post_id=26, comment_body="You're making an impact.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment71 = Comment(
        created_by=6, post_id=26, comment_body="Impressive insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment72 = Comment(
        created_by=12, post_id=27, comment_body="You're inspiring!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment73 = Comment(
        created_by=14, post_id=28, comment_body="Invaluable content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment74 = Comment(
        created_by=1, post_id=28, comment_body="Great insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment75 = Comment(
        created_by=8, post_id=28, comment_body="You're a game changer.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment76 = Comment(
        created_by=10, post_id=29, comment_body="This is top-notch.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment77 = Comment(
        created_by=9, post_id=30, comment_body="You're on point.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment78 = Comment(
        created_by=3, post_id=30, comment_body="Brilliant thoughts!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment79 = Comment(
        created_by=2, post_id=30, comment_body="You're remarkable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment80 = Comment(
        created_by=4, post_id=31, comment_body="Impressive work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment81 = Comment(
        created_by=6, post_id=32, comment_body="This is excellent.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment82 = Comment(
        created_by=12, post_id=32, comment_body="Your insights are valuable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment83 = Comment(
        created_by=5, post_id=32, comment_body="Thanks for sharing!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment84 = Comment(
        created_by=13, post_id=33, comment_body="You're an inspiration.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment85 = Comment(
        created_by=1, post_id=34, comment_body="This is amazing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment86 = Comment(
        created_by=11, post_id=34, comment_body="You're insightful!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment87 = Comment(
        created_by=14, post_id=35, comment_body="You're a rockstar.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment88 = Comment(
        created_by=7, post_id=35, comment_body="This is fantastic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment89 = Comment(
        created_by=10, post_id=36, comment_body="You're changing lives!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment90 = Comment(
        created_by=8, post_id=37, comment_body="You're a thought leader.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment91 = Comment(
        created_by=2, post_id=37, comment_body="Your perspective is valuable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment92 = Comment(
        created_by=9, post_id=37, comment_body="This is brilliant.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment93 = Comment(
        created_by=3, post_id=37, comment_body="Appreciate your insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment94 = Comment(
        created_by=6, post_id=38, comment_body="You're inspiring.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment95 = Comment(
        created_by=12, post_id=38, comment_body="This is thought-provoking.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment96 = Comment(
        created_by=1, post_id=39, comment_body="You're impressive.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment97 = Comment(
        created_by=4, post_id=39, comment_body="Your work is invaluable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment98 = Comment(
        created_by=5, post_id=40, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment99 = Comment(
        created_by=13, post_id=40, comment_body="Keep it up!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment100 = Comment(
        created_by=11, post_id=41, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment101 = Comment(
        created_by=7, post_id=41, comment_body="This is game-changing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment102 = Comment(
        created_by=14, post_id=41, comment_body="You're on fire!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment103 = Comment(
        created_by=10, post_id=42, comment_body="Remarkable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment104 = Comment(
        created_by=8, post_id=43, comment_body="This is gold.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment105 = Comment(
        created_by=9, post_id=43, comment_body="Impressed with your work.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment106 = Comment(
        created_by=3, post_id=44, comment_body="You're top-notch.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment107 = Comment(
        created_by=2, post_id=44, comment_body="Thanks for sharing your insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment108 = Comment(
        created_by=12, post_id=45, comment_body="This is epic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment109 = Comment(
        created_by=6, post_id=45, comment_body="You're making a difference.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment110 = Comment(
        created_by=1, post_id=45, comment_body="Incredible work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment111 = Comment(
        created_by=4, post_id=46, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment112 = Comment(
        created_by=5, post_id=46, comment_body="Mind-blowing insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment113 = Comment(
        created_by=13, post_id=46, comment_body="You're exceptional.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment114 = Comment(
        created_by=11, post_id=47, comment_body="This is top-level.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment115 = Comment(
        created_by=7, post_id=47, comment_body="Invaluable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment116 = Comment(
        created_by=14, post_id=48, comment_body="You're a visionary.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment117 = Comment(
        created_by=10, post_id=48, comment_body="Outstanding content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment118 = Comment(
        created_by=8, post_id=48, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment119 = Comment(
        created_by=9, post_id=49, comment_body="You're a game changer.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment120 = Comment(
        created_by=2, post_id=49, comment_body="This is epic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment121 = Comment(
        created_by=3, post_id=49, comment_body="You're on fire!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment122 = Comment(
        created_by=12, post_id=50, comment_body="Exceptional insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment123 = Comment(
        created_by=6, post_id=50, comment_body="You're an inspiration.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment124 = Comment(
        created_by=1, post_id=50, comment_body="This is life-changing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment125 = Comment(
        created_by=4, post_id=51, comment_body="Your work is impactful.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment126 = Comment(
        created_by=5, post_id=51, comment_body="Incredible content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment127 = Comment(
        created_by=13, post_id=51, comment_body="This is gold.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment128 = Comment(
        created_by=11, post_id=52, comment_body="You're a thought leader.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment129 = Comment(
        created_by=7, post_id=52, comment_body="Thought-provoking insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment130 = Comment(
        created_by=14, post_id=53, comment_body="This is fantastic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment131 = Comment(
        created_by=10, post_id=53, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment132 = Comment(
        created_by=9, post_id=53, comment_body="Invaluable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment133 = Comment(
        created_by=8, post_id=54, comment_body="You're changing lives!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment134 = Comment(
        created_by=2, post_id=54, comment_body="Your work is remarkable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment135 = Comment(
        created_by=3, post_id=55, comment_body="Incredible insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment136 = Comment(
        created_by=12, post_id=55, comment_body="You're a game changer.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment137 = Comment(
        created_by=6, post_id=55, comment_body="This is epic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment138 = Comment(
        created_by=1, post_id=56, comment_body="Outstanding work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment139 = Comment(
        created_by=4, post_id=56, comment_body="You're a visionary.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment140 = Comment(
        created_by=5, post_id=57, comment_body="You're on point.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment141 = Comment(
        created_by=13, post_id=57, comment_body="Brilliant insights!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment142 = Comment(
        created_by=11, post_id=57, comment_body="This is top-level.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment143 = Comment(
        created_by=7, post_id=58, comment_body="Impressive content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment144 = Comment(
        created_by=14, post_id=58, comment_body="You're remarkable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment145 = Comment(
        created_by=10, post_id=59, comment_body="This is game-changing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment146 = Comment(
        created_by=8, post_id=59, comment_body="Thanks for sharing your insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment147 = Comment(
        created_by=9, post_id=60, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment148 = Comment(
        created_by=2, post_id=60, comment_body="Remarkable work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment149 = Comment(
        created_by=3, post_id=60, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment150 = Comment(
        created_by=12, post_id=61, comment_body="Invaluable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment151 = Comment(
        created_by=6, post_id=61, comment_body="This is gold.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment152 = Comment(
        created_by=1, post_id=61, comment_body="You're a visionary.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment153 = Comment(
        created_by=4, post_id=62, comment_body="You're making an impact.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment154 = Comment(
        created_by=5, post_id=62, comment_body="Brilliant thoughts.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment155 = Comment(
        created_by=13, post_id=62, comment_body="You're a thought leader.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment156 = Comment(
        created_by=11, post_id=63, comment_body="This is top-notch.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment157 = Comment(
        created_by=7, post_id=63, comment_body="You're an inspiration.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment158 = Comment(
        created_by=14, post_id=64, comment_body="Exceptional work.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment159 = Comment(
        created_by=10, post_id=64, comment_body="You're impressive.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment160 = Comment(
        created_by=8, post_id=64, comment_body="You're changing lives!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment161 = Comment(
        created_by=9, post_id=65, comment_body="Incredible insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment162 = Comment(
        created_by=2, post_id=65, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment163 = Comment(
        created_by=3, post_id=65, comment_body="This is epic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment164 = Comment(
        created_by=12, post_id=66, comment_body="Outstanding work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment165 = Comment(
        created_by=6, post_id=66, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment166 = Comment(
        created_by=1, post_id=66, comment_body="Invaluable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment167 = Comment(
        created_by=4, post_id=67, comment_body="You're on point.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment168 = Comment(
        created_by=5, post_id=67, comment_body="Brilliant insights!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment169 = Comment(
        created_by=13, post_id=67, comment_body="This is top-level.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment170 = Comment(
        created_by=11, post_id=68, comment_body="Impressive content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment171 = Comment(
        created_by=7, post_id=68, comment_body="You're remarkable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment172 = Comment(
        created_by=14, post_id=69, comment_body="This is game-changing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment173 = Comment(
        created_by=10, post_id=69, comment_body="Thanks for sharing your insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment174 = Comment(
        created_by=8, post_id=70, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment175 = Comment(
        created_by=9, post_id=70, comment_body="Remarkable work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment176 = Comment(
        created_by=2, post_id=70, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment177 = Comment(
        created_by=3, post_id=71, comment_body="Incredible insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment178 = Comment(
        created_by=12, post_id=71, comment_body="You're making an impact.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment179 = Comment(
        created_by=6, post_id=71, comment_body="Brilliant thoughts!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment180 = Comment(
        created_by=1, post_id=72, comment_body="You're changing lives!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment181 = Comment(
        created_by=4, post_id=72, comment_body="Invaluable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment182 = Comment(
        created_by=5, post_id=72, comment_body="You're a thought leader.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment183 = Comment(
        created_by=13, post_id=73, comment_body="This is epic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment184 = Comment(
        created_by=11, post_id=73, comment_body="Outstanding work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment185 = Comment(
        created_by=7, post_id=73, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment186 = Comment(
        created_by=14, post_id=74, comment_body="Invaluable insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment187 = Comment(
        created_by=10, post_id=74, comment_body="This is top-notch.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment188 = Comment(
        created_by=8, post_id=75, comment_body="Impressive content.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment189 = Comment(
        created_by=9, post_id=75, comment_body="You're remarkable.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment190 = Comment(
        created_by=2, post_id=75, comment_body="This is game-changing.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment191 = Comment(
        created_by=3, post_id=76, comment_body="Thanks for sharing your insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment192 = Comment(
        created_by=12, post_id=76, comment_body="You're a legend.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment193 = Comment(
        created_by=6, post_id=76, comment_body="Remarkable work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment194 = Comment(
        created_by=1, post_id=77, comment_body="You're a genius.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment195 = Comment(
        created_by=4, post_id=77, comment_body="Incredible insights.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment196 = Comment(
        created_by=5, post_id=78, comment_body="This is epic.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment197 = Comment(
        created_by=13, post_id=78, comment_body="Outstanding work!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment198 = Comment(
        created_by=11, post_id=79, comment_body="You're making an impact.",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment199 = Comment(
        created_by=7, post_id=79, comment_body="Brilliant thoughts!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )

    comment200 = Comment(
        created_by=14, post_id=80, comment_body="You're changing lives!",
        created_at=fake.date_time_between(start_date=start_date, end_date=end_date)
    )


    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)
    db.session.add(comment6)
    db.session.add(comment7)
    db.session.add(comment8)
    db.session.add(comment9)
    db.session.add(comment10)
    db.session.add(comment11)
    db.session.add(comment12)
    db.session.add(comment13)
    db.session.add(comment14)
    db.session.add(comment15)
    db.session.add(comment16)
    db.session.add(comment17)
    db.session.add(comment18)
    db.session.add(comment19)
    db.session.add(comment20)
    db.session.add(comment21)
    db.session.add(comment22)
    db.session.add(comment23)
    db.session.add(comment24)
    db.session.add(comment25)
    db.session.add(comment26)
    db.session.add(comment27)
    db.session.add(comment28)
    db.session.add(comment29)
    db.session.add(comment30)
    db.session.add(comment31)
    db.session.add(comment32)
    db.session.add(comment33)
    db.session.add(comment34)
    db.session.add(comment35)
    db.session.add(comment36)
    db.session.add(comment37)
    db.session.add(comment38)
    db.session.add(comment39)
    db.session.add(comment40)
    db.session.add(comment41)
    db.session.add(comment42)
    db.session.add(comment43)
    db.session.add(comment44)
    db.session.add(comment45)
    db.session.add(comment46)
    db.session.add(comment47)
    db.session.add(comment48)
    db.session.add(comment49)
    db.session.add(comment50)
    db.session.add(comment51)
    db.session.add(comment52)
    db.session.add(comment53)
    db.session.add(comment54)
    db.session.add(comment55)
    db.session.add(comment56)
    db.session.add(comment57)
    db.session.add(comment58)
    db.session.add(comment59)
    db.session.add(comment60)
    db.session.add(comment61)
    db.session.add(comment62)
    db.session.add(comment63)
    db.session.add(comment64)
    db.session.add(comment65)
    db.session.add(comment66)
    db.session.add(comment67)
    db.session.add(comment68)
    db.session.add(comment69)
    db.session.add(comment70)
    db.session.add(comment71)
    db.session.add(comment72)
    db.session.add(comment73)
    db.session.add(comment74)
    db.session.add(comment75)
    db.session.add(comment76)
    db.session.add(comment77)
    db.session.add(comment78)
    db.session.add(comment79)
    db.session.add(comment80)
    db.session.add(comment81)
    db.session.add(comment82)
    db.session.add(comment83)
    db.session.add(comment84)
    db.session.add(comment85)
    db.session.add(comment86)
    db.session.add(comment87)
    db.session.add(comment88)
    db.session.add(comment89)
    db.session.add(comment90)
    db.session.add(comment91)
    db.session.add(comment92)
    db.session.add(comment93)
    db.session.add(comment94)
    db.session.add(comment95)
    db.session.add(comment96)
    db.session.add(comment97)
    db.session.add(comment98)
    db.session.add(comment99)
    db.session.add(comment100)
    db.session.add(comment101)
    db.session.add(comment102)
    db.session.add(comment103)
    db.session.add(comment104)
    db.session.add(comment105)
    db.session.add(comment106)
    db.session.add(comment107)
    db.session.add(comment108)
    db.session.add(comment109)
    db.session.add(comment110)
    db.session.add(comment111)
    db.session.add(comment112)
    db.session.add(comment113)
    db.session.add(comment114)
    db.session.add(comment115)
    db.session.add(comment116)
    db.session.add(comment117)
    db.session.add(comment118)
    db.session.add(comment119)
    db.session.add(comment120)
    db.session.add(comment121)
    db.session.add(comment122)
    db.session.add(comment123)
    db.session.add(comment124)
    db.session.add(comment125)
    db.session.add(comment126)
    db.session.add(comment127)
    db.session.add(comment128)
    db.session.add(comment129)
    db.session.add(comment130)
    db.session.add(comment131)
    db.session.add(comment132)
    db.session.add(comment133)
    db.session.add(comment134)
    db.session.add(comment135)
    db.session.add(comment136)
    db.session.add(comment137)
    db.session.add(comment138)
    db.session.add(comment139)
    db.session.add(comment140)
    db.session.add(comment141)
    db.session.add(comment142)
    db.session.add(comment143)
    db.session.add(comment144)
    db.session.add(comment145)
    db.session.add(comment146)
    db.session.add(comment147)
    db.session.add(comment148)
    db.session.add(comment149)
    db.session.add(comment150)
    db.session.add(comment151)
    db.session.add(comment152)
    db.session.add(comment153)
    db.session.add(comment154)
    db.session.add(comment155)
    db.session.add(comment156)
    db.session.add(comment157)
    db.session.add(comment158)
    db.session.add(comment159)
    db.session.add(comment160)
    db.session.add(comment161)
    db.session.add(comment162)
    db.session.add(comment163)
    db.session.add(comment164)
    db.session.add(comment165)
    db.session.add(comment166)
    db.session.add(comment167)
    db.session.add(comment168)
    db.session.add(comment169)
    db.session.add(comment170)
    db.session.add(comment171)
    db.session.add(comment172)
    db.session.add(comment173)
    db.session.add(comment174)
    db.session.add(comment175)
    db.session.add(comment176)
    db.session.add(comment177)
    db.session.add(comment178)
    db.session.add(comment179)
    db.session.add(comment180)
    db.session.add(comment181)
    db.session.add(comment182)
    db.session.add(comment183)
    db.session.add(comment184)
    db.session.add(comment185)
    db.session.add(comment186)
    db.session.add(comment187)
    db.session.add(comment188)
    db.session.add(comment189)
    db.session.add(comment190)
    db.session.add(comment191)
    db.session.add(comment192)
    db.session.add(comment193)
    db.session.add(comment194)
    db.session.add(comment195)
    db.session.add(comment196)
    db.session.add(comment197)
    db.session.add(comment198)
    db.session.add(comment199)
    db.session.add(comment200)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the comments table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_seed_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
