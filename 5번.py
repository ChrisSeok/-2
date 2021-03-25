#사용자로부터 입력된 3자리 수의 자리수의 합을 구하라.
>>> number=135
>>> sum = 0;
>>> while number > 0 :
    digit = number % 10
    sum = sum + digit
    number= number // 10
    
>>> print("자리수의 합은 %d입니다. " % sum)
자리수의 합은 9입니다. 
>>> 
