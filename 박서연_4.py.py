#4번문제.
won = int(input("1000원권 개수:"))
itemPrice = int(input("물건값:"))

change = won*1000 - itemPrice

ncoin500 = change // 500
ncoin100 = (change - ncoin500*500) // 100

print("500원 동전의 개수:", ncoin500)
print("100원 동전의 개수:", ncoin100)