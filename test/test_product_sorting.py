"""
This module contains test cases for the product sorting functionality.

"""

import pytest
from src.pageActions.products_page import ProductsPageActions
from dataProvider.products_data import sort_options
from src.utils.logger import setup_logger

logger = setup_logger()

@pytest.mark.sorting
@pytest.mark.usefixtures("logged_in_user")
@pytest.mark.parametrize("sort_option, attribute, order", sort_options)
def test_product_sorting(page, sort_option, order, attribute):
    products_page = ProductsPageActions(page)
    products_page.sort_products(sort_option)
    
    logger.info(f"Sorting products by {sort_option}")
    
    if attribute == "price":
        values = products_page.get_product_prices()
    else:
        values = products_page.get_product_names()

    if order == "ascending": 
        assert values == sorted(values), f"Products are not sorted ascending by {attribute}"
        logger.info(f"Sorted {attribute} successfully in ascending order.")

    else: 
        assert values == sorted(values, reverse=True), f"Products are not sorted descending by {attribute}"
        logger.info(f"Sorted {attribute} successfully in descending order.")
