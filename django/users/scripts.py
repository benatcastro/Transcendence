from .models import TranscendenceUser
from match_history.models import MatchEntry
from django.db import IntegrityError

def delete_mockup_users(num_users):
    for i in range(num_users):
        try:
            username = f'user{i}'
            user = TranscendenceUser.objects.get(username=username)
            user.delete()
            print(f"User '{username}' has been deleted.")
        except TranscendenceUser.DoesNotExist:
            print(f"User '{username}' does not exist.")

def create_mockup_users(num_users):
    for i in range(num_users):
        print(f"creating user: '{i}' created.")
        username = f'user{i}'
        email = f'user{i}@example.com'
        password = 'password123'  # You can change this as per your requirements
        
        try:
            user, created = TranscendenceUser.objects.get_or_create(username=username, email=email, password=password)

            if created:
                print(f"User '{username}' created.")
            else:
                print(f"User '{username}' already exists.")

        except IntegrityError:
            print(f"Integrity error creating user '{username}'.")

def create_match_history_mockup(iterations, username1='user1', username2='user2'):
    create_mockup_users(iterations)
    user1 = TranscendenceUser.objects.get(username=username1)
    user2 = TranscendenceUser.objects.get(username=username2)
    for i in range(iterations):
       MatchEntry.objects.create(winner=user1, loser=user2) 
    for i in range(iterations):
       MatchEntry.objects.create(winner=user2, loser=user1) 