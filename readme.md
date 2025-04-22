
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

#Instruction

---

### 📁 Dataset Details
#Details

---

### 🧹 Preprocessing
#Preprocess Brief

---

### 🧠 Models Used

#Model Brief

#Split Model 

#Train Setup

### ⚙️ Training Command Examples

#Bash Detection (YOLOv5 - YOLOv8)


#Bash Segmentation (YOLOv9 - YOLOv11)

---

### 📊 Evaluation Metrics
#Detection

#Segmentation

---

### 📈 Output
 #Output Session

---

#Contribution Session
