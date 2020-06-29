# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
Input: 123
Output: 321

# Example 2:
Input: -123
Output: -321

# Example 3:
Input: 120
Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        
        
        nums = ['0','1','2','3','4','5','6','7','8','9']

        x = list(str(x))
        x.reverse()
        if x[-1] not in nums:
            x.insert(0,x.pop())
        answer = "".join(x)
        answer = int(answer)  
            
        if answer < -2147483648 or 2147483647 < answer:
            answer = 0
        
        return answer
