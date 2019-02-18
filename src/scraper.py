
class Scraper:
    def __init__(self,config):
        self.config = config

    # TODO if on-page products, return a list of dictionaries
    def scrape_all_products(self,html_page_text):
        return None

    # TODO return a dictionary containing the product scraped
    def scrape_product(self,html_page_text):
        return None

    def read_total_number_items(self,html_page_text):
        return None

    def extract_field(self, dictionary, first_field_name, second_field_name = None):
        try:
            if not second_field_name:
                return dictionary[first_field_name]
            else:
                return dictionary[first_field_name][second_field_name]
        except Exception as e:
            print(str(e))
            return ""