# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

# Example 1:
# Input: A = "ab", B = "ba"
# Output: true

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        lis = []
        answer = []
        
        for i in range(len(A)):
    
            if A[i] != B[i]:
                lis.append(A[i])
                answer.append(B[i])
        
        lis.reverse()

        if len(lis) > 2 or len(A) == 1:
            return False

        temp = set(A)
        temp = list(temp)
        
        if len(A) == 0 or len(A) != len(B):
            return False
        
        elif len(temp) != len(A) and lis == answer:
            return True        


        elif len(lis) != 2 and A[-1] != B[0]:
            return False

        else:
            if lis == answer:
                return True
            else:
                return False
