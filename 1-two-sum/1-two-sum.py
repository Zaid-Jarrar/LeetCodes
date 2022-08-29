class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        for index in range(len(nums)):
            num = nums[index]
            difference = target - num
            if difference not in dic:
                dic[nums[index]] = index
            else:
                return [dic[difference],index]
                
        
        # result = []
        # for index in range(len(nums)):
        #     for index2 in range(len(nums)):
        #         if index != index2:
        #             if nums[index] + nums[index2] == target:
        #                 result.append(index)
        #                 result.append(index2)
        #                 return result
        # return result
        