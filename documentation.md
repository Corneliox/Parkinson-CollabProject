# 📝 Project Diary: Parkinson's Dataset Preparation

## 📅 April 20-26, 2025
During this week, I focused on data mining and organizing datasets related to Parkinson's disease hand-drawing analysis (spirals and waves). I gathered approximately 3,500 data samples from various sources and consolidated them into a structured format. Below is the breakdown of the datasets used:

### 🗃️ Dataset Used Path

This project utilizes multiple datasets related to Parkinson’s disease hand-drawing analysis (spirals and waves).  
Below are the datasets organized and described based on their structure:

---

#### 📂 1. [Kaggle - Parkinson's Drawings Dataset](https://www.kaggle.com/datasets/kmader/parkinsons-drawings) (`archive.zip`)
**Folder Structure**:
```
archive/
└── spiral/
    ├── testing/
    │   ├── healthy/
    │   └── parkinson/
    └── training/
        ├── healthy/
        └── parkinson/
└── wave/
    ├── testing/
    │   ├── healthy/
    │   └── parkinson/
    └── training/
        ├── healthy/
        └── parkinson/
```

---

#### 📂 2. [Mendeley Data - Parkinson's Spiral Dataset](https://data.mendeley.com/datasets/fd5wd6wmdj/1) (`Parkinson’s Disease Detection Using Spiral Images (Hand Drawings).zip`)
**Folder Structure**:
```
Parkinson’s Disease Detection Using Spiral Images (Hand Drawings)/
└── Parkinson Dataset/
    └── dataset/
        ├── spiral/
        │   ├── testing/
        │   └── training/
        └── wave/
            ├── testing/
            └── training/
```

---

#### 📂 3. [Kaggle - Handwritten Parkinson’s Disease (Augmented)](https://www.kaggle.com/datasets/banilkumar20phd7071/handwritten-parkinsons-disease-augmented-data) (`dataset.zip`)
**Folder Structure**:
```
Dataset/
├── Healthy/
└── Parkinson/
```

---

#### 📂 4. [HandPD - UNESP Handwritten Parkinson’s Dataset](https://wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/)
**Folder Structure**:
```
HealthySpiral/
└── HealthySpiral/

PatientSpiral/
└── PatientSpiral/
```
---
---

## 📅 April 28, 2025
Today, I began the process of resizing all collected images to a uniform size of 512x512 pixels. This step is crucial for ensuring consistency in the dataset for training the database model. Additionally, I started annotating the images to prepare them for further analysis and model training.

### 🛠️ Tasks Completed:
- Resized images to 512x512 pixels.
- Began annotating the dataset for training purposes.

## 📝 Resize Method Explanation

In the dataset pre-processing step, all hand-drawing images were resized to a fixed dimension of **512 × 512 pixels** using the **LANCZOS resampling method**.

---

### 📏 Why Resizing?

- To standardize the input dimensions for the YOLO models.
- To ensure consistent training and inference performance across the dataset.

---

### 📐 Why 512×512?

- **512** is a common size that balances:
  - Detail preservation
  - Computational efficiency
- It is a good compromise between memory usage and model accuracy, especially important when handling medical image datasets.

---

### 🔍 Resizing Method Used

- **LANCZOS interpolation** (also known as Lanczos resampling).

---

### 🧠 About LANCZOS

- A **high-quality resampling algorithm** based on the sinc function.
- Designed for **both downscaling and upscaling** images.
- Preserves **more fine details** compared to simpler methods like bilinear or nearest neighbor.
- Especially effective when high accuracy in preserving edges and fine details is important — **critical for medical datasets**, such as Parkinson's hand-drawing tasks.

---

### 🛠 Technical Note

- Implemented via **Python's Pillow (PIL) library**.
- Accessed by using the flag: `Image.LANCZOS`.
- It is considered **the best choice** when resizing datasets where fine-grained distortions (e.g., tremors in spiral drawings) must be preserved.

---

### 📚 Short Summary for Report

> All images were resized to **512 × 512 pixels** using the **LANCZOS interpolation method** to preserve fine details and ensure standardized input size for model training.

---
---

## 📅 April 29, 2025
#### 8.28 A.M
Succesfully splitting into 80/20 - 70/30 and changing my format into 

