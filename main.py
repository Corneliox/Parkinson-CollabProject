import io
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from typing import List
from ultralytics import YOLO
from fastapi.responses import FileResponse  # <-- Import this

# --- Model Loading ---
try:
    model = YOLO("best.pt") # <-- Changed to 'best.pt'
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = FastAPI()

# --- API Endpoint (No Change) ---
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

# --- Serve Frontend Files (UPDATED) ---

@app.get("/")
def read_root():
    return FileResponse('index.html')

@app.get("/app.js") # <-- This is the fix for the 404
def read_app_js():
    return FileResponse('app.js')

@app.get("/style.css") # <-- This serves your new style
def read_style_css():
    return FileResponse('style.css')