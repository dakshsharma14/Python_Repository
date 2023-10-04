# List:  ordered, mutable, allows duplicate elements
mylist = ["Banana", "cherry", "apple", 5]
matrix = [[0, 1], [2, 3]]

# we can iterate through it
number = list(range(20))

print(number)
print(mylist)

item = mylist[0]
print(item)

for i in mylist:
    print(i)

if "Banana" in mylist:
    print("yes")
else:
    print("No")

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# unpacking the list
numbers = [1, 2, 3, 4, 5, 7, 8]
first, second, *other = numbers
print(other)

# loop through list
letters = ["a", "b", "c"]
# items = [0, "a"]
# index, letter = items

# if we use enumerate object, it will give us the tuple(enumerate(letters))
for index, letter in enumerate(letters):
    print(index, letter)

