/**
 * 26. Remove Duplicates from Sorted Array
 * Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 */



var removeDuplicates = (nums) => {
    let current = nums[0];
    k = 1;
    for(let i = 1; i < nums.length; i++) {
        if(current < nums[i]) {
            nums[k] = nums[i];
            current = nums[i];
            k++;
        } 
    }
    return k;
}