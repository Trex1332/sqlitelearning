#add to tables
from models import db,books,source,person,app

with app.app_context():
    book1 = books("atomic habit")
    book2 = books("SAONGAF")

    db.session.add_all([book1,book2])
    db.session.commit()

    print(books.query.all())

    book1 = books.query.filter_by(name='atomic habit').first()
    print(book1)

    bob = person('bob',book1.id)

    source1 = source("idk",book1.id)
    source2 = source("idk2",book1.id)

    db.session.add_all([bob,source1,source2])
    db.session.commit()

    book1 = books.query.filter_by(name='atomic habit').first()

    print(book1)