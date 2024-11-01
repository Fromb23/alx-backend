#!/usr/bin/python3
"""
    BaseCaching
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        """Initialize the MRUCache and call the parent constructor."""
        super().__init__()

    def put(self, key, item):
        """Assign an item to a key in the cache
        managing the MRU eviction policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = list(self.cache_data.keys())[-1]
                del self.cache_data[mru_key]
                print(f'DISCARD: {mru_key}')

            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the key in the cache."""
        if key is None:
            return None

        return self.cache_data.get(key)
