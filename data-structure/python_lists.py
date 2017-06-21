# print list of even number
print ([x for x in range(2, 10) if not x % 2])

for i in range(2, 10):
    if not i % 2:
        print(i)

colors = ["red", 'green', 'yellow', 'blue']

i = 0
while i < len(colors):
    print("When I was %d, my favorite color was %s" % (i, colors[i]))
    i = i + 1