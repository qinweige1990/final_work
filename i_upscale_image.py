import process_image.upscale
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()
    if args.input is None:
        args.input = input("输入要高清化处理的文件夹：")
        args.output = input("输入处理完成照片存储的位置：")
    process_image.upscale.upscale_image(args.input, args.output)
