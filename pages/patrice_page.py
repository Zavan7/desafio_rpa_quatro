from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class PatricePage:
    def __init__ (self, page: Page, selector_patrice: str, timeout=4000):
        self.page = page
        self.selector_patrice = selector_patrice
        self.timeout = timeout


    def patrice_page(self) -> bool:
        try:
            self.page.wait_for_selector(self.selector_patrice, timeout=self.timeout)

            patrice_page_button = self.page.locator(self.selector_patrice)
            
            if not patrice_page_button.is_enabled():
                return False
            
            patrice_page_button.click()
            return True
        
        except Exception as e:
            return False