# Overview
### This program lets you download tons of images from Google and crop specific objects in images.

- #### -k, --Keyword: keyword that you want to search in google
- #### -l, --Limit: number of images you want to download
- #### -t, --Type: type of images (in this project it must be one of the plastic types, glass or aluminium)
- #### -c, --Class: specific coco object that you want to detect and crop (for example in this project we chose "bottle" class)

# Usage
### 1. Clone the repositories.
```bash
$ git clone https://github.com/RecycleAI/RecycleIT-C.git
$ cd ./RecycleIT-C/src/tools/image_scraper
```


### 2. Install
Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

### 3. Run main.py
```bash
$ python main.py -k "PET bottle" -l 20 -t "PET"
```
