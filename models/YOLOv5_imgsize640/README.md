# Train different versions of YOLOv5
In this project, we try the YOLOV5 model on the Kaggle data set to create an Object detector using on waste separation procedure. To train the model, we utilize the Pro version of GPU in Colab. The properties of this GPU are shown below:
<p align="center">
<img width="600" src="https://user-images.githubusercontent.com/74295283/196374934-b0be0d2d-a0da-4646-92d9-2240f46f0d3c.png">
 </p>

## Data set preparation
The Kaggle data set contains 4736 images in 4 Aluminium, Glass, PET, and HDPE classes. We use this data set to customize the YOLO algorithm weights based on some related categories of images with our dataset.
In our study:
* 70% of images (3.3K images) were placed in the training set, and 30% were separated as validation and test sets (944 images for the validation set and 475 images for the test set). 
* The images were resized into 640x640 pixels. 
* To augment images, the rotation of 90&deg; clockwise and counterclockwise, &plusmn;15% vertical and horizontal shearing and 32% zoom-in have been applied, which has been done with the Roboflow website.
## Import model
In the first step, we need to clone the YOLOV5 repository and install requirements.txt. Models and datasets download automatically from the latest YOLOv5 release.
```bash
!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow
```
The data set is available from Roboflow and evoked by the following command:
```bash
from roboflow import Roboflow
rf = Roboflow(api_key="wM8oWAPG8TZirTrzo38g")
project = rf.workspace("sayeh-faraz-dzv2y").project("waste-recycling")
dataset = project.version(4).download("yolov5")
```
Now we can train the YOLOv5 model based on our data set. We trained three versions of this model, which are called YOLOv5s (small), YOLOv5m (medium), and YOLOv5l (large). The below image shows the different kinds and properties of YOLO models.
<p align="center">
<img width="700" src="https://user-images.githubusercontent.com/74295283/196380221-a7ac813e-842a-4902-89cd-b9bcf5fc20ea.png">
 </p>


The following table reports the hyper-parameters in each training procedure:
| Model | epochs | batch size | img size | weights | 
| :--- | :---: | :---: | :---: | :---: |
| **YOLOv5s** | 100 | 32 | 640*640 | yolov5s.pt |
| **YOLOv5m** | 100 | 32 | 640*640 | yolov5m.pt |
| **YOLOv5l** | 100 | 32 | 640*640 | yolov5l.pt |
|  |  |  |  |  |

As an example, the medium version of YOLOv5 is trained by the following code:
```bash
!python train.py --img 640 --batch 32 --epochs 100 --data data.yaml --weights yolov5m.pt
```
## The training results
The **small**, **medium** and **large** version of YOLOv5 model completed 100 epochs in **1.732** hours, **1.923** hours and **2.538** hours.

 The summary of the training procedure for **YOLOv5s**:

_Model summary: 157 layers, 7020913 parameters, 0 gradients, 15.8 GFLOPs_

|Class  |   Images | Instances  |   P    |  R  |   mAP@.5 | mAP@[.5,.95] |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  all  |  944  |  1002 | 0.983 | 0.983 | 0.99 | 0.797  |
|0 Alucan| 944  | 218   |0.986  |  0.959|   0.979    |  0.738 |
|  1 Glass   | 944   |310 |  0.975   |   0.99   |    0.994   |   0.802 |
|  2 HDPE    |    944 |    189   |   0.99   |   0.989   |   0.995   |   0.806 |
|  3 PET |   944   |    285   |   0.981    |  0.993   |   0.992    |  0.842 |
|  |  |  |  |  |  |  |

The summary of the training procedure for **YOLOv5m**:

_Model summary: 212 layers, 20865057 parameters, 0 gradients, 47.9 GFLOPs_

|Class  |   Images | Instances  |   P    |  R  |   mAP@.5 | mAP@[.5,.95]|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  all  |  944  |  1002 | 0.979 | 0.988 | 0.992 | 0.807  |
|0 Alucan| 944  | 218   |0.981  |  0.963|   0.988    |  0.759 |
|  1 Glass   | 944   |310 |  0.96   |   0.994   |    0.994   |   0.805 |
|  2 HDPE    |    944 |    189   |   0.99   |   0.998   |   0.995   |   0.82 |
|  3 PET |   944   |    285   |   0.984    |  0.996   |   0.992    |  0.844 |
|  |  |  |  |  |  |  |

The summary of the training procedure for **YOLOv5l**:

_Model summary: 267 layers, 46124433 parameters, 0 gradients, 107.7 GFLOPs_
|Class  |   Images | Instances  |   P    |  R  |   mAP@.5 | mAP@[.5,.95]|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  all  |  944  |  1002 | 0.99 | 0.982 | 0.993 | 0.816  |
|0 Alucan| 944  | 218   |0.995  |  0.962|   0.992    |  0.766 |
|  1 Glass   | 944   |310 |  0.981   |   0.984   |    0.993   |   0.819 |
|  2 HDPE    |    944 |    189   |   0.996   |   0.989   |   0.995   |   0.823 |
|  3 PET |   944   |    285   |   0.986    |  0.993   |   0.993    |  0.855 |
|  |  |  |  |  |  |  |

## Take inference

After training the model, we saved the resulting weights produced by the model with the name best.pt. Now we can take inferences from the model by uploading the resulting weight with the following command:
```bash 
!python detect.py --weights path/to/the/weights/best.pt --img 640 --conf 0.1 --source {dataset.location}/images
```
## ONNX format
To export our trained model to onnx format, we use the following command:
```bash
!python export.py --weights ../best.pt --data ../data.yaml --include torchscript onnx  --imgsz 640 640
```
