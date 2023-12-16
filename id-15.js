/**
 * 15. 3Sum
 * Source: https://leetcode.com/problems/3sum/
 */

const threeSum = (nums) => {
    const sortedNums = nums.sort((a, b) => a - b);
    const results = [];

    for(let i = 0; i < nums.length; i++) {
        let l = i+1;
        let r = nums.length-1;
        if((i > 0 && sortedNums[i] !== sortedNums[i-1]) || i === 0) {
            while(l < r) {
                if(sortedNums[l] + sortedNums[r] + sortedNums[i] === 0) {
                    results.push([sortedNums[i], sortedNums[l], sortedNums[r]]);
                    l++;
                    while(sortedNums[l] === sortedNums[l-1] && l < r) {
                        l++;
                    }
                } 
                if(sortedNums[l] + sortedNums[r] + sortedNums[i] > 0) {
                    r--;
                } 
                if(sortedNums[l] + sortedNums[r] + sortedNums[i] < 0) {
                    l++;
                } 
            }

        }
    }
    return results;
}

