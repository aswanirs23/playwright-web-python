from src.pageObjects.products_PO import productsPO
from src.utils.ui_actions import UIActions

class ProductsPageActions:   
    def __init__(self, page):
        self.products_page = productsPO(page)
        self.ui_actions = UIActions(page)
    
    def sort_products(self, sort_option):
        sort_element = self.products_page.ddl_sort()
        self.ui_actions.click_element(sort_element)
        self.products_page.ddl_sort_option(sort_option)
        
    def get_product_prices(self):
        product_prices_element = self.products_page.hdr_product_price()
        return [float(price.inner_text().replace("$", "")) for price in product_prices_element.all()]
    
    def get_product_names(self):
        product_names_element = self.products_page.hdr_product_name()
        return [name.inner_text() for name in product_names_element.all()]
    

