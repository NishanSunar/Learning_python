#spam detector

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter something")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("The comment is spam")
else:
    print("This comment is not spam")