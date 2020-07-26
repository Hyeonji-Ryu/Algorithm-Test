# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 차례대로 별을 출력한다.

# 예제 입력 1  복사
# 1
# 예제 출력 1  복사
# *
# 예제 입력 2  복사
# 2
# 예제 출력 2  복사
# *
#  *
# *
#  *

n = int(input())

temp = n/2

if  temp < 1:
    print("* ")
elif temp >= 1:
    for i in range(0,n):
        print("* "*round(1.00001*(temp)))
        print(" *"*int(temp))
