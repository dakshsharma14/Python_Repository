from math import *

print("Hello World")

character_name = "John"
character_age = "35"

# boolean
isMale = True

print("My name is " + character_name + ",")

# working with the strings

phrase = "Daksh\nSharma"
print(phrase.lower())
print(phrase[0])

# working with numbers
print(2 * (6 + 7))
print(10 % 3)

my_num = 45
my_num2 = -7
print(str(my_num) + "this is a number but we will use string so no error is there")
print(abs(my_num2))
print(pow(3, 3))

print(ceil(3.7))
print(floor(3.7))

# getting input from someone
name = input("Enter you name: ")

print("Hey " + name)

# lets build a basic calculator
num1 = input("Enter the number 1 ")
num2 = input("Enter the number 2 ")
result = float(num1) + float(num2)

print(result)
#################################
color = input("Enter a color ")
plural = input("Enter a plural ")
celebrity = input("Enter a celebrity ")

print("Roses are " + color)
print(plural + " are blue")
print("I love " + celebrity)


def raise_to_the_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_the_power(3, 3))


# Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a statement : ")))
