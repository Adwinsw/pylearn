#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和,输出单一下角标对数,也可用于2个以上相同变量符合条件输出的多解情况
#
# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]

# @lc code=end
        

