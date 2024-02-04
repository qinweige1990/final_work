import get_words.get_word
import argparse
import logging
import pinterest_crawler_im
from get_image import pinterest

def logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()  # 默认输出到sys.stderr，也可传sys.stdout等作为参数改变输出位置
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    logger = logger()
    # --word 支持输入关键词,如果没有输入，会从飞鱼读取
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str)
    parser.add_argument("--num", default=10, type=int)
    args = parser.parse_args()
    if args.word != None:
        words = str.split(args.word, ",")
        logging.info(f'输入的热词是：{words}')
    else:
        words = get_words.get_word.get_hot_words()
        logging.info(f"拉取到飞鱼的数据，排名前{args.num}的数据是", words[:args.num])

    # 从pinterest获取图片并保存
    for word in words:
        pinterest.get_image(word)

    # pinterest_crawler_im.get_image(word)

    # 调用photoshop来resize所有的图片并保存


    # 调用photoshop的replace来替换模版中的图片并保存



    logging.info("处理完成")
