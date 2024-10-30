from app import app
from models import db, User
from datetime import datetime

with app.app_context():

    print('Deleting data')

    db.session.query(User).delete()

    # db.session.query(Message).delete()
    # db.session.query(Poll).delete()

    print('Creating users')

    user = User(username='nailowski', email='nail@gmail.com', password_hash ='nail123', first_name='Nail', last_name ='Osmanli', profile_picture_url ='abc', role ='User')
    organizer = User(username='ben', email='ben@gmail.com', password_hash ='ben123', first_name='Ben', last_name ='Cavins', profile_picture_url ='abc', role = 'Organizer')
    users = [user, organizer] 

    

    print('Users created successfully')

    db.session.add_all(users)
    db.session.commit()