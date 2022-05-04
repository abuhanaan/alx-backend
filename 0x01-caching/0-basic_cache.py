#!/usr/bin/env python3
"""Basic caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Enables storing and retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Updates the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves item using key.
        """
        return self.cache_data.get(key, None)
