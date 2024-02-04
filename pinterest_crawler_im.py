from pinterest_crawler.config import Config
from pinterest_crawler.scraper import Scraper



def get_image(keyword):

    configs = Config(search_keywords=keyword, # Search word
                     file_lengths=10,     # total number of images to download (default = "100")
                     image_quality="orig", # image quality (default = "orig")
                     bookmarks="")         # next page data (default= "")


    Scraper(configs).download_images()     # download images directly
    print(Scraper(configs).get_urls())     # just bring image links
