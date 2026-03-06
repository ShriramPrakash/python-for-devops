import sys

def add(num1,num2):
    m = num1+num2
    return m

def sub(num1,num2):
    n=num1+num2
    return n

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
   output = add(num1, num2)
   print(output)

