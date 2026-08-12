class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        result = []
        for num in nums:
            count = 0
            for j in range(len(nums)):
                if num > nums[j]:
                    count += 1
            result.append(count)
        return result



        
