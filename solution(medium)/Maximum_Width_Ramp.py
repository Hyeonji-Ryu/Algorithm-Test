# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.
# find the maximum width of a ramp in A.  If one doesn't exist, return 0.

# Example 1:
# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

# Example 2:
# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.



class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        
        num = 0
        mins = [(A[0],0)]

        for i in range(len(A)):
    
            if A[i] < mins[-1][0]:
                mins.append((A[i],i))

        for i in range(len(A)-1,-1,-1):
    
            while mins != [] and A[i] >= mins[-1][0]:
                val,index = mins.pop(-1)
                num = max(i-index, num)
                
        return num
