#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple, Dict, Any


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
        """get pagignation"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page > 0

        start_index, end_index = self.index_range(page, page_size)

        return self.dataset()[start_index:end_index]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Calculate the start and end indices for a given page."""
        start_index = (page - 1) * page_size
        end_index = page * page_size

        return (start_index, end_index)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Retrieve paginated data with hypermedia links."""
        data = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1)

        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
