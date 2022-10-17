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
The data set is available from Roboflow and evoked by:
```bash
from roboflow import Roboflow
rf = Roboflow(model_format="yolov5", api_key="zuV4MGwLFCgU3zoG6lrJ")
project = rf.workspace("recycle-2uipy").project("waste-separation-dnpvc")
dataset = project.version(1).download("yolov5")
```
Now we can train the YOLOv5 model based on our own data set. In the following you can find the training parameters:
| Model | epochs | batch size | img size | weights | 
| :--- | :---: | :---: | :---: | :---: |
| **YOLOv5s** | 100 | 16 | 416*416 | yolov5s.pt |
|  |  |  |  |  |

To train the model, run the following code:
```bash
!python train.py --img 416 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt
```
## The training results
The model has been trained in 2.518 hours. The summery of the training procedure:

Model summary: 213 layers, 7020913 parameters, 0 gradients, 15.8 GFLOPs
|Class  |   Images | Instances  |   P    |  R  |   mAP@.5 | mAP@.5:.95: 100% 30/30 [00:07<00:00,  3.96it/s]|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  all  |  949  |  1001 | 0.988 | 0.985 | 0.989 | 0.82  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0 Alucan| 949  | 237   |0.979  |  0.966|   0.978    |  0.744 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  1 Glass   |     949   |     271    |  0.983   |   0.985   |    0.99   |   0.827 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  2 HDPE    |    949    |    209   |   0.999   |   0.995   |   0.995   |   0.847 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  3 PET     |   949    |    284   |   0.993    |  0.993   |   0.992    |  0.859 |
|  |  |  |  |  |  |  |

## Take inference

After training the model, we saved the resulted weights which produced by model with the name of best.pt. Now we are be able to take inference from the model by uploading the resulted wieght with the following command:
```bash 
!python detect.py --weights path/to/the/weights/best.pt --img 416 --conf 0.1 --source {dataset.location}/images
```
## ONNX format
In order to export our trained model to onnx format, we use the following command:
```bash
!python export.py --weights ../best.pt --data ../data.yaml --include torchscript onnx  --imgsz 416 416
```
