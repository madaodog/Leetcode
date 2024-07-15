'''
981. Time Based Key-Value Store
Source: https://leetcode.com/problems/time-based-key-value-store/description/
'''

class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
         if key not in self.map:
            return ""
         values = self.map[key]
         left, right = 0, len(values) - 1
         result = ""
         while right >= left:
            mid = (right+left) // 2
            if values[mid][1] <= timestamp:
               result = values[mid][0]
               left = mid + 1
            else:
                right = mid - 1
         return result
            

            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)