[**Parkinson's Drawings**](https://www.kaggle.com/datasets/kmader/parkinsons-drawings) by "K Scott Mader"

Uploading it into 

- 70/30 Drawing : [**Parkinson's Drawings**](https://www.kaggle.com/datasets/kmader/)
- 80/20 Drawing : [**Parkinson's Drawings**](https://www.kaggle.com/datasets/kmader/)

#### 5.55 P.M
Deciding to auto annotate the Data based on file name, rememmbering that i had already split the data name by coincidence before, with logic of : 

```
Image format 512 x 512

Make label 
0 : healthy spiral
1 : healthy wave
2 : parkinson spiral
3 : parkinson wave

For each folder who had "Healthy" in folder spiral :
- Make label 0 with full  Bounding Box (annotate full resolution of images)
Else : 
- make label 2 with full Bounding Box (annotate full resolution of images)

For each folder who had "Wave" in folder wave :
- Make label 1 with full  Bounding Box (anotate all images)
Else : 
- make label 3 with full Bounding Box (annotate full resolution of images)
```

--- 
---
## 📅 April 30 - Mei 1, 2025
### April 30 
dataset already Moved all into a new dataset and can be annotated Automatically for boxes, and so and so, dont seems any prolem occure during the process, keep continuing.

### Mei 1 
#### 8 AM 
Error Occure on ne Name applied there, which Some Duplicated, but the problem resolved clear

#### 10 AM 
Problem Occure when i want to simplify the Tree Directory from 

```
📁 YOLODataset/ 
├── 📁 spiral/
│   ├── 📁 images/
│   │   ├── 📁 train/ (image here) 
│   │   └── 📁 val/ (image here) 
│   └── 📁 labels/
│       ├── 📁 train/
│       └── 📁 val/
├── 📁 wave/
│   ├── 📁 images/
│   │   ├── 📁 train/ (image here) 
│   │   └── 📁 val/ (image here) 
│   └── 📁 labels/
│       ├── 📁 train/
│       └── 📁 val/
└── 📄 spiral.yaml
└── 📄 wave.yaml
```
Into something more simpler into this path : 
```
📁 YOLODatasetFull/
├── 📁 images/
│   ├── 📁 train/
│   └── 📁 val/
├── 📁 labels/
│   ├── 📁 train/
│   └── 📁 val/
└── 📄 parkinson_full.yaml
```

Which encoutering More problem when **Name was Crashed each other**... , Logic that may solve this was 

***Auto rename it all***

#### 11.47 AM
Thanks to ChatGPT for the great help for minimalizing time, All File already Renamed.. The Workflow Should be 

```python
-> util_512Mod.py  #Resizing all image into 512
    -> util_512toYolo.py #Change into Yolo Format File
        -> util_rename.py #Change name into one format to help labelling
            -> util_autolabeling.py #Auto Label because 1 image, 1 item
                -> util_merge_to_4_class_yolo.py #merge into Train and Val Yolo Only
```

#### 12.00 AM 
After Merge into Train and Val Format Only 
```
📁 YOLODatasetFull/
├── 📁 images/
│   ├── 📁 train/
│   └── 📁 val/
├── 📁 labels/
│   ├── 📁 train/
│   └── 📁 val/
└── 📄 parkinson_full.yaml
```
You can use `change_split_gui_selecteble.py` to change Ratio

#### 12.50 PM 
Revising the logic on `change_split_gui_selecteble.py` so it will : 
- Recursively find all images inside   `images/`
- Flatten dan re-split ecerything into a fresh new train/val structure
- Move `.txt` labels to match

#### 13.00 PM 
Error occured multiple times, further update will be created after Finishing project

## 📅 Mei 2, 2025

#### 10.00 AM 
Got Not Implemented Error, need to validate Yolo Labels on image and val

#### 10.13 
Torch vision Eror : 

```
NotImplementedError: Could not run 'torchvision::nms' with arguments from the 'CUDA' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using custom build). If you are a Facebook employee using PyTorch on mobile, please visit https://fburl.com/ptmfixes for possible resolutions. 'torchvision::nms' is only available for these backends: [CPU, Meta, QuantizedCPU, BackendSelect, Python, FuncTorchDynamicLayerBackMode, Functionalize, Named, Conjugate, Negative, ZeroTensor, ADInplaceOrView, AutogradOther, AutogradCPU, AutogradCUDA, AutogradXLA, AutogradMPS, AutogradXPU, AutogradHPU, AutogradLazy, AutogradMeta, Tracer, AutocastCPU, AutocastXPU, AutocastMPS, AutocastCUDA, FuncTorchBatched, BatchedNestedTensor, FuncTorchVmapMode, Batched, VmapMode, FuncTorchGradWrapper, PythonTLSSnapshot, FuncTorchDynamicLayerFrontMode, PreDispatch, PythonDispatcher].
 ```

An error cauused by mismatch on `torchvision` not installed with CUDA support, solution : 
- Reinstall `torchvision` with cuda support

#### 11.30 
Train for first time with settings : 
```
| Parameter        | Your Value         | Recommended for RTX 2050 4GB |
|------------------|--------------------|------------------------------|
| **Image Size**   | 512                | ✅ OK (recommended)          |
| **Batch Size**   | 16                 | ⚠️ Likely too high — use 4–8 |
| **Epochs**       | 75                 | ✅ OK                        |
| **Train Images** | ~3500              | ✅ OK                        |
| **Model**        | yolov8x            | ⚠️ Use `yolov8n/s.pt`        |
```

#### 12.30 PM
Train using s and n series also reduce the batch for better performance

#### 15.30 PM
**8s** Did Great Job there but memory usage just 1 from 4 Gigs available, gonna upgrade the **Batch** into 8 and using model 8m for test

Result : 
```
Model: yolov8s_model
Validation Time: 2025-05-02 14-34-22

AP50: 0.8599
AP: 0.8557
Precision: 0.7571
Recall: 0.8728
F1-Score: [0.5822, 0.8804, 0.7444, 0.9025]

TIme elapsed : 122 Minutes
```

#### 23.52 
Running the Yolo 8m series with 12 Batch, and 50 Epoch 

## 📅 Mei 3, 2025
#### 5.30 A.M
The training done with i think overfiting in lot cases lets see the Metrics
```
Model: yolov8_model
Validation Time: 2025-05-03 04-18-51

AP50: 0.8477
AP: 0.8426
Precision: 0.7549
Recall: 0.8698
F1-Score: [0.6349, 0.8725, 0.8009, 0.8483]

Time Elapsed : 4.385 Hours
```
Got Overfitted on 25 actually dont move that much, but also the batch didnt do anything on it, just causing laggy xD 

#### 6.00 AM 
After comparing the time needed and memory usage and all, the default test will be using 
``` python 
batch = 8 
epoch = 50
```

#### 6.10 AM 
8 Batch seems to large for Yolov3, For any Model That seems largered a bit, will do it on google colab

#### 6.41
Commting Training for YOLOv5m