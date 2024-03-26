

import argparse
import process_image.ps


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    args = parser.parse_args()
    if args.input is None:
        args.input = input("输入要调整尺寸处理的文件夹：")
        args.output = input("输入处理完成照片存储的位置：")
        args.width = input("输入要调整尺寸的宽度：")
        args.height = input("输入要调整尺寸的高度：")
    process_image.ps.change_size(args.input, args.output, args.width, args.height)


