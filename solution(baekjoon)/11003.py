# 문제
# N개의 수 A1, A2, ..., AN과 L이 주어진다.

# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

# 입력
# 첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
# 둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# 첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.

# Tip: priority queue, speed: list < tuple, input() < sys.stdin.readline()

from collections import deque
import sys

num,L = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
Deque = deque()

for i in range(num):
    while Deque and Deque[-1][0] > A[i]:
        Deque.pop()
    Deque.append((A[i], i))
    while Deque and Deque[0][1] < i-L+1:
        Deque.popleft()
    print(Deque[0][0], end = ' ')
