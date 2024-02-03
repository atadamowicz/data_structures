class HashMap:
    def __init__(self, size):
        self.size = size
        self.hashmap = [list() for _ in range(size)]

    def __repr__(self):
        buckets = []
        for i, bucket in enumerate(self.hashmap):
            if bucket:
                for key, value in bucket:
                    buckets.append(f"{key}: {value} @ {i}")
        return str(buckets)

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.size

    def insert(self, key, value):
        index = self.key_to_index(key)
        bucket = self.hashmap[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self.key_to_index(key)
        bucket = self.hashmap[index]

        for k, v in bucket:
            if k == key:
                return v
            
        return None 

    def delete(self, key):
            index = self.key_to_index(key)
            bucket = self.hashmap[index]
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return True
            return False