from process_image import ps
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--psd", type=str)
    parser.add_argument("--name", type=str)
    args = parser.parse_args()

    ps.replace_and_save_psd(args.input, args.psd, args.name)