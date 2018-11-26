__author__ = 'mkesavan'

# Imports
import glob
import os.path
import re
import argparse
from pathlib import Path
import shutil


FLAGS = None

def create_labels(image_src_dir,image_target_dir, labels_dir ):
    images_path = Path(image_src_dir)
    labels_path = Path(labels_dir)
    # target_path = Path(image_target_dir)
    images_list = []
    labels_list = []

    for colordir in images_path.iterdir():
        color = colordir.name
        if(color == '.DS_Store'):
            continue
        print('color: '+ color)
        if colordir.is_dir() :
            for phonedir in colordir.iterdir():
                phone = phonedir.name
                if (phone == '.DS_Store'):
                    continue
                print('phone: '+ phone)
                if phonedir.is_dir() :
                    for image_file in phonedir.iterdir():
                        image_file_name = image_file.name
                        if(image_file_name == '.DS_Store'): 
                            continue
                        # copy files
                        shutil.copy(image_file,image_target_dir)
                        # create label text file
                        print("image file name:" + image_file_name)
                        labels = [phone,color]
                        labels_file = labels_path / (image_file_name + ".txt")
                        labels_file.write_text("\n".join(labels))
                        images_list.append(str(image_file))
                        if(phone not in labels_list):
                            labels_list.append(phone)
                        if (color not in labels_list):
                            labels_list.append(color)
    # write labels into labels file
    all_labels_file = labels_path.parent / "labels.txt"
    all_labels_file.write_text("\n".join(labels_list))
    return images_list,labels_list




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image_src_dir',
        type=str,
        default='',
        help='Path to folder of src images'
    )
    parser.add_argument(
        '--image_target_dir',
        type=str,
        default='',
        help='Where to save all images collated'
    )
    parser.add_argument(
        '--labels_dir',
        type=str,
        default='',
        help='Where to save labels'
    )

    FLAGS, unparsed = parser.parse_known_args()

    create_labels(FLAGS.image_src_dir, FLAGS.image_target_dir, FLAGS.labels_dir)
