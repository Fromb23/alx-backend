#!/usr/bin/env python3

import csv
import math
from typing import List


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        start_index, end_index = index_range(page, page_size)

        with open('Popular_Baby_Names.csv', 'r') as file:
            reader = csv.reader(file)
            dataset = list(reader)

        result = (
                dataset[start_index:end_index]
                if start_index < len(dataset)
                else []
                )
        return result


def index_range(page, page_size):
    """Calculate the start and end indices for a given page."""

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
