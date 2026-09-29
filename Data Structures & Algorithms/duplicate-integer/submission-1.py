class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() # Hash set method

        for num in nums:

            if num in seen:
                return True
            seen.add(num)
        return False
            

        