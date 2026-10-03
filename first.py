
# a=5
# b=5
# print(a+b)

# print("This is first Python program")

# integer_value = 10
# float_value = 10.5
# double_value = 10.58
# character_value = 'A'
# boolean_value = True

# print("Integer Value:", integer_value)
# print("Float Value:", float_value)
# print("Double Value:", double_value)
# print("Character Value:", character_value)
# print("Boolean Value:", boolean_value)

# number1=20
# number2=5
# print("Addition:", number1 + number2)
# print("Subtraction:", number1 - number2)
# print("Multiplication:", number1 * number2) 
# print("Division:", number1 / number2)
# print("Modulus:", number1 % number2)
# print("Exponentiation:", number1 ** number2)
# print("Floor Division:", number1 // number2)
# print("Comparison (number1 > number2):", number1 > number2)
# print("Comparison (number1 < number2):", number1 < number2)

# length=10
# breadth=5
# print("Area=", length*breadth)

# radius=7
# print("Radius of circle:",2*radius)
# print("Area of circle:",3.14*radius*radius)
# print("Circumference of circle:",2*3.14*radius)


# centimeter=150
# print("Centimeter:", centimeter)
# print("Meter:", centimeter/100)
# print("Kilometer:", centimeter/100000)

# farhrenheit=98
# print("Farhrenheit:", farhrenheit)
# print("Celsius:", (farhrenheit-32)*5/9)

# celsius=37
# print("Celsius:", celsius)
# print("Farhrenheit:", (celsius*9/5)+32)

# angle1=50
# angle2=60
# angle3=180-(angle1+angle2)
# print("Angle 3:", angle3)

# side =6
# print("area of an equilateral triangle.", (3**0.5/4)*side*side)

# marks=[70,75,80,65,60]
# print("Marks:", marks)
# print("Total Marks:", sum(marks))
# print("Average Marks:", sum(marks)/len(marks))  
# print("percentage:", (sum(marks)/500)*100)

# principal=1000
# rate=5
# time=2
# print("Simple Interest:", (principal * rate * time) / 100)

# A=5
# print("A:", A)
# B=10
# print("B:", B)

# print("Before swapping: A =", A, "B =", B)

# # Swapping the values
# A, B = B, A

# print("After swapping: A =", A, "B =", B)


# character = 'A'
# print("Character:", character)
# print("ASCII Value:", ord(character))

# second=3665
# print("Total Seconds:", second)
# print("Hours:", second//3600)
# print("Minutes:", second//60)
# print("Seconds:", second%60)

# Days=400

# print("Total Days:", Days)
# print("Years:", Days//365)
# print("Months:", (Days%365)//30)
# print(weeks := (Days%365)%30//7)

# number=4
# print("cube of", number, "is", number**3)

number=123
#print("Sum of digits of", number, "is", sum(int(digit) for digit in str(number)) )
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print("Sum of digits (using loop):", sum_of_digits)