/**
 * 
 * 1493. Longest Subarray of 1's After Deleting One Element
 * Source: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
 */

var longestSubarray = (nums) => {
    let consecutives = [];
    let count = 0;
    let highestConsecutive = 0;

    if (nums.indexOf(0, 1) === -1) {
        return nums.length - 1;
    }

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            count++;
        } else if (nums[i] === 0) {
            consecutives.push(count);
            count = 0;
        }
    }
    consecutives.push(count);


    for (let j = 0; j < consecutives.length - 1; j++) {
        highestConsecutive = Math.max(highestConsecutive, consecutives[j] + consecutives[j + 1])
    }

    return highestConsecutive;
}