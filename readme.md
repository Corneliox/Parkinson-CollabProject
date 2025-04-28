
# 🧠 Parkinson Detection via Hand-Drawn Spirals & Waves using YOLO

This project focuses on evaluating various YOLO models for detecting signs of **Parkinson's disease** from hand-drawn **spiral and wave images**. The goal is to compare models from **YOLOv3 to YOLOv11**, including **segmentation support in YOLOv9–YOLOv11**, under consistent preprocessing and data split settings.

---

## 📊 Experiment Setup & Comparison Table

| Dataset Type        | YOLO Version | Model Type  | Segmented | Augmented | Train/Test Split | Metrics Compared        | Notes                       |
|---------------------|--------------|-------------|-----------|-----------|------------------|--------------------------|-----------------------------|
| Spiral + Wave       | YOLOv3       | Detection   | No        | Yes       | 80/20            | mAP, Precision, Recall   | Classic YOLOv3 baseline     |
| Spiral + Wave       | YOLOv3       | Detection   | No        | No        | 80/20            | mAP, Precision, Recall   | No augmentation baseline    |
| Spiral + Wave       | YOLOv4       | Detection   | No        | Yes       | 70/30            | mAP, Precision, Recall   |                             |
| Spiral + Wave       | YOLOv4       | Detection   | No        | No        | 70/30            | mAP, Precision, Recall   |                             |
| Spiral + Wave       | YOLOv5       | Detection   | No        | Yes       | 80/20            | mAP, F1-score, Loss      | Ultralytics                 |
| Spiral + Wave       | YOLOv5       | Detection   | No        | No        | 80/20            | mAP, F1-score, Loss      |                             |
| Spiral + Wave       | YOLOv6       | Detection   | No        | Yes       | 70/30            | mAP, F1-score, Loss      | Ultralytics                 |
| Spiral + Wave       | YOLOv6       | Detection   | No        | No        | 70/30            | mAP, F1-score, Loss      |                             |
| Spiral + Wave       | YOLOv7       | Detection   | No        | Yes       | 80/20            | mAP, F1-score, Loss      |                             |
| Spiral + Wave       | YOLOv7       | Detection   | No        | No        | 80/20            | mAP, F1-score, Loss      |                             |
| Spiral + Wave       | YOLOv8       | Detection   | No        | Yes       | 70/30            | mAP, F1-score, Loss      |                             |
| Spiral + Wave       | YOLOv8       | Detection   | No        | No        | 70/30            | mAP, F1-score, Loss      |                             |
| Spiral + Wave       | YOLOv9       | Segmentation| Yes       | Yes       | 80/20            | mAP50, IoU, Loss         | Segmented version tested    |
| Spiral + Wave       | YOLOv9       | Segmentation| Yes       | No        | 80/20            | mAP50, IoU, Loss         |                             |
| Spiral + Wave       | YOLOv10      | Segmentation| Yes       | Yes       | 70/30            | mAP50, IoU, Loss         |                             |
| Spiral + Wave       | YOLOv10      | Segmentation| Yes       | No        | 70/30            | mAP50, IoU, Loss         |                             |
| Spiral + Wave       | YOLOv11      | Segmentation| Yes       | Yes       | 80/20            | mAP50, IoU, Loss         |                             |
| Spiral + Wave       | YOLOv11      | Segmentation| Yes       | No        | 80/20            | mAP50, IoU, Loss         |                             |

---

## 🧪 Experiment Setup Instructions

This project evaluates YOLO models from **YOLOv3 to YOLOv11**, focusing on hand-drawn patterns that are indicative of Parkinson's Disease. Two types of input (spirals and waves) are used with consistent preprocessing.

---

### 📁 Dataset Details
- **Content**: Hand-drawn spirals and waves
- **Purpose**: Parkinson detection
- **Image Resolution**: 512 x 512 px
- **Labels**: Binary (Parkinson / Non-Parkinson)
  - Healthy Spiral
    - A smoothly drawn, nearly perfect circle. The line is consistent in thickness, without tremors, hesitations, or irregularities. The spacing within the circle, if it's a spiral, is even. The circle is well-formed and controlled.
  - Healthy Wave
    - The waveform exhibits a consistent and somewhat rectangular shape with rounded peaks and troughs. The upward slope (representing exhalation) is relatively steep and consistent across cycles. The plateau at the peak is fairly level. The downward slope (representing inhalation) is also relatively steep and returns cleanly to the baseline. The cycles appear regular and uniform in width and height, indicating consistent and even breathing. There are no significant irregularities, sharp peaks, or unevenness in the pattern.
  - Patient Spiral
    -  The spiral drawing exhibits a noticeably irregular and shaky line, indicative of tremor. The spacing between the loops varies significantly, and the overall form lacks the smooth, consistent expansion seen in a healthy spiral. There are visible hesitations and minor changes in direction, resulting in a less controlled and somewhat jagged appearance.
  - Patient Wave
    - The waveform shows an irregular pattern. The upward and downward slopes are uneven, and the plateaus at the peaks are inconsistent. The cycles vary in width and height, indicating an unsteady breathing pattern.
- **Annotation**: 
  - Bounding boxes for detection (LabelImg, Roboflow)
  - Masks for segmentation (Roboflow recommended)

---

### 🧹 Preprocessing
- **Augmented Version**:
  - Random rotation
  - Scaling
  - Brightness/contrast
- **Non-Augmented Version**: Raw input only
- All images resized to **512 x 512**

---

### 🧠 Models Used

| Model Type     | Versions     | Framework      | Notes                          |
|----------------|--------------|----------------|--------------------------------|
| Detection      | YOLOv3 - v8  | Ultralytics & Darknet | Classic object detection     |
| Segmentation   | YOLOv9 - v11 | Ultralytics    | For region-based detection     |

Each model is trained under two data splits:
- **80/20** (Train/Test)
- **70/30** (Train/Test)

Common training setup:
```
imgsz=512
epochs=50
batch=16
```

---

### ⚙️ Training Command Examples

#### 🔹 Detection (YOLOv5 - YOLOv8)
```bash
yolo task=detect mode=train model=yolov8n.pt data=parkinson.yaml epochs=50 imgsz=512
```

#### 🔹 Segmentation (YOLOv9 - YOLOv11)
```bash
yolo task=segment mode=train model=yolov9n-seg.pt data=parkinson.yaml epochs=50 imgsz=512
```

---

### 📊 Evaluation Metrics
- **Detection**: `mAP@0.5`, `Precision`, `Recall`, `F1-score`, `Loss`
- **Segmentation**: `mAP@0.5`, `IoU`, `Segmentation Loss`

---

### 📈 Output
All model results (metrics, losses, etc.) will be compiled into a structured **Excel sheet** for direct comparison. These will help identify the best-performing model configuration for Parkinson's pattern detection.

---

Feel free to contribute or experiment with new augmentations, split ratios, or model tweaks. Let’s help bring better insights into early Parkinson’s detection through visual cues.

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


