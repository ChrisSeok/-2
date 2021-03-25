# 5번 B735042 김대겸

# 사용자로부터 정수 입력 받기
user_Num = int(input("정수="))
# 1의 자리 숫자 구하기
num_1 = user_Num % 10
# 10의 자리 숫자 구하기
num_2 = int(((user_Num - num_1) % 100) / 10)
# 100의 자리 숫자 구하기
num_3 = user_Num // 100
# 자리수의 합 출력
num_Total = num_1 + num_2 + num_3
print(num_Total)