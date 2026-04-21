from pages.initial_page import InitialPage
from playwright.sync_api import sync_playwright

import time


url = 'https://practicetestautomation.com/'

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    initial_page = InitialPage(page, url)
    initial_page.home_page()

    time.sleep(5)
    browser.close()