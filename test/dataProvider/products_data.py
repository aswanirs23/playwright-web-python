import pytest

sort_options = [
    pytest.param("lohi", "price", "ascending", id="Products sort by price - Low to High"),
    pytest.param("hilo", "price", "descending", id="Products sort by price - High to Low"),
    pytest.param("az", "name", "ascending", id="Products sort by name - A to Z"),
    pytest.param("za", "name", "descending", id="Products sort by name - Z to A")
]