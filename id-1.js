/**
 * 1. Two Sum
 * Source: https://leetcode.com/problems/two-sum/
 */

var twoSum = (nums, target) => {
    hashMap = {};

    for(let i = 0; i < nums.length; i++){
        complement = target - nums[i];
        if(complement in hashMap && hashMap[complement] !== i) {
            return [i, hashMap[complement]];
        }
        hashMap[nums[i]] = i;
        
    }
    return [];

}
