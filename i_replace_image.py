from process_image import ps
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--psd", type=str)
    parser.add_argument("--name", type=str)
    args = parser.parse_args()
    if args.input is None:
        args.input = input("输入元素所在的文件夹：")
        args.psd = input("输入模版位置：")
        args.name = input("输入保存后的名称：")
    ps.replace_and_save_psd(args.input, args.psd, args.name)