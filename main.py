import os.path

import argparse
import logging
from get_image import pinterest
import get_words.google_trend
import process_image.ps


def logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()  # 默认输出到sys.stderr，也可传sys.stdout等作为参数改变输出位置
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    logger = logger()
    this_root = os.path.dirname(__file__)

    # --word 支持输入关键词,如果没有输入，会从飞鱼读取
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str)
    parser.add_argument("--num", default=10, type=int)
    parser.add_argument("--skip", default=False, type=bool)
    args = parser.parse_args()
    if args.word != None:
        words = str.split(args.word, ",")
        logging.info(f'输入的热词是：{words}')
    else:
        # words = get_words.get_word.get_hot_words()
        words = get_words.google_trend.get_google_trend()
        logging.info(f"拉取数据，排名前{args.num}的数据是", words[:args.num])

    # 从pinterest获取图片并保存
    number = args.num if args.num is not None else 2
    for word in words[:number]:
        if not args.skip:
            pinterest.get_image(word)
        word = word.replace(" ", "-")
        photo_dir = os.path.join(this_root, f"process_image/photos/{word}")
        output_dir = os.path.join(this_root, f"process_image\\resized_photos\\{word}")
        process_image.ps.change_size(photo_dir, output_dir, 3840,2160)

        process_image.ps.replace_and_save_psd(output_dir, os.path.join(this_root, 'files/template.psd'), word)
    logging.info("处理完成")
