# 🧠 Parkinson's Detection Web App (YOLOv11n)

This repository contains the full project for a real-time, web-based application to detect Parkinson's disease from hand-drawn spirals and waves. The app is powered by a **YOLOv11n** model that was selected after a comprehensive research study comparing 22 different YOLO variants.

This project is divided into two main parts:

1. **The Web Application**: A real-time inference app that uses a phone/PC camera.

2. **The Model Research**: The complete academic study and data used to train the `best.pt` model.

## 🚀 The Web Application

This is a client-server application that allows a user to get a real-time diagnosis by drawing a spiral or wave in front of their camera.

### ✨ App Features

* **Real-time Camera Feed**: Connects directly to your phone or PC camera.

* **Secure Connection**: Uses `ngrok` to create an HTTPS tunnel, enabling camera access on mobile browsers.

* **1:1 Aspect Ratio**: The camera feed is formatted into a square to match the model's training.

* **5-Shot Capture**: Captures 5 images in rapid succession to ensure accuracy.

* **Backend Inference**: Sends images to a Python (FastAPI) server to run the YOLOv11n model.

* **Averaged Diagnosis**: Displays results for all 5 images and provides a final "Majority Vote" diagnosis and average confidence score.

### 💻 Technology Stack

* **Frontend**: HTML, CSS, JavaScript (using `navigator.mediaDevices`)

* **Backend**: Python, FastAPI, Uvicorn

* **Machine Learning**: PyTorch, Ultralytics (YOLO)

* **Deployment (Local)**: `ngrok` for secure HTTPS tunneling

### 📁 App File Structure

~~~
/Parkinson Unika/
├── 📄 main.py         (The FastAPI Backend API)
├── 📄 index.html      (The HTML frontend)
├── 📄 style.css       (The CSS for styling)
├── 📄 app.js          (The JavaScript for camera/snapping/API calls)
├── 📦 best.pt         (The final trained YOLOv11n model)
└── 📄 README.md       (This file)

~~~

### ⚙️ How to Run

1. **Clone the Repository**

   ~~~bash
   git clone [your-repo-url]
   cd [your-repo-folder]
   ~~~

2. **Set up Python Environment**
   It is recommended to use a virtual environment.

   ~~~bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Or using Conda (in Anaconda Prompt)
   conda create -n parkinson_app python=3.10
   conda activate parkinson_app
   ~~~

3. **Install Dependencies**

   ~~~bash
   pip install fastapi "uvicorn[standard]" python-multipart ultralytics
   ~~~

4. **Download the Model**
   Place your trained `best.pt` file in the main project folder.

5. **Run the Backend Server**
   In your first terminal, run the `uvicorn` server.

   ~~~bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ~~~

6. **Run `ngrok` for HTTPS**
   For your phone's camera to work, you **must** use a secure (HTTPS) connection.
   In a **second terminal**:

   ~~~bash
   ngrok http 8000
   ~~~

   `ngrok` will give you a public `https://` URL (e.g., `https://random-words.ngrok-free.app`).

7. **Open on Your Phone**
   Open the `https://` URL from the `ngrok` terminal on your phone's web browser. The app will load, and you can now grant it camera permissions.

## 🔬 Model Research & Training (Summary)

The `best.pt` model used in this application is the result of a comprehensive academic study comparing 22 different YOLO variants, based on the findings from "V3 - Final Paper".

### 📜 Abstract

Tremors are a prominent early indicator of Parkinson’s Disease (PD). This study explores using deep learning-based object detection to identify tremor patterns through hand-drawn spirals and waves. The goal is to classify drawings as either healthy or Parkinson-affected across four classes: **healthy spiral**, **healthy wave**, **Parkinson spiral**, and **Parkinson wave**.

A total of **3,723 original images** were collected, which were then augmented to a final dataset of **11,786 images**. The study tested 22 YOLO variants (from YOLOv3 to YOLOv12x) under various data splits and augmentation strategies.

### 🏆 Best Performing Model: YOLOv11n

After four experimental scenarios, the study concluded that a combination of **double augmentation** and a **balanced 80:20 data split** produced the most stable and accurate results.

**YOLOv11n** emerged as the best overall model, achieving the highest precision (**94.31%**) and an AP50 of **96.52%**.

#### Final Model Comparison (Augmented 2x, 80:20 Split)

| **Model** | **AP50** | **AP** | **Precision** | **Recall** | **F1-Score (min)** | **F1-Score (max)** | 
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| YOLOv5s | 0.9646 | 0.9645 | 0.9336 | 0.945 | 0.9007 | 0.9719 | 
| YOLOv8m | 0.9649 | 0.9647 | 0.9268 | 0.9312 | 0.9089 | 0.9502 | 
| YOLOv8n | 0.9652 | 0.9644 | 0.9386 | 0.9436 | 0.8991 | 0.9768 | 
| YOLOv9t | 0.9618 | 0.9618 | 0.9117 | 0.9093 | 0.8673 | 0.9393 | 
| YOLOv10m | 0.9647 | 0.9647 | 0.9329 | 0.9388 | 0.8964 | 0.973 | 
| YOLOv10n | 0.9645 | 0.9644 | 0.936 | 0.9304 | 0.8951 | 0.9771 | 
| **YOLO11n** | **0.9652** | **0.9646** | **0.9431** | **0.949** | **0.9108** | **0.9799** | 

### 🗃️ Dataset

The dataset was a combination of four public sources, as listed in `Source.txt`:

