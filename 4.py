#4번, B835193 석채원
x = int(input("1000원권 개수:"))*1000
y = int(input("물건값:"))
change = x-y
a = int(change/500)
b = int(change%500/100)
print("500원 동전의 개수:",a)
print("100원 동전의 개수:",b)

