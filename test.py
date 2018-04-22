t = range(4)

t1 = (i for i in t)
t2 = (i for i in t1)

print(list(t1))
print(list(t2))