1. **[Kaggle - Parkinson's Drawings Dataset](https://www.kaggle.com/datasets/kmader/parkinsons-drawings)** (`archive.zip`)
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

2. **[Mendeley Data - Parkinson's Spiral Dataset](https://data.mendeley.com/datasets/fd5wd6wmdj/1)** (`Parkinson’s Disease Detection Using Spiral Images (Hand Drawings).zip`)
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

3. **[Kaggle - Handwritten Parkinson’s Disease (Augmented)](https://www.kaggle.com/datasets/banilkumar20phd7071/handwritten-parkinsons-disease-augmented-data)** (`dataset.zip`)
**Folder Structure**:
```
Dataset/
├── Healthy/
└── Parkinson/
```
---

4. **[HandPD - UNESP Handwritten Parkinson’s Dataset](https://wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/)**
**Folder Structure**:
```
HealthySpiral/
└── HealthySpiral/

PatientSpiral/
└── PatientSpiral/
```

---
All images were pre-processed (resized to **512x512 pixels** using **LANCZOS resampling**) and auto-labeled into four classes.

For Research Purpose, I've already put it all in one compact place on [Kaggle](https://www.kaggle.com/datasets/cornelioac/parkinson-yolo-dataset)

### 🏷️ Classes

* **0**: healthy spiral

* **1**: healthy wave

* **2**: parkinson spiral

* **3**: parkinson wave

## 📝 Project Diary (April-May 2025)

<details>
<summary>Click to expand the full data preparation and training log</summary>

### 📅 April 20-26, 2025

Focused on data mining and organizing datasets. Gathered approximately 3,500 data samples from the four sources.

### 📅 April 28, 2025

Began resizing all collected images to a uniform size of **512x512 pixels** using the **LANCZOS resampling method**. Started annotation process.

### 📅 April 29, 2025

* **8.28 A.M**: Successfully splitting data into 80/20 and 70/30 ratios.

* **5.55 P.M**: Decided to auto-annotate the Data based on the folder name (e.g., folder "Healthy" and "spiral" -> label "healthy spiral"). The annotation is a full bounding box for the entire image, effectively turning this into an image classification task using an object detector.

### 📅 April 30 - May 1, 2025

* **April 30**: Dataset moved and annotated automatically.

* **May 1, 10 AM**: Encountered problems merging datasets due to filename collisions.

* **May 1, 11.47 AM**: Solved filename collision by creating a Python preprocessing pipeline:

  ~~~python
  -> util_512Mod.py      # Resizing all image into 512
    -> util_rename.py    # Change name into one format to help labelling
      -> util_autolabeling.py # based on file Healthy/Wave = healthy_wave
        -> util_512toYolo.py # Change into Yolo Format File
          -> util_merge_to_4_class_yolo.py # merge into Train and Val Yolo Only
  ~~~

* **May 1, 12.00 PM**: Created `change_split_gui_selectable.py` to easily change train/val ratios.

### 📅 May 2, 2025

* **10.13 A.M**: Fixed `NotImplementedError` with `torchvision::nms` by reinstalling `torchvision` with CUDA support.

* **11.30 A.M**: First training attempt with `yolov8x`, `batch=16`. Realized this was too large for my **RTX 2050 4GB**.

* **15.30 PM**: `yolov8s` training finished. (AP50: 0.8599, Time: 122 Min).

* **23.52 P.M**: Started `yolov8m` training with `batch=12`, `epochs=50`.

### 📅 May 3, 2025

* **5.30 A.M**: `yolov8m` finished, but was overfitted. (Time: 4.385 Hours).

* **6.00 AM**: Decided on standard training parameters: `batch = 8`, `epoch = 50`.

* **8.55 A.M**: `yolov5m` finished. (AP50: 0.8365, Time: 2.219 hours).

* **12.13 P.M**: Noted that Ultralytics does not natively support YOLOv4, v6, or v7. Decided to skip them and focus on v3, v5, v8, v9, v10, v11, v12.

### 📅 May 4 - 5, 2025

* Finished training all models locally (RTX 2050) and on Kaggle (TPU4). Total training time: **35.35 hours**.

* Learned that any model using >4GB VRAM must be run on Kaggle.

### 📅 May 6 - 20, 2025

* **May 10**: Augmented data, resulting in ~6,000 images.

* **May 11**: Augmented data again to **11,786 images total**.

* **May 18**: Re-split the final 11k dataset into a balanced 80/20 format.

  * **Train**: 9,431 images

  * **Val**: 2,355 images

* Began the final training runs on the mini models (v5s, v8n, v9t, v10n, v11n) with this new, balanced dataset.

* **May 21**: Finalized preprocessing pipeline and manual label review.

</details>

## 🔭 Future Work

Based on the research paper, future work could include:

* **Build a Multi-Modal Dataset**: Incorporate clinical metadata like patient age, gender, and disease stage, as well as temporal data like stroke speed and pen pressure.

* **Integrate Attention Mechanisms**: Explore modules like CBAM or SOCR to help the model focus on fine-grained tremor features.

* **Clinical Application**: Build an interactive, clinical-grade application for medical professionals to use.

## 📚 References

* V3 - Final Paper.docx

* Yüzgeç Özdemir, E., & Özyurt, F. (2025). Elasticnet-Based Vision Transformers for early detection of Parkinson’s disease.

* Terven, J., & Córdova-Esparza, D. M., & Romero-González, J. A. (2023). A Comprehensive Review of YOLO Architectures...

* ... (and other references from the paper)
