# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

def solution(n):
    sqrt = int(n**(1/2))
    primes = [True]*(n+1)
    for num in range(2,sqrt+1):
        if primes[num] == True:
            times = 2
            while times*num <= n:
                primes[num*times] = False
                times += 1
    return len(list(filter(lambda x: x == True,primes[2:])))
