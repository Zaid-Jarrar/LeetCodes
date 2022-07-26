class Solution(object):
 
    def pivotIndex(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        left_sum = 0   
        for index in range(len(nums)):
        # if index < (len(nums)):
            right_sum = sum(nums) - left_sum - nums[index]
            if left_sum == right_sum:

                return index
            left_sum = left_sum + nums[index]


        return -1
