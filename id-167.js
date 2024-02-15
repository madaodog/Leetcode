/**
 * 167. Two Sum II - Input Array Is Sorted
 * Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 */

const twoSum = (numbers, target) => {
    let l = 0;
    let r = numbers.length - 1;
    while(l < r) {
        if(numbers[l] + numbers[r] === target) {
            return [l+1, r+1];
        }
        if(numbers[l] + numbers[r] > target) {
            r--;
        }
        if(numbers[l] + numbers[r] < target) {
            l++;
        }
    }
    return false;
}



s = [1, 2, 4, 5, 10, 12]
console.log(twoSum(s, 9));