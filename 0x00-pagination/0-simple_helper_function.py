#!/usr/bin/env python3
"""
    index_range
"""


def index_range(page, page_size):
    """Calculate the start and end indices for a given page."""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
