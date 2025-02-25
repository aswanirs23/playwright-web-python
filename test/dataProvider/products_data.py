"""
Product Sorting Test Data Provider
This module contains test data for product sorting functionality testing.
It provides parameterized test cases for different sorting options:
- Price sorting (low to high, high to low)
- Name sorting (A to Z, Z to A)
"""

import pytest

sort_options = [
    pytest.param("lohi", "price", "ascending", id="Products sort by price - Low to High"),
    pytest.param("hilo", "price", "descending", id="Products sort by price - High to Low"),
    pytest.param("az", "name", "ascending", id="Products sort by name - A to Z"),
    pytest.param("za", "name", "descending", id="Products sort by name - Z to A")
]