#!/usr/bin/env python3
"""FIFO caching system with First-In-First-Out eviction policy."""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache that evicts the oldest item when limit is reached."""
    def __init__(self):
        """Initialize the FIFOCache class."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item to cache and evict oldest if limit is reached."""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        if key and item:
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve value from cache based on the key."""
        return self.cache_data.get(key)
