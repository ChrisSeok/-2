#4 B735042 김대겸

num_1000 = int(input("1000원권 개수: "))
price = int(input("물건값: "))
# 총 잔돈
change_total = 1000 * num_1000 - price
# 500원짜리와 100원짜리 개수
num_500 = change_total // 500
change_500 = change_total % 500
num_100 = int(change_500 / 100)
# 출력
print(num_500)
print(num_100)