# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.


class Solution:
    def maximumSwap(self, num: int) -> int:
        
        nums = list(str(num))
        re_nums = sorted(nums, reverse=True)
        
        for i in range(len(nums)):
    
            if nums[i] != re_nums[i]:
                reve = re_nums[i:]
                origin = nums[i:]
                temp = origin[0]
                index = max(list(filter(lambda x: origin[x] == reve[0], range(len(origin)))))
                origin[0] = reve[0]
                origin[index] = temp
                nums[i:] = origin
                break
         
        answer = "".join(nums)
        
        return int(answer)
