print("Welcome to the Game")
name = input("What is your name?\n")
name1 = input("What is your loved one's name?\n")

combined_name = name + name1
lower_name = combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l + o + v + e

love_total = int(str(true) + str(love))

if (love_total < 10) or (love_total > 90):
    print(f"Your love score is {love_total}, you go together like coke and mentos ")
elif (love_total >=40) and (love_total <= 50):
    print(f"Your love score is {love_total}, you go together alright ")
else:
    print(f"Your score is {love_total}")