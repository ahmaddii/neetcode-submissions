class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            
            needed = target - nums[i]

            if needed in seen:
                return [seen[needed[i]],i]
            
            seen[nums[i]] = i # store current no and index in dict
        
        return []

# needed = target - current number
# it dosent compare all number if we see already put in dict
