/**
 * 77. Combinations
 * Source: https://leetcode.com/problems/combinations/
 */

/**
 * Backtracking solution
 * Alternative solution: bruteforce combinations s.t. each combination = [x, x+1, x+2, ... , n] where combination.length = k
 * If combinations.length === (n+k-1)! / (k! * (n-1)!), stop
 */

var combine = function(n, k) {
    return backtracking([], 1, k, n, []);
};

var backtracking = (combination, start, maxLength, numbers, allCombinations) => {
    if(combination.length === maxLength) {
        allCombinations.push([...combination]);
    }

    for(let i=start;i < numbers+1;i++) {
        combination.push(i);
        backtracking(combination, i+1, maxLength, numbers, allCombinations);
        combination.pop();
    }
    return allCombinations;

}
