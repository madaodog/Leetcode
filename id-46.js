/**
 * 46. Permutations
 * Source: https://leetcode.com/problems/permutations/
 */

var permute = (nums) => {
    let visited = Array(nums.length).fill(false);
    let permutations = [];
    let permutation = [];

    var backtrack = (nums) => {
        if(permutation.length === nums.length) {
            permutations.push(permutation.slice());
        }
        for(let i = 0; i < nums.length; i++) {
            if(!visited[i]) {
                visited[i] = true;
                permutation.push(nums[i]);
                backtrack(nums);
                permutation.pop(nums[i]);
                visited[i] = false;
            }

        }
    }
    backtrack(nums);
    return permutations;
}

console.log(permute([1, 2, 3]));