s = {1, 5, 6, 7, "nishan"}
t = {90, 45, 23, "hello"}
s.add(45) #this adds 45 to the set
print(s,type(s))

print(len(s)) #len() gives the length of the set

s.remove(6) #this removes 6 from the set

s.pop() #pop() pops the random value and return the poped value

# s.clear() #this clear all the elements of the set

print(s.union(t)) #this union the set 's' amd set 't'


print(s.intersection(t)) #this returs the overlapping value of two sets
