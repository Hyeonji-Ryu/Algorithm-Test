# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:
# Input: [4,3,2,7,8,2,3,1]
# Output: [5,6]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        total = list(range(1,len(nums)+1))
        nums = list(set(nums))
        ans = []
        count = len(total)-len(nums)
        i, j = 0, 0
        
        while len(ans) != count:
        
            if i == len(nums):
                while len(ans) != count:
                    ans.append(total[j])
                    j += 1
                break
    
            if nums[i] != total[j]:
                ans.append(total[j])
                j += 1

            else:
                i += 1
                j += 1 

        return ans
