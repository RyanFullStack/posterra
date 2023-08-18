from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_posts():
    post1 = Post(
        created_by=9, community_id=1, post_title='The New American Gothic', post_body='Oil on canvas, 2017, Criselda Vesquez', ext_url='https://drive.google.com/uc?id=13IpRkqZ6tqnxFFT1or6-7f7MM6eeQav-'
    )
    post2 = Post(
        created_by=10, community_id=1, post_title='The Making of the Perfect Martini', post_body='Lithography, 2000, Guy Buffet', ext_url='https://drive.google.com/uc?id=1DOYd7t4HzLMyyyYLRUE5kPNU2Sz8mY3_'
    )
    post33 = Post(
        created_by=2, community_id=1, post_title='Leaving the house with wet hair in the Midwest...', post_body='Hair art?...', ext_url='https://drive.google.com/uc?id=1yg4MfrIgOw-DCxYjsyzwdCfolaeskiXk'
    )
    post34 = Post(
        created_by=8, community_id=1, post_title='Enjoy the moment', ext_url='https://drive.google.com/uc?id=1V5RiEdYVpYHihpPj8KevpeKvejtHQiAD'
    )
    post35 = Post(
        created_by=5, community_id=1, post_title='Disneyland Tokyo is making a Beauty and the Beast ride, the animatronics look insane', ext_url='https://drive.google.com/uc?id=1HVC6-g0sG3aZuFQeO0CbbdSa5Rvjst5j'
    )
    post3 = Post(
        created_by=1, community_id=2, post_title='What if God came down one day and said', post_body="'Its pronounced Jod' then left?"
    )
    post4 = Post(
        created_by=2, community_id=2, post_title="Bill Gates said, 'I will always choose a lazy person to do a difficult job because a lazy person will find an easy way to do it.'", post_body='Whats a real-life example of this?'
    )
    post36 = Post(
        created_by=13, community_id=2, post_title="1 dad reflex 2 children", post_body='How is this even possible?', ext_url='https://drive.google.com/uc?id=1gyCcfYj7ofz4OKKI6ihp-MG3bLec8yDg'
    )
    post37 = Post(
        created_by=10, community_id=2, post_title="How long does it take to learn this?", ext_url='https://drive.google.com/uc?id=1_tlqRckuyvLahIOh-XCWHlygyVh8_RQK'
    )
    post38 = Post(
        created_by=8, community_id=2, post_title="Would you watch a show where a billionaire CEO has to go an entire month on their lowest paid employees salary, without access to any other resources than that of the employee?", post_body='What do you think would happen?'
    )
    post5 = Post(
        created_by=2, community_id=3, post_title='Illinois House passes bill prohibiting book bans', ext_url='https://www.wgem.com/2023/03/23/illinois-house-passes-bill-prohibiting-book-bans/'
    )
    post6 = Post(
        created_by=6, community_id=3, post_title='Textbook costs have risen nearly 1000 percent since the 70s', ext_url='https://www.vox.com/the-goods/2019/3/6/18252322/college-textbooks-cost-expensive-pearson-cengage-mcgraw-hill'
    )
    post39 = Post(
        created_by=12, community_id=3, post_title='Living with a fox', ext_url='https://drive.google.com/uc?id=1fHrabwxkTb-_yXWqFZWV7H_gRrmiBP5I'
    )
    post40 = Post(
        created_by=6, community_id=3, post_title='More people visit their library than attend the NFL, NHL, NBA, Nascar, or the movie theater COMBINED.', ext_url='https://www.libraries2020.org/but_nobody_uses_libraries_anymore'
    )
    post41 = Post(
        created_by=6, community_id=3, post_title='I hate when the back of a book is devoid of a synopsis and is replaced with critical acclaim', post_body="Just something that I find quite annoying when looking for a new book, especially when trying to pick up a classic. I don't mind if there's a few reviews or even an opening paragraph that talks about the novels success but please give me some idea of what its actually about."
    )
    post7 = Post(
        created_by=6, community_id=4, post_title='[I ate] a taco box', post_body='Soo good!', ext_url='https://drive.google.com/uc?id=1DK7FZPHss2-AsVRScGbYSPDVV5BDb8xz'
    )
    post8 = Post(
        created_by=11, community_id=4, post_title="[Pro/Chef] 'Raspbaby Yoda' Raspberry Pie", ext_url='https://drive.google.com/uc?id=1nlBfm2PYbTqkzCG5JSmHsnCAR9zPDb9p'
    )
    post42 = Post(
        created_by=7, community_id=4, post_title="[Homemade] Crunchwrap Supreme", ext_url='https://drive.google.com/uc?id=1y92JRPsnNTZ6GrR8wDPxp1rI7XKYrTYF'
    )
    post43 = Post(
        created_by=2, community_id=4, post_title="Grandmas delicious 21 layer jello", ext_url='https://drive.google.com/uc?id=13fTcf-e_mruYfcHSAC5MThkQD2ZxMN_y'
    )
    post44 = Post(
        created_by=13, community_id=4, post_title="[Pro/Chef] Tantanmen Ramen with chicken", ext_url='https://drive.google.com/uc?id=1ReqcGa32GuE3i6IvKeP5ERiAS_s6F078'
    )
    post9 = Post(
        created_by=11, community_id=5, post_title='Sheep in Human Clothing', ext_url='https://drive.google.com/uc?id=1neYGdPTKBQ-fh3E21vXKvLiloWdvlyRd'
    )
    post10 = Post(
        created_by=10, community_id=5, post_title='UPDATE. EA announces plans for next gen controller.', post_body='As expected.', ext_url='https://drive.google.com/uc?id=1eiopBe7p2uUrd8rC_-7Pto4HCRl3n9wF'
    )
    post45 = Post(
        created_by=2, community_id=5, post_title='Trump boards Air Force One with toilet paper stuck to his shoe', ext_url='https://drive.google.com/uc?id=1afc_-kwuHFdlsEo3az_MtieYM9ZF6YrO'
    )
    post46 = Post(
        created_by=9, community_id=5, post_title="It's all downhill from here.", ext_url='https://drive.google.com/uc?id=1iF8CRBMozUptkRIWFRKAFCqKzDaaS9oZ'
    )
    post47 = Post(
        created_by=6, community_id=5, post_title='A true gentleman', ext_url='https://drive.google.com/uc?id=1lFUOfJuEvlp_FnPJAc7Vrpxd-qgyrxjM'
    )
    post11 = Post(
        created_by=14, community_id=6, post_title='Minesweeper 99 x 99, 1500 mines. Took me about 2.5 hours to finish, nerve-wracking.', post_body='No one might care, but just wanted to share this.', ext_url='https://drive.google.com/uc?id=1ykYVEhXHw9pdLZZMGXZkPZFfa_EPn93M'
    )
    post12 = Post(
        created_by=4, community_id=6, post_title='Jerry', ext_url='https://drive.google.com/uc?id=12cPYdYh32cpkwnAvsg9zzuxi88XGRoyb'
    )
    post48 = Post(
        created_by=8, community_id=6, post_title='Surgical precision...', post_body='Me in GTA', ext_url='https://drive.google.com/uc?id=1GhZiE-uzVg3nU4FZ4XZAMRhHi3lHKJae'
    )
    post49 = Post(
        created_by=10, community_id=6, post_title='Poor bird', ext_url='https://drive.google.com/uc?id=1szOxcabBZ6Oot99oLxLCabdl1uk8T07V'
    )
    post50 = Post(
        created_by=12, community_id=6, post_title='The Silver Snipers are a CS:GO team in Sweden where the youngest member is 62 and the oldest 81. They say playing CS has helped to give them a confidence boost and serve as a sort of mental gymnastics', ext_url='https://drive.google.com/uc?id=1ejSV772hs0_vgy4ZdEtXdVpqVh_nbT00'
    )
    post13 = Post(
        created_by=13, community_id=7, post_title='3,000-year-old underwater castle discovered in Turkeys largest lake', ext_url='https://inhabitat.com/3000-year-old-underwater-castle-discovered-in-turkeys-largest-lake/'
    )
    post14 = Post(
        created_by=2, community_id=7, post_title='700 year old Knights Templar cave discovered in England', ext_url='https://www.bbc.com/news/uk-england-39193347'
    )
    post51 = Post(
        created_by=7, community_id=7, post_title='Bush cracks joke to Obama while Clinton makes a speech', ext_url='https://drive.google.com/uc?id=1ES5d7ILRNrtxf1zQUR8LTwfsbxQ8ajW8'
    )
    post52 = Post(
        created_by=8, community_id=7, post_title='Scientists reconstruct the face of a man who died in Cambridgeshire 700 years ago, revealing what an ordinary 13th century man looked like', ext_url='https://www.independent.co.uk/news/science/archaeology/average-13th-century-man-look-like-difference-cambridge-dundee-university-chris-rynn-john-robb-a7640886.html'
    )
    post53 = Post(
        created_by=1, community_id=7, post_title='A Lot of What Is Known about Pirates Is Not True, and a Lot of What Is True Is Not Known', ext_url='https://www.neh.gov/humanities/2017/winter/feature/lot-what-known-about-pirates-not-true-and-lot-what-true-not-known'
    )
    post15 = Post(
        created_by=4, community_id=8, post_title="Tom Hanks as Mister Rogers on the set of 'You Are My Friend'", post_body='We miss you, Mister Rogers!', ext_url='https://drive.google.com/uc?id=12RkeR0y08fPhl1-2oDGaF39ykI3l3R2h'
    )
    post16 = Post(
        created_by=8, community_id=8, post_title="This 'Deadpool 2' poster", post_body='My favorite poster by far. What do you think?', ext_url='https://drive.google.com/uc?id=14WV3hv8oBYXE0AIsLidPlgwyBjZcebEi'
    )
    post54 = Post(
        created_by=14, community_id=8, post_title="Courtney Love warning about Harvery Weinstein in 2005", ext_url='https://drive.google.com/uc?id=1wqtY8xzcQXSLfwPGsgWSJ3hcnd1oQjbz'
    )
    post55 = Post(
        created_by=12, community_id=8, post_title="Leonardo DiCaprio gets his Oscar engraved", ext_url='https://drive.google.com/uc?id=14CzXnag7GrfJc8qAQQPvv8_e6R0mfwYL'
    )
    post56 = Post(
        created_by=11, community_id=8, post_title="Buster Keaton gets rejected by a hatcheck girl without a word being spoken in Seven Chances (1925)", ext_url='https://drive.google.com/uc?id=140PTSIR9u4n-HaaACY2OgKFeqHKT0zMp'
    )
    post17 = Post(
        created_by=5, community_id=9, post_title='A song I wrote just for Posterra', post_body='Enjoy!', ext_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    )
    post18 = Post(
        created_by=14, community_id=9, post_title="Jamie Lee Curtis leading the charge for earlier concerts: 'I want to hear Coldplay at 1PM'", ext_url='https://www.audacy.com/1053davefm/news/jamie-lee-curtis-leading-the-charge-for-earlier-concerts'
    )
    post57 = Post(
        created_by=3, community_id=9, post_title="Weird Al just got his star on the Walk of Fame", ext_url='https://drive.google.com/uc?id=1--D8lqD65Q6cOeJS-3ofm_Gd-CU2wg0d'
    )
    post58 = Post(
        created_by=7, community_id=9, post_title="Two dudes make their own party outside the club", ext_url='https://drive.google.com/uc?id=1cZ-jKPHZ0y7smjJu20RgPSH2vMlh0LHQ'
    )
    post59 = Post(
        created_by=5, community_id=9, post_title="Eminem was interviewed by the Secret Service over his anti-Trump lyrics and then rapped along when they read them to him", ext_url='https://variety.com/2019/music/news/eminem-trump-ivanka-secret-service-1203382499/'
    )
    post19 = Post(
        created_by=8, community_id=10, post_title='Campbell will acquire Raos premium sauces parent company for $2.7 billion', ext_url='https://abcnews.go.com/GMA/Food/campbell-acquire-raos-premium-sauces-parent-company-27/story?id=102071512'
    )
    post20 = Post(
        created_by=1, community_id=10, post_title='Volunteer divers find 32 submerged cars in Doral lake, possibly linked to missing persons cold cases', post_body='More details to be released soon.', ext_url='https://wsvn.com/news/local/miami-dade/volunteer-divers-find-32-submerged-cars-in-doral-lake-possibly-linked-to-missing-persons-cold-cases/'
    )
    post60 = Post(
        created_by=3, community_id=10, post_title='News for today:', post_body='Slippery as hell!', ext_url='https://drive.google.com/uc?id=1pL-KH046rlsYV47jVQYHRAYsOOKjXmw6'
    )
    post61 = Post(
        created_by=5, community_id=10, post_title="Homeowner snags purse from package thief's car", post_body='The suspects were later arrested.', ext_url='https://drive.google.com/uc?id=1ccIJ-a1aP2Wk_fLjFdVtB_exl85QREei'
    )
    post62 = Post(
        created_by=12, community_id=10, post_title='Hot Fuzz guys spotted in the London Attack', ext_url='https://drive.google.com/uc?id=1maJSbP7SVuI47q513KrnpI-j0ALzYWcX'
    )
    post21 = Post(
        created_by=10, community_id=11, post_title='Oregon wildfires making it look straight apocalyptic', ext_url='https://drive.google.com/uc?id=1UoKeH-dF06UU2r9dno0rwZJPQm09R7K5'
    )
    post22 = Post(
        created_by=9, community_id=11, post_title='Meeting Keanu Reeves at a traffic light', ext_url='https://drive.google.com/uc?id=1Tq97LIdtSBcZ1qV0Xsoi8fDvTLlso7rX'
    )
    post63 = Post(
        created_by=12, community_id=11, post_title='Getting that perfect headshot', ext_url='https://drive.google.com/uc?id=1gRX6HeqEzsufGDNpFZI90daK5yaJgVrI'
    )
    post64 = Post(
        created_by=9, community_id=11, post_title='This is Dr Katie Bouman the computer scientist behind the first ever image of a black-hole. She developed the algorithm that turned telescopic data into the historic photo we see today.', ext_url='https://drive.google.com/uc?id=1dxngyty_1QUxWbzf28HqU0My3_wtnsvq'
    )
    post65 = Post(
        created_by=9, community_id=11, post_title="They noticed there was a blank wall at mcdonald's so they decided to make this fake poster of themselves. It's now been 51 days since they hung it up.", ext_url='https://drive.google.com/uc?id=1v-bH_9Z-Z6UR7kQXEkDKQzdySQWdvvor'
    )
    post23 = Post(
        created_by=12, community_id=12, post_title="Scientists believe that the function of zebras' stripes are to deter insects", post_body='A team of researchers painted black and white stripes on cows. They found that it reduced the number of biting flies landing on the cows by more than 50%.', ext_url='https://www.realclearscience.com/quick_and_clear_science/2019/10/07/painting_zebra_stripes_on_cows_wards_off_biting_flies.html'
    )
    post24 = Post(
        created_by=3, community_id=12, post_title='In Seattle, Washington, delaying the start time of two high schools by nearly an hour lengthened students daily sleep by more than half an hour, and was associated with reduced sleepiness and increased academic performance.', ext_url='https://www.eurekalert.org/news-releases/528060'
    )
    post66 = Post(
        created_by=10, community_id=12, post_title='Fighting litter with crows', ext_url='https://drive.google.com/uc?id=1l9bDLpX-NoFQYHfDnyCDaYH3fgyR3aPT'
    )
    post67 = Post(
        created_by=8, community_id=12, post_title='Spinning a skateboard wheel so fast the centripetal force rips it apart', ext_url='https://drive.google.com/uc?id=1__wniS3Dhr9bwwbz8bPHObLIRzvOFbGQ'
    )
    post68 = Post(
        created_by=1, community_id=12, post_title='Slow reaction time', ext_url='https://drive.google.com/uc?id=1e4W5kF7FYu10iyuB_YcdaTFQb6s2GMkh'
    )
    post25 = Post(
        created_by=3, community_id=13, post_title='First full-colour Image of deep space from the James Webb Space Telescope revealed by NASA (in 4k)', post_body='We are so small.', ext_url='https://drive.google.com/uc?id=1uOT6uc7iJV3NKwlywBJrymbB_CMnrDSJ'
    )
    post26 = Post(
        created_by=13, community_id=13, post_title='I took nearly 50,000 images of the night sky to make an 81 Megapixel image of the moon.', ext_url='https://drive.google.com/uc?id=1Ym0RDxULKsLJFlmTYo3t8JIFijEmEPZW'
    )
    post69 = Post(
        created_by=4, community_id=13, post_title='By complete accident I captured a plane crossing in front of our sun. I was able to figure out exactly which flight it was and got connected with the pilot, who was thrilled.', ext_url='https://drive.google.com/uc?id=14lGlqS9-6ByNavLMuRfZX2SjdafkJWD1'
    )
    post70 = Post(
        created_by=2, community_id=13, post_title='The clearest image of Mars ever taken!', ext_url='https://drive.google.com/uc?id=1OYsLAMTr_xR7O6uf0Qx492NU26vCGSCQ'
    )
    post71 = Post(
        created_by=11, community_id=13, post_title="Astronaut Samantha Cristoforetti Wears 'Star Trek' Uniform in Space", ext_url='https://drive.google.com/uc?id=1FD1_9lB2ucMblnISpkDJqzAFoewMG9C4'
    )
    post27 = Post(
        created_by=7, community_id=14, post_title='The Monterrey Stadium. Mexico.', post_body='My favorite place to go!', ext_url='https://drive.google.com/uc?id=1LuW8TR4fGnICyXwLWUizGcCgG9s_slYD'
    )
    post28 = Post(
        created_by=3, community_id=14, post_title='What 10,000 horsepower does to a drag tire at launch', ext_url='https://drive.google.com/uc?id=13TGtHlMFgHRSu_1PBNat7T8-b1GOyDwA'
    )
    post72 = Post(
        created_by=9, community_id=14, post_title="His wife died in a car crash, he promised her he'd win gold", ext_url='https://drive.google.com/uc?id=17S-xl9bRil0SdBqGmmBHzBiQd5C-uV_6'
    )
    post73 = Post(
        created_by=10, community_id=14, post_title='School Science teacher dunks for his students', ext_url='https://drive.google.com/uc?id=1C8u3XlomXu_8DCW2uDumm0uzzSTzHALp'
    )
    post74 = Post(
        created_by=5, community_id=14, post_title='Coach puts on his professional face', ext_url='https://drive.google.com/uc?id=1NH9ImCMoGiCTT5o4_s_aWt4EPAyEyP0V'
    )
    post29 = Post(
        created_by=4, community_id=15, post_title="Stranger Things 5: Will Takes 'Center Stage' in final Season", ext_url='https://tvline.com/previews/stranger-things-season-5-spoilers-will-vecna-connection-1235024449/'
    )
    post30 = Post(
        created_by=7, community_id=15, post_title='Giving Back', post_body="'The Office' Star Leslie David Baker Is Giving Back $110,000 Worth of Fan Donations for Stalled Stanley Spinoff, Says Funds Were Never Used for Personal Matters", ext_url='https://variety.com/2023/tv/news/the-office-actor-returns-fan-donations-stnaley-spinoff-1235687187/'
    )
    post75 = Post(
        created_by=11, community_id=15, post_title='Mark Zuckerbot at his congress hearing', ext_url='https://drive.google.com/uc?id=1NmbEfUMx5V_N0GvgX7g4RG0kjUV6RK9F'
    )
    post76 = Post(
        created_by=5, community_id=15, post_title='Camera shutter speed synced to helicopter`s rotor', ext_url='https://drive.google.com/uc?id=1YUVw3Pn8o8u3MYXxBn6MqF0DJEOcAtMq'
    )
    post77 = Post(
        created_by=14, community_id=15, post_title="Captain Disillusion breaks down a fake America's Got Talent act and calls out the producers.", ext_url='https://www.youtube.com/watch?v=_dSp_f0f9gE'
    )
    post31 = Post(
        created_by=10, community_id=16, post_title='This is what happens when one company owns dozens of local news stations', post_body='Uncanny valley vibes...', ext_url='https://www.youtube.com/watch?v=hWLjYJ4BzvI&feature=youtu.be'
    )
    post32 = Post(
        created_by=9, community_id=16, post_title="Roughly the first five seconds of 'Never Gonna Give You Up' is now a silent Sony Music title card that displays copyright and licensing information, essentially ruining Rick Rolling", ext_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    )
    post78 = Post(
        created_by=1, community_id=16, post_title="Kids in Elementary school hold a surprise party for their beloved school custodian", ext_url='https://drive.google.com/uc?id=1Txlw6SnVfSQG6TotFyGYaCR9SNU8k2M0'
    )
    post79 = Post(
        created_by=3, community_id=16, post_title="You've seen a doggo reaction, but have you seen a birdo reaction?", ext_url='https://drive.google.com/uc?id=1kthtWkNIqwnOyQ3k58QBsXWO45eHQ1ce'
    )
    post80 = Post(
        created_by=11, community_id=16, post_title="Good boy saves small boy", ext_url='https://drive.google.com/uc?id=1zT0cKHkxH4mJhkbxMwvhSL2cOanZhnY9'
    )


    db.session.add(post72)
    db.session.add(post46)
    db.session.add(post60)
    db.session.add(post32)
    db.session.add(post45)
    db.session.add(post36)
    db.session.add(post57)
    db.session.add(post51)
    db.session.add(post75)
    db.session.add(post66)
    db.session.add(post30)
    db.session.add(post52)
    db.session.add(post4)
    db.session.add(post19)
    db.session.add(post62)
    db.session.add(post20)
    db.session.add(post58)
    db.session.add(post21)
    db.session.add(post22)
    db.session.add(post5)
    db.session.add(post44)
    db.session.add(post33)
    db.session.add(post43)
    db.session.add(post63)
    db.session.add(post41)
    db.session.add(post80)
    db.session.add(post73)
    db.session.add(post12)
    db.session.add(post78)
    db.session.add(post34)
    db.session.add(post47)
    db.session.add(post1)
    db.session.add(post15)
    db.session.add(post17)
    db.session.add(post18)
    db.session.add(post79)
    db.session.add(post9)
    db.session.add(post31)
    db.session.add(post49)
    db.session.add(post55)
    db.session.add(post11)
    db.session.add(post39)
    db.session.add(post61)
    db.session.add(post67)
    db.session.add(post8)
    db.session.add(post74)
    db.session.add(post42)
    db.session.add(post48)
    db.session.add(post37)
    db.session.add(post10)
    db.session.add(post16)
    db.session.add(post13)
    db.session.add(post50)
    db.session.add(post59)
    db.session.add(post76)
    db.session.add(post35)
    db.session.add(post70)
    db.session.add(post64)
    db.session.add(post68)
    db.session.add(post38)
    db.session.add(post7)
    db.session.add(post40)
    db.session.add(post14)
    db.session.add(post3)
    db.session.add(post53)
    db.session.add(post56)
    db.session.add(post65)
    db.session.add(post69)
    db.session.add(post23)
    db.session.add(post54)
    db.session.add(post24)
    db.session.add(post25)
    db.session.add(post26)
    db.session.add(post27)
    db.session.add(post29)
    db.session.add(post6)
    db.session.add(post2)
    db.session.add(post71)
    db.session.add(post28)
    db.session.add(post77)

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
