#!/usr/bin/env python3
"""Implementing the LIFO caching algorithm.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """nables storing and retrieving items from a dictionary
       using the LIFO concept when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Updates the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # popitem() removes item in LIFO manner if set to True
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves item using key.
        """
        return self.cache_data.get(key, None)
