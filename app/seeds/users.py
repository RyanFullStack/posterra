from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    doug = User( #1
        username='altitude', first_name='Doug', last_name='Smith', email='doug@aa.io', password='password', bio='Aviation Enthusiast/Business Owner', profile_pic='/userpics/doug.jpg'
    )
    chris = User( #2
        username='theforceisstrong', first_name='Chris', last_name='Rea', email='chris@aa.io', password='password', bio='Skydiving Safety Director', profile_pic='/userpics/chris.png'
    )
    dave = User( #3
        username='pilotguy', first_name='Dave', last_name='Guendner', email='dave@aa.io', password='password', bio='Commercial Pilot', profile_pic='/userpics/dave.png'
    )
    ryann = User( #4
        username='ryannnnnn', first_name='Ryann', last_name='Nicosia', email='ryann@aa.io', password='password', bio="Killing it since '90", profile_pic='/userpics/ryann.png'
    )
    dillon = User( #5
        username='dailon', first_name='Dillon', last_name='Perez', email='dillon@aa.io', password='password', bio='DJ Party extraordinaire', profile_pic='/userpics/dillon.png'
    )
    melissa = User( #6
        username='snackattack', first_name='Melissa', last_name='Moore', email='melissa@aa.io', password='password', bio='Brings all the snacks!', profile_pic='/userpics/melissa.png'
    )
    emily = User( #7
        username='emilyisapro', first_name='Emily', last_name='Ferenc', email='emily@aa.io', password='password', bio='Ex-pro basketball player', profile_pic='/userpics/emily.png'
    )
    natalie = User( #8
        username='nat', first_name='Natalie', last_name='Rodriguez', email='natalie@aa.io', password='password', bio='Events coordinator', profile_pic='/userpics/natalie.jpg'
    )
    haley = User( #9
        username='hayyo', first_name='Haley', last_name='Toon', email='haley@aa.io', password='password', bio='Videographer/Artist', profile_pic='/userpics/haley.png'
    )
    hunter = User( #10
        username='hunt', first_name='Hunter', last_name='Amundson', email='hunter@aa.io', password='password', bio='Pro Skydiver/Coach', profile_pic='/userpics/hunter.jpg'
    )
    kayleigh = User( #11
        username='kaykay', first_name='Kayleigh', last_name='Trosper', email='kayleigh@aa.io', password='password', bio='Best bartender in the biz!', profile_pic='/userpics/kayleigh.jpg'
    )
    annalise = User( #12
        username='airmedic', first_name='Annalise', last_name='Eure', email='annalise@aa.io', password='password', bio='Air Medic', profile_pic='/userpics/annalise.png'
    )
    nacho = User( #13
        username='nacho', first_name='Mark', last_name='Perez', email='nacho@aa.io', password='password', bio='Pilot for the highrollers', profile_pic='/userpics/nacho.png'
    )
    sparky = User( #14
        username='sparky', first_name='Eric', last_name='Strydom', email='sparky@aa.io', password='password', bio='Gets struck by lightning', profile_pic='/userpics/sparky.jpg'
    )


    db.session.add(doug)
    db.session.add(chris)
    db.session.add(dave)
    db.session.add(ryann)
    db.session.add(dillon)
    db.session.add(melissa)
    db.session.add(emily)
    db.session.add(natalie)
    db.session.add(haley)
    db.session.add(hunter)
    db.session.add(kayleigh)
    db.session.add(annalise)
    db.session.add(nacho)
    db.session.add(sparky)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
