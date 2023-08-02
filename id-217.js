/**
 * 217. Contains Duplicate
 * Source: https://leetcode.com/problems/contains-duplicate/
 */

var containsDuplicate = function(nums) {
    hashMap = {};

    for(let i = 0; i < nums.length; i++) {
        if(hashMap.hasOwnProperty(nums[i])) {
            return true;
        } else {
            hashMap[nums[i]] = 1;
        }
    }
    return false;
    
};