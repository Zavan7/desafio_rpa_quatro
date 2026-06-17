from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class ClickTest:
    def __init__ (
            self, page: Page,
            click_test_selector: str,
            selector_add: str,
            timeout=4000
        ):
        self.page = page
        self.click_test_selector = click_test_selector
        self.selector_add = selector_add
        self.timeout = timeout


    def click_test (self) -> bool:
        try:
            logger.info('4° - Click Test')
            click_test_button = self.page.locator(self.click_test_selector)

            click_test_button.wait_for(state='visible', timeout=self.timeout)
            

            if not click_test_button.is_enabled():
                logger.error('Button not found')
                return False
            
            click_test_button.click()


            self.page.locator(self.selector_add).wait_for(
                state='visible',
                timeout=20000
            )
            logger.info('Input loaded successfully')
            return True
        
        except Exception as e:
            logger.error(f'4° - Click Test\nError: {e}')
            return False
