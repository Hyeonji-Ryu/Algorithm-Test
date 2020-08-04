# Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.
# Return a list of two integers [A, B] where:
# A and B are No-Zero integers.
# A + B = n
# It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

 
# Example 1:
# Input: n = 2
# Output: [1,1]
# Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.

# Example 2:
# Input: n = 11
# Output: [2,9]


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        nums = list(str(n))
        A = 0
        A_nums = list(str(A))
        
        while '0' in A_nums or '0' in nums:
            A += 1
            B = n - A
            nums = list(str(B))
            A_nums = list(str(A))
            
        B = "".join(nums)
        return  [A, int(B)]
