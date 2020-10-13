from fbchat import Client
from fbchat.models import Message

# log in
# facebook user credentials
username = "username"
password = "password"
# login
client = Client(username, password)

# get 20 users you most recently talked to
users = client.fetchThreadList()
#print(users)

# # get the detailed informations about these users
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[1] for user in users ]

# # sort by number of messages
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)

# # print the best friend!
friend = sorted_detailed_users[1]
print("Friend:", friend.name, "with a message count of", friend.message_count)

# # message the friend!
client.send(Message(text=f"Congratulations {friend.name}, I just tested out my bot with you {friend.message_count} fear not!"), thread_id=friend.uid)


# get all users you talked to in messenger in your account
all_users = client.fetchAllUsers()
print("You talked with a total of", len(all_users), "users!")

# # let's logout
# client.logout()