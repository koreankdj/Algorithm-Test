a = [1, 2, 3, 4, 5]
del a[0]
a.insert(3, a[0])
del a[0]

print(a)