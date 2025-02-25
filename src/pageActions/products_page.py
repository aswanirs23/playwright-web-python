"""
Products Page Actions
This class handles all interactions with the products listing page.
"""

from src.pageObjects.products_PO import productsPO
from src.utils.ui_actions import UIActions

class ProductsPageActions (productsPO, UIActions):
        
    def sort_products(self, sort_option):
        sort_dropdown = self.ddl_sort()
        self.click_dropdown_option(sort_dropdown, sort_option)
        
    def get_product_prices(self):
        product_prices_element = self.hdr_product_price()
        return [float(price.inner_text().replace("$", "")) for price in product_prices_element.all()]
    
    def get_product_names(self):
        product_names_element = self.hdr_product_name()
        return [name.inner_text() for name in product_names_element.all()]
    

