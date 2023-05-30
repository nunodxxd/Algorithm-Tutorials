# Hashtable Algorithm

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = [(key, value)]
        else:
            for pair in self.buckets[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.buckets[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return None
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None

# Create a hashtable with a size of 10
ht = Hashtable(10)

# Put some key-value pairs into the hashtable
ht.put("text-1", 1)
ht.put("text-2", 2)
ht.put("text-3", 3)

# Retrieve values based on their keys
print(ht.get("text-1"))  # Output: 1
print(ht.get("text-2"))  # Output: 2
print(ht.get("text-3"))  # Output: 3