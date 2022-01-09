# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        for i in range(0,len(nums)):
                
            temp = nums[:]
            temp.remove(nums[i])
        
            if target - nums[i] in temp:
                        
                number = target - nums[i]
                        
                if number == nums[i]:
                    return [i,temp.index(number)+1]
                else:
                    return [i,nums.index(number)]

                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
            temp = dict()
        
            for i in range(len(nums)):
                
                number = target - nums[i]
        
                if number in temp:
                        return [i,temp[number]]
                temp[nums[i]] = i
