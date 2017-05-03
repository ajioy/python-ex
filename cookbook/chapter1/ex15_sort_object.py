class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u:u.user_id))


users = [User(43), User(103), User(99)]
from operator import attrgetter
print("after sorted users")
print(sorted(users, key=attrgetter('user_id'))) 

max_user = max(users, key=attrgetter('user_id'))
print(max_user)
