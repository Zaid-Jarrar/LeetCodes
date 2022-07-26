class Solution(object):
 
    def pivotIndex(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _walk(nums,index):
            global result

            if index < (len(nums)):
                left = nums[:index]

                left_sum=sum(left)
                right_sum = sum(nums) - left_sum - nums[index]
                
                if left_sum == right_sum:
                    result = index
                    return result
                index +=1
                _walk(nums,index)
            else:
                result = -1
        _walk(nums,0)
        return result

