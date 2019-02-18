import threading
from src.main_scraping_task import run_scraping_task

class CrawlingThreading:
    def __init__(self,url):
        self.url = url
        thread = threading.Thread(target=self.run,args=())
        thread.daemon = True
        thread.start()

    def run(self):
        print('Thread to crawl freida has started')
        run_scraping_task()
