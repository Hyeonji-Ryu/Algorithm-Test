# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# 조건: 괄호의 개수가 같아야 한다. 마지막은 닫힘으로 끝나야 한다. 

def solution(s):
    cnt_left = 0
    cnt_right = 0
    
    for val in s:
        if val == "(":
            cnt_left += 1
        elif (val == ")") and (cnt_left > cnt_right):
            cnt_right += 1
        else:
            return False
    if cnt_left != cnt_right:
        return False
    return True
