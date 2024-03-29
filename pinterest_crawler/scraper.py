import requests
import json
import os
import urllib
import sys


class Scraper:

    def __init__(self, config, image_urls=[]):
        self.config = config
        self.image_urls = image_urls

    # Set config for bookmarks (next page)
    def setConfig(self, config):
        self.config = config

    # Download images
    def download_images(self):
        folder = "photos/"+self.config.search_keyword.replace(" ", "-")
        number = 0
        # prev get links
        results = self.get_urls()
        try:
            os.makedirs(folder, exist_ok=True)
            print("Directory ", folder, " Created ")
        except FileExistsError:
            a = 1
        arr = os.listdir(folder+"/")
        count = 0
        for i in results:
            count = count+1
            if count > 10:
                break
            try:
                file_name = self.config.search_keyword + str(count) + '.jpg'
                download_folder = str(folder) + "/" + file_name
                print("Download ::: ", i)
                urllib.request.urlretrieve(i,  download_folder)
                number = number + 1
            except Exception as e:
                print(e)

    # get_urls return array
    def get_urls(self):
        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url
        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]
        for i in results:
            img = i["images"][self.config.image_quality]
            if img["width"] > img["height"] and i['reaction_counts'].get('1', 0) > 20:
                self.image_urls.append(img["url"])
                print(img["width"],img["height"], i['reaction_counts']['1'])

        if len(self.image_urls) < int(self.config.file_length):
            self.config.bookmarks = resource_response["bookmark"]
            # print(self.image_urls)
            print("Creating links", len(self.image_urls))
            self.get_urls()
            return self.image_urls[0:self.config.file_length]

        #if len(str(resource_response["bookmark"])) > 1 : connect(query_string, bookmarks=resource_response["bookmark"])



