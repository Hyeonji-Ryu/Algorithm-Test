# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        count1 = 0
        count2 = 0
        answer = 0
        
        for i in range(0,len(s)):
    
            if s[i] == 'R':
                count1 += 1
    
            elif s[i] =='L':
                count2 += 1
    
            if count1 == count2:
                answer += 1
                count1 = 0
                count2 = 0
                
        return answer
