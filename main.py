
from pages.test_exceptions import TestExceptions
from pages.initial_page import InitialPage
from pages.patrice_page import PatricePage
from pages.click_test import ClickTest

from datetime import UTC, datetime
from playwright.sync_api import sync_playwright

from config.log import setup_logging
from db.mongo import MongoDB
import logging

setup_logging()

logger = logging.getLogger(__name__)

time_stamp = 2
url = 'https://practicetestautomation.com/'
patrice_page_selector = '#menu-item-20'
selector_test = "//a[text()='Test Exceptions']"
click_test_selector  = '#add_btn'
test_selector_final  = '#row2 .input-field'

mongo = MongoDB()

def main() -> None:
    result = {
        'start_date': None,
        'end_date': None,
        'duration': None,
        'status': 'Running',
        'error': None
    }

    start_date = datetime.now(UTC)
    browser = None

    try:
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()

            # Fluxo de navegação
            InitialPage(page, url).home_page()
            PatricePage(page, patrice_page_selector).patrice_page()
            TestExceptions(page, selector_test).test_exceptions()
            ClickTest(page, click_test_selector, test_selector_final).click_test()

            result['status'] = 'Success'

    except Exception as e:
        logger.error(f'Erro durante execução: {e}', exc_info=True)
        result['status'] = 'Failed'
        result['error'] = str(e)

    finally:
        if browser:
            try:
                browser.close()
            except Exception:
                logger.warning('Browser já estava fechado ou não inicializado')

        end_date = datetime.now(UTC)
        duration = (end_date - start_date).total_seconds()

        result.update({
            'start_date': start_date,
            'end_date': end_date,
            'duration': duration
        })

        # Exibe resultado no console
        for key, value in result.items():
            print(f"{key}: {value}")

        # Salva no MongoDB
        try:
            mongo.insert(result)
            logger.info('Resultado salvo no DB')
        except Exception as e:
            logger.error(f'Erro ao salvar no DB: {e}', exc_info=True)
            result['error'] = str(e)

        logger.info('Execução finalizada')


if __name__ == '__main__':
    main()