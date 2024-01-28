class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        # Enumerate in python basically gives us the current index of where we are at and the value of the index we are interating at. Since we need index here, we use enumerate.
        for i, num in enumerate(nums):
            to_search = target - num

            if to_search in index_dict:
                return [i, index_dict[to_search]]

            index_dict[num] = i