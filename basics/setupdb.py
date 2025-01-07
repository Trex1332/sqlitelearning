from base import db, character,app

with app.app_context():
#creates all the tabels

    db.create_all()

    sam = character('Sam','Rien')
    frank = character('Frank','Doom')

    print(sam.id)
    print(frank.id)


    db.session.add_all([sam,frank])


    db.session.commit()

    print(sam.id)
    print(frank.id)