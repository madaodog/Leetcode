/**
 * 42. Trapping Rain Water
 * Source: https://leetcode.com/problems/trapping-rain-water/
 */

const trap = (height) => {
    let left = 0;
    let right = height.length-1;
    let leftBorder = height[left];
    let rightBorder = height[right];
    let rain = 0;

    while(left < right) {

        if(leftBorder > rightBorder) {
            right--;
            rightBorder = Math.max(height[right], rightBorder);
            rain += Math.max(0, rightBorder - height[right]);
        }
        else if(leftBorder <= rightBorder) {
            left++;
            leftBorder = Math.max(height[left], leftBorder);
            rain += Math.max(0, leftBorder - height[left]);
        }

    }
    return rain;
}

height = [0,1,0,2,1,0,1,3,2,1,2,1]

console.log(trap(height));