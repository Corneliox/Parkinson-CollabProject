
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
- **Labels**: Binary (Parkinson / Non-Parkinson)
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
- All images resized to **640x640**

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
imgsz=640
epochs=50
batch=16
```

---

### ⚙️ Training Command Examples

#### 🔹 Detection (YOLOv5 - YOLOv8)
```bash
yolo task=detect mode=train model=yolov8n.pt data=parkinson.yaml epochs=50 imgsz=640
```

#### 🔹 Segmentation (YOLOv9 - YOLOv11)
```bash
yolo task=segment mode=train model=yolov9n-seg.pt data=parkinson.yaml epochs=50 imgsz=640
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
