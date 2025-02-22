from playwright.sync_api import Page

class productsPO:
    def __init__(self, page: Page):
        self.page = page

    def btn_add_to_cart(self):
        return self.page.get_by_role("button", name="ADD TO CART")
    
    def ddl_sort(self):
        return self.page.get_by_role("combobox")
    
    def ddl_sort_option(self, sort_option):
        return self.page.get_by_role("combobox").select_option(value=sort_option)    
    
    def hdr_product_name(self):
        return self.page.locator(".inventory_item_name")
    
    def hdr_product_price(self):
        return self.page.locator(".inventory_item_price")
        
