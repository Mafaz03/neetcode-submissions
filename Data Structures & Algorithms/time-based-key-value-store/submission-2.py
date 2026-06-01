class TimeMap:

    def __init__(self):
        self.key_val_hash = {} # {key: [(value, timestep), (value, timestep), ....]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_val_hash:
            self.key_val_hash[key].append((value, timestamp))
        else:
            self.key_val_hash[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.key_val_hash: return ""
        temp_arr = self.key_val_hash[key]

        if len(temp_arr) == 0: return ""
        

        L, R = 0, len(temp_arr)-1

        while L <= R:
            mid = (L+R)//2

            if temp_arr[mid][-1] == timestamp:
                print("found, ", temp_arr[mid])
                return temp_arr[mid][0]
            
            if temp_arr[mid][-1] < timestamp:
                L = mid + 1
            else:
                R = mid - 1
        
        if temp_arr[R][-1] < timestamp: return temp_arr[R][0]
        return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)