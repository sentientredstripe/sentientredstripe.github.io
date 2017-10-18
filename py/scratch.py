y=3
z=22
w=z//y
print(w)
for num in range(w):
    if num % 3 == 0:
        z = z + 1
        print(z)