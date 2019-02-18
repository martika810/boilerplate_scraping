from pathlib import Path
import pandas as pd
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urljoin
from src.progress import Progress


class CrawlerUsingSelenium:
    def __init__(self,browser,config):
        self.browser = browser
        self.config = config

    def crawl_all_pages_to_end(self,initial_url,file_to_save_results):
        try:

            # TODO Open url

            # TODO Get list of url to scrape (if only get the url for each product, if not for each page)

            # TODO Extract

            # TODO save in a dataframe using saver

            # TODO Record the progress using progress

            return True
        except Exception as e:
            print(str(e))
            # progress.save_process_progress(True,True)
            return False

    def scrape(self, file_to_save_results):
        print("Start crawling...")

        got_to_end = self.crawl_all_pages_to_end(self.config.initial_page,file_to_save_results)
        if(got_to_end):
            print('Scraping finished successfully')
        else:
            print("Error during scraping")

        print("Finish crawling...")