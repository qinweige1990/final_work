import os.path

import get_words.get_word
import argparse
import logging
import pinterest_crawler_im
from get_image import pinterest
import get_words.google_trend
import process_image.mock

def logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()  # 默认输出到sys.stderr，也可传sys.stdout等作为参数改变输出位置
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    logger = logger()
    this_root = os.path.dirname(__file__)
    print("start")
    # --word 支持输入关键词,如果没有输入，会从飞鱼读取
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str)
    parser.add_argument("--num", type=int)
    parser.add_argument("--skip", default=False, type=bool)
    args = parser.parse_args()
    if args.word != None:
        words = str.split(args.word, ",")
        args.num = len(words)
        print(f'输入的热词是：{words}')
    else:
        # words = get_words.get_word.get_hot_words()
        words = get_words.google_trend.get_google_trend()
        print(f"拉取数据，排名前{args.num}的数据是", words[:args.num])

    # 从pinterest获取图片并保存
    number = args.num if args.num is not None else 2
    for word in words[:number]:
        if not args.skip:
            pinterest.get_image(word)