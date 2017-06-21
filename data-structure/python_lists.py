"""
Lists:
- We can put different types of data in a same lists
- We can access the value from the list with the index (index start from 0)
- Lists are mutable meaning we can change lists after we have created them
"""

# Define/create a list
my_list = [1, 2, 3, 4, 5]

# Accessing the first value from the list
print(my_list[0]) # output --> 1

# Accessing the last value from the list
print(my_list[4]) # output --> 5

# Accessing all the value from the lists
item = 0
while item < len(my_list):
    print("my_list[%d] --> %s" % (item, my_list[item]))
    item = item + 1

# print color of my choice from the list
colors = ["red", 'green', 'yellow', 'blue']
# add item to the list
colors.append("while")
# insert an item to the list - it will add an item into a specific index
colors.insert(4, "black")
# delete an item from the list
colors.remove("yellow")
i = 0
while i < len(colors):
    print("When I was %d, my favorite color was %s" % (i, colors[i]))
    i = i + 1

# print list of even number - using list comprehension
print ([x for x in range(2, 10) if not x % 2])

