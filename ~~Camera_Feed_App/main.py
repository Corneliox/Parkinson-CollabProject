import io
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from typing import List
from ultralytics import YOLO
from fastapi.responses import FileResponse

# --- Model Loading (No Change) ---
try:
    model = YOLO("best.pt")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = FastAPI()

# --- API Endpoint (UPDATED) ---
@app.post("/detect/")
async def detect_images(files: List[UploadFile] = File(...)):
    if not model:
        return {"error": "Model not loaded"}, 500

    detection_results = []
    confidence_scores = []
    class_names = []

    for file in files:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # --- Run Detection ---
        # We don't set conf=0.90 here, we filter manually
        results = model(image) 
        
        # --- NEW DETECTION LOGIC ---
        best_confidence = 0.0
        best_class_name = "No Result" # Default if nothing is found

        # Check if any boxes were detected
        if len(results[0].boxes) > 0:
            # Find the box with the highest confidence score
            for box in results[0].boxes:
                conf = box.conf.item() # Get confidence (e.g., 0.95)
                
                if conf > best_confidence:
                    best_confidence = conf
                    class_idx = int(box.cls.item()) # Get class index (e.g., 0, 1)
                    best_class_name = model.names[class_idx] # Get name (e.g., 'Parkinson')

        # --- NOW we check your 0.90 threshold ---
        if best_confidence < 0.60:
            best_class_name = "Undetermined"
            # Keep best_confidence to show the score, or set to 0.0
            # best_confidence = 0.0 
        
        detection_results.append({
            "class_name": best_class_name,
            "confidence": best_confidence
        })
        confidence_scores.append(best_confidence)
        class_names.append(best_class_name)

    # --- Averaging Logic (No Change) ---
    avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
    final_class = max(set(class_names), key=class_names.count) if class_names else "N/A"

    return {
        "individual_results": detection_results,
        "average_confidence": avg_confidence,
        "final_result": final_class
    }

# --- Serve Frontend Files (No Change) ---
@app.get("/")
def read_root():
    return FileResponse('index.html')

@app.get("/app.js")
def read_app_js():
    return FileResponse('app.js')

@app.get("/style.css")
def read_style_css():
    return FileResponse('style.css')