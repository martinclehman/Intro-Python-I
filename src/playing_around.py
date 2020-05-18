"""
print("Hello, world!")

name = "Tim"

print(name)

greeting = "Hello, "
name = "Aaron"
print(greeting + name)

print("hello " + name)
print("hello " + "world")

print("hello ", name)
print(f'Hello, {name}')
"""

my_list = ['b', 'c', 'd']

my_list.append('a')

my_list[0] = 1

# print(my_list)

# for x in my_list: 
#     print(x)
#     print(x)

# for (let j = 0; j < my_list.length; j++) {  }

# for index in range(len(my_list)):
#     print(index, my_list[index])

# for (idx, el) in enumerate(my_list):
#     print(idx, el)

numbers = [1, 2, 3, 4, 5]

squares = [dog * dog for dog in numbers] # [1, 4, 9, 16, 25]
# print(squares)

squares = []

for num in numbers:
    squares.append(num * num)

# print(squares)

halves = [num / 2 for num in numbers]
# print(halves)

evens = [num for num in numbers if num % 2 == 0]
# print(evens)

names = ["andrea", "gwen", "stephanie", "sagdi", "yankho", "tim", "bobbyg", "oliver"]

# get all names that start with s
# also capitalize them
s_names = [name.capitalize() for name in names if name.startswith('s')]

# print(s_names)

names = ["ben", "bob", "barbara", "bart", "joe"]
b_names = [name[0].upper() + name[1:] for name in names if name.startswith("b")]
# print(b_names)


b_names = []
for name in names:
    if name.startswith('b'):
        b_name = name[0].upper() + name[1:]
        b_names.append(b_name)

# my_list[0] = 1
# "ben"[0] = "B" # this will not work! strings are immutable

# Program to demonstrate conditional operator 
a, b = 10, 20
min = a if a < b else b 
# print(min) 

# JS example: true ? console.log('this') : console.log('notthis') 
# const my_var = true ? "a" : "b";

# a, b = some_func()
# def my_func():
#     return (1, 2)

my_dict = {"a": 1, "b": (1, 2, 3, -5)}

print(my_dict)

# my_dict[key] = value
my_dict["c"] = 3
my_dict[1] = "d"

my_dict["a"] = 0

# print(my_dict)

for x in my_dict:
    print(f'{x} is the key and {my_dict[x]} is the value')

new_list = [1, 2, "a", (1, 2), {"a": 1}]

new_list[0] = "c"
# print(new_list)

my_tuple = ("a", 1, 3)

my_tuple = (-1, -2, "a", {"b": 1})
# print(my_tuple)

my_set = set()
set.add("a")

"""
lists: ordered
dictionaries: NOT ordered
sets: NOT ordered
"""