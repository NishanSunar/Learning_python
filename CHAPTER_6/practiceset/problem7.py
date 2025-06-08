#write a program to find out whether a given post is talking about "nishan" or not

post = "Hey, Nishan is a good boy. He is a hard working boy."

if("Nishan".lower() in post.lower()):
    print("This post is talking about you.")
else:
    print("This post is not talking about you>")