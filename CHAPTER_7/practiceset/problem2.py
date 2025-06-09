#write a program to greet all the person names stored in a list "L" and which starts with S.

L = ['Nishan', 'Sumit', 'Kishor', 'Sandesh', 'Ram']

for name in L:
    if(name.startswith("S")):
        print(f"Hello {name}")
        
