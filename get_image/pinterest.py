import os
import urllib

from apify_client import ApifyClient
import json
import requests
from PIL import Image
from io import BytesIO


def get_image(name: str):
    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_cgdkO2Br3SILtjnJlG9DbKFheZdzON37DMHK")

    # Prepare the Actor input
    run_input = {
        "includeComments": False,
        "maxItems": 200,
        "endPage": 5,
        "extendOutputFunction": "($) => { return {} }",
        "customMapFunction": "(object) => { return {...object} }",
        "proxy": {"useApifyProxy": True},
        "search": name,
    }
    print("开始拉取pinterest数据，搜索词：", name)
    print("----------------------------------")
# Run the Actor and wait for it to finish
    run = client.actor("rusvWpGtw0MugV2j4").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    pins = client.dataset(run['defaultDatasetId']).iterate_items()
    sortedPins = sorted(pins, key=lambda x: x['pinner_follower_count'], reverse=True)
    print(f"拉取到{len(sortedPins)}张图片，选取评论数最高的图片并保存")
    print("----------------------------------")
    folder = "process_image/photos/"+name.replace(" ", "-")
    os.makedirs(folder, exist_ok=True)
    number = 0
    max = 10
    for item in sortedPins:
        try:
            image = item["images"]["orig"]
            width = image.get('width', 0)
            height = image.get('height', 0)
            if width > height:
                # 照片的URL地址
                url = item["images"]["orig"]["url"]
                file_name = name + str(number) + '.png'
                print("find one image",file_name)
                download_folder = str(folder) + "/" + file_name
                print("Download ::: ", url)
                urllib.request.urlretrieve(url,  download_folder)
                number = number + 1
            if number >= max:
                break
        finally:
            continue
'''
            # 使用requests库来获取照片
            response = requests.get(url)

            # 将获取到的二进制数据转化为可操作的图像
            image = Image.open(BytesIO(response.content))

            # 使用save方法保存图像到本地
            imageName = "local" + '.jpg'
            image.save(imageName)
'''
