class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# convert the nums to set becuase it removes the duplicates in hash set
# find the lenght if find duplicate in set its length is lowered then original array then compare the lenght is small then return true 

# its complexity is also O(n)