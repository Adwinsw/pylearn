#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和,输出单一下角标对数,不能用于2个以上相同变量符合条件输出的多解情况
#
# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hasmap = {}
            for i,num in enumerate(nums):
                j = hasmap.get(target - num)
                if j is not None:
                    return [j,i]
                hasmap[num] = i
# @lc code=end