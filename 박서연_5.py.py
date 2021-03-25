#5번문제.
x = int(input("정수="))
hundreds = x // 100
tens = (x - hundreds*100) // 10
units = x % 10
print(hundreds + tens + units)
