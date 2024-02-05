# Import third-party modules
import os
# Import local modules
from photoshop import Session
from psd_tools import PSDImage
from tempfile import mkdtemp

def get_psd_files():
    files = {}
    this_root = os.path.dirname(__file__)
    file_root = os.path.join(this_root, "files")
    for file_name in os.listdir(file_root):
        files[file_name] = os.path.join(file_root, file_name)
    return files


def change_size(dir, photo_name, width, height):
    this_root = os.path.dirname(__file__)
    photo_dir = os.path.join(this_root, f"photos/{dir}")
    photo_path = os.path.join(photo_dir, photo_name)
    with Session(photo_path, action="open") as ps:
        resized_photo_path = os.path.join(this_root, f"resized_photo/{dir}")
        os.makedirs(resized_photo_path, exist_ok=True)
        output_path = os.path.join(resized_photo_path, photo_name)
        # resize image
        if os.name == "nt":
            orig_name = ps.active_document.name
            thumb_name = f"{orig_name}_resize"
            thumb_doc = ps.active_document.duplicate(thumb_name)
            thumb_doc.resizeImage(width, height)
            thumb_doc.saveAs(output_path, ps.JPEGSaveOptions(), asCopy=True)
            thumb_doc.close()
        else:
            print("not windows, pass resize")
    return output_path

def replace_and_save_psd(photo, psd_file, name):
    with Session(psd_file, action="open") as ps:
        for active_layer in ps.active_document.layerSets:
            # layer_set = ps.active_document.layerSets.getByName("画板 9")
            print(f"current layer {active_layer.name}")
            replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
            desc = ps.ActionDescriptor
            idnull = ps.app.charIDToTypeID("null")
            desc.putPath(idnull, photo)
            ps.app.executeAction(replace_contents, desc)
    psd_path = os.path.join(os.path.dirname(__file__), f"files/{psd_file}")
    all_in_one_photo = os.path.join(os.path.dirname(__file__), f"final_photos/{name}.png")
    split_photos_dir = os.path.join(os.path.dirname(__file__), f"final_photos/{name}")
    psd = PSDImage.open(psd_path)
    psd.composite().save(all_in_one_photo)
    for layer in psd:
        print(layer)
        layer_image = layer.composite()
        layer_image.save(f'{split_photos_dir}/{layer.name}.png')


