'''
853. Car Fleet
Source: https://leetcode.com/problems/car-fleet/description/
'''
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine the position and speed into a list of tuples
        pos_speed = list(zip(position, speed))
        
        # Sort the list based on the position in descending order
        pos_speed.sort(reverse=True, key=lambda x: x[0])
        
        fleets = 0
        finish_time = 0
        
        for pos, spd in pos_speed:
            # Calculate the time to reach the target for the current car
            current_time = (target - pos) / spd
            # If the current car takes more time than the lead car of the current fleet,
            # it forms a new fleet
            if current_time > finish_time:
                fleets += 1
                finish_time = current_time
        
        return fleets
    

s = Solution()
print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
