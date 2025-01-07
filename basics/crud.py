from base import db, character, app

with app.app_context():

    #creates
    myc = character('John','Sombra')
    db.session.add(myc)
    db.session.commit()

    #read
    allusers = character.query.all() #list of character objjects in tabel
    print(allusers)

    #select id
    c1 = character.query.get(1)
    print(c1.name)

    #filter
    sombra = character.query.filter_by(characters='Sombra')
    print(sombra.all())


#update
    firstcharcter = character.query.get(1)
    firstcharcter.characters = 'Doomfist'
    db.session.add(firstcharcter)
    db.session.commit()

    #delete

    second = character.query.get(2)
    db.session.delete(second)
    db.session.commit()

    allusers = character.query.all()
    print(allusers)
