import os




def change_size(dir, photo_name, width, height):
    this_root = os.path.dirname(__file__)
    photo_dir = os.path.join(this_root, f"photos/{dir}")
    photo_path = os.path.join(photo_dir, photo_name)
    print(photo_path, photo_dir)
    resized_photo_path = os.path.join(this_root, f"resized_photos/{dir}")
    os.makedirs(resized_photo_path, exist_ok=True)
    output_path = os.path.join(resized_photo_path, photo_name)
    print(f"output_path: {output_path}")
    return output_path

def replace_and_save_psd(photo, psd_file, name):
    psd_path = os.path.join(os.path.dirname(__file__), f"files/{psd_file}")
    all_in_one_photo = os.path.join(os.path.dirname(__file__), f"final_photos/{name}.png")
    split_photos_dir = os.path.join(os.path.dirname(__file__), f"final_photos/{name}")
    print(f'photo path: {photo}')
    os.makedirs(split_photos_dir, exist_ok=True)



