// Get elements
const video = document.getElementById('video-feed');
const snapButton = document.getElementById('snap-button');
const resultsContainer = document.getElementById('results-container');
const finalResultDiv = document.getElementById('final-result');

// 1. Turn on the camera
async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ 
            video: { facingMode: 'user' } // Use 'environment' for back camera
        });
        video.srcObject = stream;
    } catch (err) {
        console.error("Error accessing camera: ", err);
    }
}

// (Add this to the 'app.js' file from earlier)

snapButton.addEventListener('click', snapAndProcess);

async function snapAndProcess() {
    resultsContainer.innerHTML = "Processing...";
    finalResultDiv.innerHTML = "";
    
    const formData = new FormData();
    const capturedImages = []; // To store images for display

    // --- 3. Capture 5 Images ---
    for (let i = 0; i < 5; i++) {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        
        // Draw the current video frame to the canvas
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Store the image data URL for display
        capturedImages.push(canvas.toDataURL('image/jpeg'));

        // Convert canvas to a 'Blob' to send to the server
        await new Promise(resolve => {
            canvas.toBlob(blob => {
                formData.append('files', blob, `snapshot_${i}.jpg`);
                resolve();
            }, 'image/jpeg');
        });
        
        // Wait a tiny bit for a new frame (e.g., 200ms)
        await new Promise(resolve => setTimeout(resolve, 200));
    }

    // --- 4. Send to Backend ---
    try {
        const response = await fetch('/detect/', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        // --- 5. Display Results ---
        displayResults(data, capturedImages);

    } catch (err) {
        console.error("Error sending images: ", err);
        resultsContainer.innerHTML = "Error processing images.";
    }
}

function displayResults(data, images) {
    resultsContainer.innerHTML = ""; // Clear "Processing..."
    
    // 1. Display 5 Photos + Individual Results
    data.individual_results.forEach((result, index) => {
        const img = document.createElement('img');
        img.src = images[index]; // Use the captured image

        const resultText = document.createElement('p');
        resultText.innerHTML = `
            <b>Result:</b> ${result.class_name} <br>
            <b>Confidence:</b> ${(result.confidence * 100).toFixed(2)}%
        `;
        
        const itemDiv = document.createElement('div');
        itemDiv.className = 'result-item';
        itemDiv.appendChild(img);
        itemDiv.appendChild(resultText);
        resultsContainer.appendChild(itemDiv);
    });

    // 2. Display Final Average Result
    finalResultDiv.innerHTML = `
        <hr>
        <h3>Final Diagnosis (Majority Vote): ${data.final_result}</h3>
        <h3>Average Confidence Score: ${(data.average_confidence * 100).toFixed(2)}%</h3>
    `;
}

startCamera();