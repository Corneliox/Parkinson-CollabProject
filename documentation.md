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

