class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            aranan = target - nums[i]

            if aranan in seen:
                return[seen[aranan],i]
            seen[nums[i]] = i


            



     #   for i in range(len(nums)):
      #      for j in range(i+1,len(nums)):
       #         if nums[i] + nums[j] == target:
        #            output_list = [i,j]
         #           return output_list

        