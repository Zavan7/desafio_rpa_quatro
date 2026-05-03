from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class TestExceptions:
    def __init__(self, page: Page, selector_test: str, timeout=4000):
        self.page = page
        self.selector_test = selector_test
        self.timeout = timeout

    def test_exceptions(self) -> bool:
        
        try:
            self.page.wait_for_selector(self.selector_test, timeout=self.timeout)

            test_button = self.page.locator(self.selector_test)

            if not test_button.is_enabled():
                return False
            
            test_button.click()
            return True
        
        except Exception as e:
            return False