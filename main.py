import io
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from typing import List
from ultralytics import YOLO
from fastapi.responses import FileResponse  # <-- Import this
from fastapi.staticfiles import StaticFiles  # <-- Import this

# --- Model Loading ---
# Assuming 'yolo11n' is your model file, e.g., 'yolov8n-cls.pt'
# Place your 'your_model.pt' file in the same directory
try:
    model = YOLO("best.pt") 
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = FastAPI()

# --- API Endpoint (No Change) ---
@app.post("/detect/")
async def detect_images(files: List[UploadFile] = File(...)):
    # (The detection logic from the previous answer goes here)
    # (This code block is unchanged)
    if not model:
        return {"error": "Model not loaded"}, 500

    detection_results = []
    confidence_scores = []
    class_names = []

    for file in files:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # --- Run Detection ---
        # NOTE: This logic assumes a CLASSIFICATION model.
        # See the section below if you are using a DETECTION model.
        results = model(image, conf=0.90) 
        
        if len(results) > 0 and results[0].probs is not None:
            top_prob = results[0].probs.top1conf.item()
            top_class_idx = results[0].probs.top1
            class_name = model.names[top_class_idx]
            
            if top_prob < 0.90:
                class_name = "Undetermined"
                top_prob = 0.0
        else:
            class_name = "No Result"
            top_prob = 0.0

        detection_results.append({
            "class_name": class_name,
            "confidence": top_prob
        })
        confidence_scores.append(top_prob)
        class_names.append(class_name)

    avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
    final_class = max(set(class_names), key=class_names.count) if class_names else "N/A"

    return {
        "individual_results": detection_results,
        "average_confidence": avg_confidence,
        "final_result": final_class
    }

# --- Serve Frontend Files (NEW) ---
# This part serves your 'index.html' and 'app.js' files

# Mount the 'app.js' file
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def read_root():
    # Serve the 'index.html' file
    return FileResponse('index.html')