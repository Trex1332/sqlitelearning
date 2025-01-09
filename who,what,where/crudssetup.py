from base import db, whowhatwhere, app

with app.app_context():

    name = str(input("Whats Your Name? "))
    game = str(input("Which game is your favorite character from? "))
    characte = str(input("Who are they? "))


    new = whowhatwhere(name,game,characte)
    db.session.add(new)
    db.session.commit()

    all = whowhatwhere.query.all()
    for i in all:
        print(i)
        print(" \n")