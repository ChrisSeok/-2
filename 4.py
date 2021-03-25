# 4번 C111152 Jong Uk Lim

Thou = int(input('1000원권 개수: '))*1000
Goods= int(input('물건값: ' ))
change = Thou - Goods
hund5 = change//500
hund1 = (change- hund5*500)//100
print('500원 동전의 개수: ',hund5)
print('100원 동전의 개수: ',hund1)