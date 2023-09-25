friends = ["daksh", "Rantej", "Sam", "Sumit"]
luck_numbers = [4, 5, 63, 46, 345, 343, 3]

print(friends[1])
# back of the list
print(friends[-1])
print(friends[1:])


friends[1] = "Sharma"
print(friends[1:3])

friends.extend(luck_numbers)
print(friends)

friends.append("keshi")
friends.insert(1, "Xavi")
print(friends)

# copy
friends2 = friends.copy()
print(friends2)