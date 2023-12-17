/**
 * 11. Container With Most Water
 * Source: https://leetcode.com/problems/container-with-most-water/
 * 
 */

const maxArea = (height) => {
    let left = 0;
    let right = height.length - 1;
    let highest = 1;
    if(height.length === 2) {
        return container(0,1, height[0], height[1]);
    }
    while(left < right) {
        highest = Math.max(container(left, right, height[left], height[right]), highest);
        if(height[left] > height[right]) {
            right--;
        }
        else if(height[left] <= height[right]) {
            left++;
        }
}
    return highest;
}

const container = (i1, i2, h1, h2) => {
    return (i2-i1)*Math.min(h1,h2);
}

height = [1,8,6,2,5,4,8,3,7]
height2 = [4,3,2,1,4]

height3 = [2,3,4,5,18,17,6]

height4 = [1,3,2,5,25,24,5]

console.log (maxArea(height4));