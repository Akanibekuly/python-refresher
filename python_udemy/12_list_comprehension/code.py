friends=["Sam","Samantha","Sauron"]
starts_s=[friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)

print(friends==starts_s)
print("friends: ",id(friends), "starts_s: ",id(starts_s))