from base import db,whowhatwhere,app

with app.app_context():
#creates all the tabels

    db.create_all()