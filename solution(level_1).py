# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.

def solution(x, n):
    answer = []
    for i in range(1,n+1):
        num = x*i
        answer.append(num)
    return answer


# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

def solution(arr1, arr2):
    temp = []
    lis = []
    for i in range(0,len(arr1)):
        for j in range(0,len(arr1[0])):
            sum = arr1[i][j]+arr2[i][j]
            lis.append(sum)
        temp.append(lis)
        lis = []
    return temp


# 문제 설명
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

def solution(arr):
    mean = sum(arr)/len(arr)
    answer = mean
    return answer


# 문제 설명
# 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
#num은 int 범위의 정수입니다.
# 0은 짝수입니다.

def solution(num):
    if num % 2 == 0:
        anwser = 'Even'
    else: anwser = 'Odd'
    return anwser


# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

def solution(arr):
    if len(arr)>1:
        arr.remove(min(arr))
        return arr
    else:
        answer = [-1]
        return answer
    

# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.

def solution(n):
    ans =[]
    temp = str(n)
    lis = sorted(temp, reverse=True)
    answer = lis[0]
    for i in range(1,len(lis)):
             answer += lis[i]
    return int(answer)


# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    
    temp = str(n)
    a = []
    for i in range(0,len(temp)):
        num = int(temp[i])
        a.append(num)
    answer = sum(a)
    return answer


# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.

def solution(n):
    answer = []
    temp = str(n)
    num = len(temp)-1
    for i in range(0,len(temp)):
        num1 = int(temp[num-i])
        answer.append(num1)  
    return answer


# 문제 설명
# 길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

#제한 조건
#n은 길이 10,000이하인 자연수입니다.

def solution(n):
    s='수박'*n
    answer = s[:n]
    return answer
