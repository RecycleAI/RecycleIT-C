import os
import shutil
import argparse
import numpy as np
import torch
from PIL import Image
from google_images_download import google_images_download


def filter_and_crop(keyword, img_type, coco_class):
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
    # Images
    # Get the list of all files and directories
    path = os.path.join("scraper/downloads", keyword)
    dir_list = os.listdir(path)
    # print("Files and directories in '", path, "' :")
    for img in dir_list:
        old_name = os.path.join(path, img)
        new_name = os.path.join(path, str(np.random.rand(1, )[0]) + ".jpg")
        os.rename(old_name, new_name)
        # Inference
        results = model(new_name)
        # Results
        results.crop(save_dir='scraper/runs/detect/exp')  # or .show(), .save(), .crop(), .pandas(), etc.
    dir_path = os.path.join("scraper", keyword)
    try:
        os.mkdir(dir_path)
    except:
        print("dir exist")

    for x in os.walk("scraper/runs/detect"):
        if x[0].endswith(coco_class):
            img_path = x[0]
            img_dir_list = os.listdir(img_path)
            for img in img_dir_list:
                random_name = str(np.random.rand(1, )[0])
                image_name = '%s-%s.jpg' % (img_type, random_name)
                img_final_path = os.path.join(dir_path, image_name)
                im1 = Image.open(os.path.join(img_path, img))
                im1.save(img_final_path)
    shutil.rmtree('scraper/runs')
    shutil.rmtree('scraper/downloads')


def image_scraper(keyword, image_num, img_type, coco_class):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword, "limit": image_num, "print_urls": False,
                 "output_directory": "scraper/downloads"}
    response.download(arguments)
    filter_and_crop(keyword, img_type, coco_class)


def main():
    search_name = "PET bottle"
    images_num = 20
    images_type = "PET"
    coco_class = "bottle"

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-k", "--Keyword", help="keyword that we want to search")
    parser.add_argument("-l", "--Limit", help="number of images we want to collect")
    parser.add_argument("-t", "--Type",
                        help="image type (in this case it must be one of the plastic types or glass or aluminium)")
    parser.add_argument("-c", "--Class", help="coco class in this project it is bottle class")

    # Read arguments from command line
    args = parser.parse_args()

    if args.Keyword:
        search_name = args.Keyword
    if args.Limit:
        images_num = args.Limit
    if args.Type:
        images_type = args.Type
    if args.Class:
        coco_class = args.Class

    print(f"{search_name}, {images_num}, {images_type}, {coco_class}")
    image_scraper(search_name, images_num, images_type, coco_class)


if __name__ == "__main__":
    main()
