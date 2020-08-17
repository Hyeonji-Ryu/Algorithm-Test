# Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, 
# where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.
# Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.
# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

# Example 1:
# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. 
#              Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
#              No other pairs satisfy the condition, so we return the max of 4 and 1.

# Example 2:
# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.


### Tip: yi + yj + |xi - xj| -> yi + yj + xj - xi -> xj + yj + yi - xi in 1 <= i < j <= points.length.

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        from collections import deque
        
        Deque = deque()
        ans = float('-inf')
        
        for x_j, y_j in points:
    
            while Deque and x_j - Deque[0][1] > k:
                Deque.popleft() # k보다 큰 값들 모두 제거
    
            if Deque:
                ans = max(ans, x_j + y_j + Deque[0][0]) # k와 같거나 작은 경우 최댓값 도출
    
            while Deque and Deque[-1][0] <= y_j-x_j:
                Deque.pop() # y-x중에 큰 값들만 남기기
    
            Deque.append([y_j-x_j,x_j]) # 데이터 추가
    
        return ans 
