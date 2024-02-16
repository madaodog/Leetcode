/**
 * 74. Search a 2D Matrix
 * Source: https://leetcode.com/problems/search-a-2d-matrix/
 */

const searchMatrix = (matrix, target) => {
    // Treat the 2D matrix as a 1D list, and continue to map indices likewise
    width = matrix[0].length;
    height = matrix.length;
    left = 0;
    right = width * height - 1;

    while(left <= right) {
        mid = Math.floor((left + right) / 2);
        columnOfMid = Math.floor(mid / width);
        rowOfMid = mid % width;

        if(matrix[columnOfMid][rowOfMid] === target) {
            return true;
        } else if(matrix[columnOfMid][rowOfMid] < target) {
            left = mid + 1;
        } else if(matrix[columnOfMid][rowOfMid] > target) {
            right = mid - 1;
        }
    }
    return false;
};