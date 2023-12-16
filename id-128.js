/**
 * 128. Longest Consecutive Sequence
 * Source: https://leetcode.com/problems/longest-consecutive-sequence/
 */

const longestConsecutive = (nums) => {
    const set = new Set(nums);
    let current = 1;
    let longest = 1;

    if(nums.length === 0) {
        return 0;
    }

    for(let i = 0; i < nums.length; i++) {
        if(!set.has(nums[i]-1)) {
            let number = nums[i];
            set.delete(number);
            while(set.has(number+1)) {
                current++;
                set.delete(number+1);
                number++;
            }
        }
        longest = Math.max(longest, current);
        current = 1;
    }
    return longest;
}

nums = [100,4,200,1,3,2]

console.log(longestConsecutive(nums));