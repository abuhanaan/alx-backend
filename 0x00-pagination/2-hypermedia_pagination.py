#!/usr/bin/env python3
from typing import Tuple
import csv
import math
from typing import List, Dict
"""Hypermedia pagination.
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        # verifies that both arguments are integers and greater than 0
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        # getting the correct indexes to paginate the dataset correctly
        start, end = index_range(page, page_size)
        data = self.dataset()
        # If the input arguments are out of range for the dataset,
        # return an empty list
        if start > len(data):
            return []
        # O/W, return the data
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Displays information about a page.

        Keyword arguments:
        page_size -- the length of the returned dataset page
        page -- the current page number
        data -- the dataset page (equivalent to return from previous task)
        next_page -- number of the next page, None if no next page
        prev_page -- number of the previous page, None if no previous page
        total_pages -- the total number of pages in the dataset as an integer
        Return: return_description
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
                'page_size': len(page_data),
                'page': page,
                'data': page_data,
                'next_page': page + 1 if end < len(self.__dataset) else None,
                'prev_page': page - 1 if start > 0 else None,
                'total_pages': total_pages,
        }
        return page_info
