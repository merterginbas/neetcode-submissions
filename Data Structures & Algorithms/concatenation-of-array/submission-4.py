class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums * 2 
        for i in range(len(ans)):
            if i < len(nums):
                ans[i]=nums[i]
            else: 
                j = i - len(nums) #***
                ans[i] = nums[j]
        return ans