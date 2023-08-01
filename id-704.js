/**
 * 704. Binary Search
 * Source: https://leetcode.com/problems/binary-search/
 */

var search = function(nums, target) {
    let start = 0;
    let end = nums.length;
    let middle = Math.floor( nums.length / 2);
    if(nums[middle] === target) {
        return middle;
    }
    while(nums[middle] !== target && start < end) {
        if(nums[middle] > target) {
            end = middle-1;
            middle = Math.floor((start+end) / 2);
        }
        if(nums[middle] < target) {
            start = middle+1;
            middle = Math.floor((start+end) / 2);
        }
        if(nums[middle] === target) {
            return middle;
        }
    }
    return -1;

};