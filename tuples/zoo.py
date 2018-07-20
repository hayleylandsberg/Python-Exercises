# 1. Create a tuple named zoo that contains your favorite animals.
zoo = ('dog', 'cat', 'bird')
print(zoo)
# 2. Find one of your animals using the .index(value) method on the tuple.
index = zoo.index('cat')
print(index)
# 3. Determine if an animal is in your tuple by using for value in tuple.

# 4. Create a variable for each of the animals in your tuple with this cool feature of Python.

# # example
# (lizard, fox, mammoth) = zoo
# print(lizard)
# 5. Convert your tuple into a list.
zoo_list = list(zoo)
# 6. Use extend() to add three more animals to your zoo.
zoo_list.extend(['turtle', 'rabbit', 'fish'])
print(zoo_list)

# 7. Convert the list back into a tuple.
zoo_tuple = tuple(zoo_list)
print(zoo_tuple)
