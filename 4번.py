 itemprice= int(input("물건값을 입력하시오: "))
물건값을 입력하시오: 2600
>>> note= int(input("1000원 지폐개수: "))
1000원 지폐개수: 5
>>> coin500= int(input("500원 동전개수: "))
500원 동전개수: 4
>>> coin100= int(input("100원 동전개수: "))
100원 동전개수: 4
>>> 
>>> 
>>> change= note*1000+ coin500*500 + coin100*100 - itemprice
>>> 
>>> #거스름돈(500원 동전 개수)을 계산한다.
>>> nCoin500=change//500
>>> change= change%500
>>> 
>>> #거스름돈(100원 동전 개수)을 계산한다.
>>> nCoin100= change//100
>>> change= change&100
>>> 
>>> print("500원=", nCoin500, "100원=", nCoin100)
500원= 9 100원= 3
>>> 
