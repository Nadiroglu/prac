from app import app
from models import db, User, Event, Merch
from datetime import datetime

with app.app_context():

    print('Deleting data')

    db.session.query(User).delete()
    db.session.query(Event).delete()
    db.session.query(Merch).delete()

    # db.session.query(Message).delete()
    # db.session.query(Poll).delete()

    print('Creating users')
    print('Creating events')
    print('Creating merchs')

    user = User(username='nailowski', email='nail@gmail.com', password_hash ='nail123', first_name='Nail', last_name ='Osmanli', profile_picture_url ='abc', role ='User')
    organizer = User(username='ben', email='ben@gmail.com', password_hash ='ben123', first_name='Ben', last_name ='Cavins', profile_picture_url ='abc', role = 'Organizer')
    users = [user, organizer] 


    event1 = Event (
        title = 'Coding', 
        description = 'Coding event', 
        location = 'Brooklyn', 
        date_time = datetime.strptime('2024-04-15 19:00:00', '%Y-%m-%d %H:%M:%S'), 
        image_url = 'https://images.pexels.com/photos/19451448/pexels-photo-19451448/free-photo-of-two-people-sitting-at-a-table-with-a-laptop.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    
    event2 = Event (
        title = 'Writing', 
        description = 'Writing event', 
        location = 'Pittsburgh', 
        date_time = datetime.strptime('2024-05-15 19:00:00', '%Y-%m-%d %H:%M:%S'), 
        image_url = 'https://images.pexels.com/photos/768125/pexels-photo-768125.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')

    events = [event1, event2]

    merch1 = Merch(name = 'Shirt', description = 'better', price = '$25.00', image_url = 'https://images.pexels.com/photos/292999/pexels-photo-292999.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', event_id = 1)

    merch2 = Merch(name = 'Blouse', description = 'Worse', price = '$25.00', image_url = 'https://images.pexels.com/photos/1566412/pexels-photo-1566412.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', event_id = 2)

    merchs = [merch1, merch2]


    

    print('Users created successfully')

    db.session.add_all(users)
    db.session.add_all(events)
    db.session.add_all(merchs)
    db.session.commit()