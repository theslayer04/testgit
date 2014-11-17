input1 = int(input())

input2 = int(input())
try:
    result = input1 / input2
    print(result)
except ZeroDivisionError:
    print("You are officially an idiot ")


