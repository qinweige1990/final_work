# Import third-party modules
import os
import random
import string

# Import local modules
from photoshop import Session
from psd_tools import PSDImage

from tempfile import mkdtemp
import imghdr
from util import utils
import filetype
from util_main import get_psd_files



@utils.debug_params
def change_size(photo_dir, output_dir, width, height):
    for photo_name in utils.list_files_abs_path(photo_dir):
        try:
            with Session(photo_name, action="open", auto_close=True) as ps:
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, photo_name.split("\\")[-1])
                print(output_dir, photo_name.split("\\")[-1], output_path)
                # resize image
                orig_name = ps.active_document.name
                thumb_name = f"{orig_name}_resize"
                thumb_doc = ps.active_document.duplicate(thumb_name)
                thumb_doc.resizeImage(width, height)
                thumb_doc.saveAs(output_path, ps.PNGSaveOptions(), asCopy=True)
                thumb_doc.close()
        finally:
            continue


@utils.debug_params
def replace_and_save_psd(dir, psd_file, photo_name):
    for photo in utils.list_files_abs_path(dir):
        try:
            with Session(psd_file, action="open", auto_close=True) as ps:
                orig_name = ps.active_document.name
                doc = ps.active_document.duplicate(f'{orig_name}_process')
                for active_layer in doc.layerSets:
                    # layer_set = ps.active_document.layerSets.getByName("画板 9")
                    print(f"current layer {active_layer.name}")
                    replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
                    desc = ps.ActionDescriptor
                    idnull = ps.app.charIDToTypeID("null")
                    input_file = photo
                    print(input_file)
                    desc.putPath(idnull, input_file)
                    ps.app.executeAction(replace_contents, desc)
                psd_output = f'{psd_file}_{photo_name}_{"".join(random.choices(string.digits, k=4))}'
                doc.saveAs(psd_output, ps.PhotoshopSaveOptions(), asCopy=True)
            psd_path = f"{psd_output}.psd"
            all_in_one_photo =  f"{psd_output}.png"
            split_photos_dir = f"{psd_output}/final_photos/{photo_name}"
            os.makedirs(split_photos_dir,exist_ok=True)
            psd = PSDImage.open(psd_path)
            psd.composite().save(all_in_one_photo)
            for layer in psd:
                print(layer)
                layer_image = layer.composite()
                layer_image.save(f'{split_photos_dir}/{layer.name}.png')
        finally:
            continue
