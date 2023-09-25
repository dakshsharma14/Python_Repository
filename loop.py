i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

##############################################
secret_word = "animal"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if guess_count <= guess_limit:
        guess = input("guess a word ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("you are out of guess")
else:
    print("You won")
print("Great")

######################################
friend = ["dadfad", "adsgfasfga", "asdfgaefa"]
for index in range(10):
    print(index)
print()
for ind in range(3,10):
    print(ind)

print("range")
for leng in range(len(friend)):
    print(friend[leng])