#!/usr/bin/env python3
"""Implementing the FIFO caching algorithm.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Enables storing and retrieving items from a dictionary
       using the FIFO concept when the limit is reached.
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Retrieves item using key.
        """
        return self.cache_data.get(key, None)
