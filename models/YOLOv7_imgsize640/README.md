In this project we try YOLOV7 model on Kaggle data set to create an Object detector using on waste separation procedure.
## Data set prepration
The Kaggle data set contains 4811 images in 4 Aluminium, Glass, PET, and HDPE classes. We use this data set to customize the YOLO algorithm weights based on some related categories of images with our dataset.
In our study:
* 70% of images (3.3K images) were placed in the training set, and 30% were separated as validation and test sets (944 images for the validation set and 475 images for the test set). 
* The images resized into 416x416 pixels. 
* To augment images, the rotation of 90&deg; clockwise and counter clockwise, &plusmn;15% vertical and horizontal shearing and 32% zoom in have been applied which has done with Roboflow website.
## Import the model
In the first step we need to clone the YOLOV7 repository and install requirements.txt. Models and datasets download automatically from the latest YOLOv7 release.
```bash
!git clone https://github.com/WongKinYiu/yolov7  # clone repo
%cd yolov7
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow
```
The data set is available from Roboflow and evoked by the following command:
```bash
from roboflow import Roboflow
rf = Roboflow(api_key="wM8oWAPG8TZirTrzo38g")
project = rf.workspace("sayeh-faraz-dzv2y").project("waste-recycling")
dataset = project.version(3).download("yolov7")
```
Now we can train the YOLOv7 model based on our data set. In the following, you can find the training parameters:
| Model | epochs | batch size | img size | weights | 
| :--- | :---: | :---: | :---: | :---: |
| **YOLOv7** | 100 | 32 | 640*640 | yolov7.pt |
|  |  |  |  |  |

To train the model, run the following code:
```bash
!python train.py --img 640 640 --batch 32 --epochs 100 --data {dataset.location}/data.yaml --cfg cfg/training/yolov7.yaml --weights yolov7.pt --device 0 --name yolov7 --hyp data/hyp.scratch.p5.yaml --workers 8
```
## The training results
The model has been trained in 100 epochs in 4.567 hours. The training procedure's summary and the model's performance are reported in the following table and illustrated in the figure below.

Model Summary: 415 layers, 37212738 parameters, 37212738 gradients, 105.2 GFLOPS

|Class  |   Images | Instances  |   P    |  R  |   mAP@.5 | mAP@[.5,.95]|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  all  |  944  |  1002 | 0.982| 0.985|0.99  |  0.813 |
|0 Alucan| 944  | 218   |0.977 | 0.972|0.982 |  0.756|
|1 Glass | 944  | 310   |0.974 | 0.98 |  0.99 |   0.809|
|2 HDPE  | 944  | 189   |0.989 | 0.995| 0.996  |   0.836|
|  3 PET | 944  |  285  |0.988 | 0.993| 0.994  |  0.852|
|  |  |  |  |  |  |  |

<p align="center">
  <img width="900"src="https://user-images.githubusercontent.com/74295283/196716968-6bcc92f3-cf63-493f-9435-a044672f46c7.png">
</p>

## Take inference

After training the model, we saved the resulting weights produced by the model with the name best.pt. Now we can take inferences from the model by uploading the resulting weight with the following command:
```bash 
!python detect.py --weights runs/train/yolov7/weights/best.pt --img 640 --conf 0.1 --source {dataset.location}/test/images
```
## ONNX format
In order to export our trained model to onnx format, we use the following command:
```bash
!python export.py --weights ../best.pt --data ../data.yaml --include torchscript onnx  --imgsz 640 640
```

