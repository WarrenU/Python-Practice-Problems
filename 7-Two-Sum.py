# https://leetcode.com/problems/two-sum/description/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# EX:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# TODO: Implement using a hash map!!! See 8-Two-Sum
class Solution(object):
    def complementary_number(self, target, sub_val):
        """
        Returns a complementary number given a target value.
        int target: value to find complement of
        int sub_val: a value to subtract target from
        return int: a number, x s.t. sub_val + x = target
        """
        return target-sub_val

    def targetNumInList(self, nums, target, curr_num_index):
        """
        Returns the target complementary number in the list.
        Gets the complementary number to find in the list (target-curr_num).
        Checks to see that it is not the same number we are iterating over (curr_num).
        """
        rg_excluding_curr_num = nums[:curr_num_index] + nums[curr_num_index+1:]
        curr_num = nums[curr_num_index]
        complementary_num = self.complementary_number(target, curr_num)
        if complementary_num in rg_excluding_curr_num:
            print(rg_excluding_curr_num)
            return rg_excluding_curr_num.index(complementary_num) + 1
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for curr_num in nums:
            curr_num_index = nums.index(curr_num)
            index_complement = self.targetNumInList(nums, target, curr_num_index)
            if(index_complement):
                return [curr_num_index, index_complement]
        