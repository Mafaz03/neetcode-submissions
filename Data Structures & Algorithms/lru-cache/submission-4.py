class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {} # {key: val}
        self.capcity = capacity
        self.recent = {} # {key: access}
        self.counter = 0

    def get(self, key: int) -> int:
        to_return = self.hashmap.get(key, -1)

        if key in self.recent:
            self.recent[key] = self.counter
        
        self.counter += 1
        return to_return

    def put(self, key: int, value: int) -> None:
        if (key not in self.hashmap) and (len(self.hashmap) == self.capcity):
                # need to pop the least used
                key_to_delete = self.get_key_for_least_access(self.recent)
                self.hashmap.pop(key_to_delete)
                self.recent.pop(key_to_delete)
        self.hashmap[key] = value
        self.recent[key] = self.counter
        self.counter += 1

    def get_key_for_least_access(self, hashmap):
        return min(hashmap, key = hashmap.get)

