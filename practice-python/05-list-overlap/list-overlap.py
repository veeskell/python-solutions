import random

def rand_list(size):
    l=[]
    for elem in range(size):
        l.append(random.randint(0,20))
    return l

a = rand_list(random.randint(0,10))
b = rand_list(random.randint(0,10))

print(a)
print(b)

c=[]
for elem in a:
    if elem in b and elem not in c:
        c.append(elem)

print(c)
