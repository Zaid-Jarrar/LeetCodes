class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        total = 0
        for num in nums:
            total += num
            nums[count] = total
            count += 1

        return nums


    
            