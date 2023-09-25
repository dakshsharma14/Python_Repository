is_male = True
is_tall = False

if is_male and is_tall:
    print("you are a male")
elif is_male and not is_tall:
    print("Not tall but male")
elif not is_male and is_tall:
    print("you are not male but tall")
else:

    print("You are not a male")


#2d list
numbers_grid = [
    [3,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(numbers_grid[0][1])

for row in numbers_grid:
    for col in row:
        print(col)




# calculating the max value that a user inputs
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num2 and num3 >= num1:
        return num3


print(max_num(3, 5, 9))


# building a better calculator
x = float(input("enter a number 1 "))
op = input("enter a operator ")
y = float(input("enter a number 2 "))

if op == "+":
    print(x + y)
elif op == "-":
    print(x-y)
elif op == "/":
    print(x/y)
elif op == "*":
    print(x*y)
else:
    print("invalid operator")
