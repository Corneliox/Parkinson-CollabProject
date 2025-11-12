import io
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from typing import List
from ultralytics import YOLO

# --- Model Loading ---
# Load your pre-trained .pt model
# This assumes it's a YOLOv8 classification or detection model
try:
    model = YOLO("your_model.pt") 
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Parkinson Detection API is running"}

@app.post("/detect/")
async def detect_images(files: List[UploadFile] = File(...)):
    if not model:
        return {"error": "Model not loaded"}, 500

    detection_results = []
    confidence_scores = []
    class_names = []

    # --- Inference on 5 Images ---
    for file in files:
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # --- Run Detection ---
        # Set confidence threshold to 0.90 as requested
        # Note: YOLO's `conf` is for *detection* boxes. For *classification*,
        # the top result is usually what you want, but we can still filter.
        # For a pure classification model, you'd check `results[0].probs.top1conf`.
        
        results = model(image, conf=0.90) 
        
        # Process result for this one image
        if len(results) > 0 and results[0].probs is not None:
            # This is for a Classification model
            top_prob = results[0].probs.top1conf.item() # Get top confidence
            top_class_idx = results[0].probs.top1    # Get top class index
            class_name = model.names[top_class_idx]  # Get class name
            
            # Since you set conf=0.90, we can use it as a filter
            if top_prob < 0.90:
                class_name = "Undetermined"
                top_prob = 0.0 # Or top_prob, if you want to show it anyway
        else:
            # Handle no detection or different model type
            class_name = "No Result"
            top_prob = 0.0

        detection_results.append({
            "class_name": class_name,
            "confidence": top_prob
        })
        confidence_scores.append(top_prob)
        class_names.append(class_name)

    # --- Calculate Average and Final Result ---
    
    # 1. Average Confidence
    avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0

    # 2. Final Result (Majority Vote)
    if class_names:
        final_class = max(set(class_names), key=class_names.count)
    else:
        final_class = "N/A"

    return {
        "individual_results": detection_results,
        "average_confidence": avg_confidence,
        "final_result": final_class
    }