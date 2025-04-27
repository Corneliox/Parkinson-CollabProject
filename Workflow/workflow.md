# 🧠 Parkinson Detection – Custom Workflow

This workflow is designed for building a YOLO-based Parkinson's Disease hand-drawing detection model.

## 🔰 Step 1: Prepare Your Dataset

### Collect Data
- Gather hand-drawn spiral and wave images.

### Label Your Data
- Use **LabelImg** for bounding boxes. ❎
- Use **Roboflow** for segmentation masks. ✅

### Organize into YOLO Format
```
/datasets/parkinson/
  ├── images/
  │   ├── train/
  │   └── val/
  ├── labels/
  │   ├── train/
  │   └── val/
  └── parkinson.yaml
```

## ⚙️ Step 2: Create Data Splits
- Prepare two dataset versions:
  - 80/20 split (train/validation)
  - 70/30 split (train/validation)
- Make both augmented and non-augmented variants.

## 🖼️ Step 3: Data Augmentation
Apply transformations:
- Random rotations
- Zooming
- Brightness/contrast shifts

> Keep augmentation consistent across models.

## 🧪 Step 4: Train YOLO Models

### Detection (YOLOv3 – YOLOv8)
```bash
yolo task=detect mode=train model=yolov8n.pt data=parkinson.yaml epochs=50 imgsz=640
```

### Segmentation (YOLOv9 – YOLOv11)
```bash
yolo task=segment mode=train model=yolov9n-seg.pt data=parkinson.yaml epochs=50 imgsz=640
```

> Repeat for each model and setting (augmented vs non-augmented).

## 📊 Step 5: Evaluate & Record Results
Evaluate each model based on:
- mAP@0.5
- Precision / Recall
- F1-score
- Loss
- IoU (for segmentation)

> Record results into an Excel summary table.

## 📁 Step 6: Export and Document
- Save best model weights.
- Document results:
  - Confusion matrices
  - PR curves
  - Summarize findings in project documentation.

## 🔎 Step 7: Analyze and Decide
Compare:
- Model versions (YOLOv3 - YOLOv11)
- Task types (Detection vs Segmentation)
- Augmented vs Non-augmented
- 80/20 vs 70/30 splits

> Decide the best model based on performance trade-offs.

## 📦 Optional Extras
- 🧪 Perform K-Fold cross-validation for best models.
- 🚀 Deploy best model into a web app (Streamlit, Gradio).
- 📈 Visualize and present predictions for stakeholders.
