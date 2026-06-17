from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class InitialPage:
    def __init__(self, page: Page, url: str, timeout=4000):
        self.page = page
        self.url = url
        self.timeout = timeout

    def home_page(self) -> bool:
        try:
            logger.info('1° - Initial Page')
            self.page.goto(self.url)
            return True
        
        except Exception as e:
            logger.error(f'1° - Initial Page\nError: {e}')
            return False
        
        