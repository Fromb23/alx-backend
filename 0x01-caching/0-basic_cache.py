#!/usr/bin/env python3
"""caching system """

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        """Add key-value pair to the cache
        using self.cache_data from BaseCaching."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve value from cache based on the key."""
        return self.cache_data.get(key)
