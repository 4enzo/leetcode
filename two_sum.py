# -*- coding: utf-8 -*-
'''
Created on 2022-04-16

@author: Enzo
'''

'''
https://leetcode-cn.com/problems/two-sum/

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
'''

# def twoSum(nums, target):
#     """
#     暴力枚举
#     """
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]== target:
#                 return [i,j]

def twoSum(nums, target):
    """
    哈希法
    """
    hash_tmp = dict()
    #enumerate是个好东西
    #枚举列表，先判断target-value是否在hash_tmp里：
    # 如果不在，则将value值存入hash_tmp里（以键的形式存入），
    # 如果存在，返回当前index值及hash_tmp[target-value]
    for index,value in enumerate(nums):
        if target-value in hash_tmp:
            return [hash_tmp[target-value],index]
        else:
            hash_tmp[value] = index

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums,target))

