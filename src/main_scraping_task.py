
from src.crawler_selenium import Crawler
from src.config import Config
import time
from src.progress import Progress


def main(browser, config):

    crawler = Crawler(browser, Config()) # Not using selenium
    crawler = Crawler(browser, Config(browser)) # If selenium based
    crawler.scrape('scraping_results_'+ str(time.time())[:10] +'.csv')

def setup():
    return None
    #TODO Here I can add the broser setup if using selenium, if not leave empty or delete
    # Set up the selenium browser
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # prefs = {"profile.default_content_setting_values.geolocation" :2}
    #
    # options.add_experimental_option("prefs",prefs)
    #
    # browser = webdriver.Chrome('./chromedriver', chrome_options=options)
    # browser.implicitly_wait(25)
    # return browser

def run_scraping_task():
    try:
        progress = Progress()
        progress.init()
        progress.save_process_progress(False,False)
        # TODO Remove if not using selenium
        browser = setup()

        config = Config(browser) #TODO: Pass browser if the crawling is selenium based
        url = config.initial_page
        main(browser, config)
        browser.quit()
    except Exception:
        if browser:
            browser.quit()

if __name__ == '__main__':

    browser = setup()
    config = Config(browser) #TODO: Pass browser if the crawling is selenium based

    main(browser,config)
    browser.quit()