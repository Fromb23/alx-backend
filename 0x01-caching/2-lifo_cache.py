#!/usr/bin/env python3
"""LIFO caching system with First-In-First-Out eviction policy."""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache that evicts the oldest item when limit is reached."""
    def __init__(self):
        """Initialize the LIFOCache class."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Remove item to cache and evict oldest if limit is reached."""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve item from cache by key."""
        return self.cache_data.get(key)
