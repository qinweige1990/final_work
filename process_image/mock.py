import os




def change_size(name, width, height):
    this_root = os.path.dirname(__file__)
    photo_dir = os.path.join(this_root, "photos")
    photo_path = os.path.join(photo_dir, name)
    resized_photo_path = os.path.join(this_root, "resized_photos")
    os.makedirs(resized_photo_path, exist_ok=True)
    output_path = os.path.join(resized_photo_path, f"{name}.jpg")
    print(f"output_path: {output_path}")
    return output_path

def replace_and_save_psd(photo, psd_file, name):
    psd_path = os.path.join(os.path.dirname(__file__), f"files/{psd_file}")
    all_in_one_photo = os.path.join(os.path.dirname(__file__), f"final_photos/{name}.png")
    split_photos_dir = os.path.join(os.path.dirname(__file__), f"final_photos/{name}")
    os.makedirs(split_photos_dir, exist_ok=True)
    print(f'替换并保存，all_in_one: {all_in_one_photo}, split_photo_dir: {split_photos_dir}')



