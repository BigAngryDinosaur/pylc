# @lc app=leetcode id=937 lang=python3

from typing import List

class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def log_sort(x: str):
            identifier, data = x.split(" ", 1)
            return (0, data, identifier) if data[0].isalpha() else (1,)

        return sorted(logs, key=log_sort)
