# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        while len(answer) == 0:
            for i in range(0,len(nums)):
                
                    temp = nums[:]
                    temp.remove(nums[i])
        
                    if target - nums[i] in temp:
                        
                        number = target - nums[i]
                        
                        if number == nums[i]:
                            answer = [i,temp.index(number)+1]
                        else:
                            answer = [i,nums.index(number)]
                        break
        return answer
