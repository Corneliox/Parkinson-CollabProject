
# 🧠 Parkinson Detection via Hand-Drawn Spirals & Waves using YOLO

This project presents a comparative study of various **YOLO models (YOLOv3 to YOLOv12)** for early detection of **Parkinson’s disease** using **hand-drawn spirals and waves**. The models were evaluated on consistent datasets and split strategies, with the aim of identifying tremor-based patterns through object detection and segmentation approaches.

> 🔍 **Total Images Used**: 11,786 (Original & Augmented)  
> 🎯 **Best Model**: YOLOv11n – AP50: 96.52%, Precision: 94.31%, Recall: 94.90%  
> 🧪 **Total Models Compared**: 22 Variants (YOLOv3 – YOLOv12x)

---

## 📊 1. Experimental Setup

### 1.1 Model Variants Tested

- **Detection Only**: YOLOv3 to YOLOv8
- **Segmentation Supported**: YOLOv9 to YOLOv12
- **Model Sizes**: Nano, Small, Medium, Large, X-Large
- **Augmentation Levels**:
  - Raw only
  - Once augmented
  - Twice augmented
- **Data Splits Tested**:
  - 80:20 (Balanced)
  - 88:12
  - 94:6

---

### 1.2 Result Sections

#### 📈 1.2.1 Before Augmentation (Pure Data with 80:20 Split)
YOLOv9m outperformed other models with **AP50 = 87.84%**, while **YOLOv12x** had the lowest performance with **AP50 = 82.69%**.

#### 🌱 1.2.2 Once-Augmented (Unbalanced 88:12)
Augmentation improved performance slightly; **YOLOv8m** gained **AP50 = 85.51%** with improved stability.

#### 🌿 1.2.3 Twice-Augmented (Unbalanced 94:6)
**YOLOv8s** showed strong improvement, hitting **AP50 = 87.58%**, followed by YOLOv8m with **AP50 = 86.71%**.

#### 📊 1.2.4 Twice-Augmented + Balanced 80:20
Final training yielded top-tier results:
| Model    | AP50    | Precision | Recall | F1-Score Max |
|----------|---------|-----------|--------|--------------|
| YOLOv11n | **96.52%** | **94.31%** | **94.90%** | **97.99%** |
| YOLOv8n  | 96.52%  | 93.86%    | 94.36% | 97.68%      |
| YOLOv5s  | 96.46%  | 93.36%    | 94.50% | 97.19%      |

---

## 📦 2. Dataset Summary

Dataset composed by merging and unifying:
- **Kaggle - Parkinson's Drawings**
- **Mendeley Spiral Dataset**
- **Augmented Handwriting Dataset**
- **UNESP HandPD**

Final class breakdown:
- 🟢 **Healthy Spiral**
- 🟦 **Healthy Wave**
- 🔴 **Parkinson Spiral**
- 🟠 **Parkinson Wave**

---

## 🧠 3. Key Insights

- **YOLOv11n** consistently outperformed others in both precision and recall.
- Models like **YOLOv12x** were unstable despite deeper architecture.
- **Balanced augmentation** with 80:20 split yielded best generalization.
- Segmentation in YOLOv9–YOLOv11 allowed for more precise spatial understanding.

---

## 📈 4. Training Details

| Parameter     | Value        |
|---------------|--------------|
| Image Size    | 512x512 px   |
| Batch Size    | 8 / 16       |
| Epochs        | 50           |
| Framework     | Ultralytics  |
| Augmentations | Horizontal Flip, Brightness, Rotation, Noise |

---

## 🧪 6. Evaluation Metrics

| Metric     | Description                                              |
|------------|----------------------------------------------------------|
| AP50       | Average Precision @ IoU 0.5 (focus metric)               |
| mAP        | Average over 0.5:0.95 IoU thresholds                     |
| Precision  | True Positive / (True Positive + False Positive)         |
| Recall     | True Positive / (True Positive + False Negative)         |
| F1-Score   | Harmonic mean of precision and recall                    |

---

## 🚀 7. How to Run

Install requirements:
```bash
pip install ultralytics
```

Train a model:
```bash
yolo task=detect mode=train model=yolov8n.pt data=parkinson.yaml imgsz=512 epochs=50
```

Segment model:
```bash
yolo task=segment mode=train model=yolov10m-seg.pt data=parkinson.yaml imgsz=512 epochs=50
```

---

## 🔭 8. Future Work

- Improve the **stability of large models** like YOLOv10/12 with advanced schedulers
- Explore **transformer-based models** or **Vision-Language fusion**
- Introduce **multi-modal inputs**: pen pressure, speed, stroke sequence
- Real-time **smart device integration** for tremor tracking

---

## ✨ Contributing

We welcome contributions! Feel free to suggest architecture improvements or dataset cleaning ideas.
