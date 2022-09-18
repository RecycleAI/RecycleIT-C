In this project we try YOLOV5 model on Kaggle data set to create an Object detector using on waste separation procedure.
## Data set prepration
The Kaggle data set contains 4811 images in 4 Aluminium, Glass, PET, and HDPE classes. We use this data set to customize the YOLO algorithm weights based on some related categories of images with our dataset.
In our study:
* 70% of images (3.3K images) were placed in the training set, and 30% were separated as validation and test sets (951 images for the validation set and 471 images for the test set). 
* The images resized into 416x416 pixels. 
* To augment images, the rotation of 90&deg; clockwise and counter clockwise, &plusmn;15% vertical and horizontal shearing and 32% zoom in have been applied which has done with Roboflow website.
## Import the model
In the first step we need to clone the YOLOV5 repository and install requirements.txt. Models and datasets download automatically from the latest YOLOv5 release.
```bash
!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow
```
