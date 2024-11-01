
#!/usr/bin/python3
"""Initialize the LRUCache and call the parent constructor."""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class that extends BaseCaching."""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign the item value to the cache_data for the given key."""
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value associated with the key
        updating its usage status."""
        if key is None or key not in self.cache_data:
            return
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
