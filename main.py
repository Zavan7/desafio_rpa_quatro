from pages.initial_page import InitialPage
from pages.patrice_page import PatricePage
from pages.test_exceptions import TestExceptions
from playwright.sync_api import sync_playwright

import time


url = 'https://practicetestautomation.com/'
patrice_page_selector = '#menu-item-20'
selector_test = "//a[text()='Test Exceptions']"


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    initial_page = InitialPage(page, url)
    initial_page.home_page()

    time.sleep(5)
    patrice_page = PatricePage(page, patrice_page_selector)
    patrice_page.patrice_page()

    time.sleep(5)
    test_exceptions = TestExceptions(page,selector_test)
    test_exceptions.test_exceptions()

    time.sleep(5)
    browser.close()