/**
 * 238. Product of Array Except Self
 * Source: https://leetcode.com/problems/product-of-array-except-self/
 */

/**
 Optimization by utilizing the symmetry of the iterations.
 Allows to have n iterations instead of 2*n
 */

 const productExceptSelf = (nums) => {
    const result = Array(nums.length).fill(1);
    let l = 1;
    let r = 1;
    for(let i = 0; i < nums.length; i++) {
        result[i] *= l;
        l *= nums[i];
        result[nums.length-i-1] *= r;
        r *= nums[nums.length-i-1];
    }
    return result;
}

