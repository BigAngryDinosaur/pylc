# @lc app=leetcode id=1 lang=python3

from typing import List, Dict

class Solution(object):

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store: Dict[int, int] = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in store:
                return [store[comp], i]
            store[num] = i


        return []
