#Hello World
print('Hello World !!!')
print()

# Identifier
num1 = 10
num2 = 10.5
str1 = 'Manoj Pal'
add = """House no 100,
     Pune, Maharashtra,
     India"""
can_vote = False


print(f"num1: {num1} and Type of num1: {type(num1)}")
print(f"num2: {num2} and Type of num2: {type(num2)}")
print(f"str1: {str1} and Type of str1: {type(str1)}")
print(f"add: {add} and Type of add: {type(add)}")
print(f"can vote: {can_vote} and Type of can_vote: {type(can_vote)}")

print()

# Operator
num1 = 11
num2 = 20

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num2 - num1}")
print(f"Multiplication: {num1 * num2}")
print(f"True Division(o/p - float): {num2/num1} and type of the result is {type(num2/num1)}")
print(f"Floor Division(o/p - int): {num2//num1} and type of the result is {type(num2//num1)}")
print(f"Power: {2**5}")

# Comparison
print(f"num1 >= num2: {num1 >= num2}")
print(f"num1 <= num2: {num1 <= num2}")
print(f"num1 == num2: {num1 == num2}")
print(f"num1 != num2: {num1 != num2}")

# If Else

if num2 > num1:
    print(f"num2 {num2} is greater than num1 {num1}.")
elif num1 == num2:
    print(f"num2 {num2} is equal to num1 {num1}.")
else:
    print(f"num2 {num2} is less than num1 {num1}.")