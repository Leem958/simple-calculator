
print('select operation: ')
print('addition: 1')
print('subtraction: 2')
print('multiplication: 3')
print('division: 4')
operation = input("Enter choice(1/2/3/4): ")
if operation in ('1', '2', '3', '4'):
  num1 = float(input("Enter first number: ")) 
  num2 = float(input("Enter second number: "))
result =float(num1) + float(num2)
if operation == '1':
  print(float(num1) + float(num2))
elif operation == '2':
  print(float(num1) - float(num2))
elif operation == '3':
  print(float(num1) * float(num2))
elif operation == '4':
  print(float(num1) / float(num2))