// Get elements
const video = document.getElementById('video-feed');
const snapButton = document.getElementById('snap-button');
const resultsContainer = document.getElementById('results-container');
const finalResultDiv = document.getElementById('final-result');
const startCamButton = document.getElementById('start-cam-button');
const videoWrapper = document.getElementById('video-wrapper');

// --- NEW: Switch Camera Button ---
const switchCamButton = document.getElementById('switch-cam-button');

// --- NEW: Global variable to track camera state ---
let currentFacingMode = 'environment'; // Default to back camera
let currentStream; // To stop the old stream

// 1. Turn on the camera (NOW CALLED BY BUTTON)
async function startCamera() {
    try {
        // Stop any existing stream before starting a new one
        if (currentStream) {
            currentStream.getTracks().forEach(track => track.stop());
        }

        const constraints = {
            video: { 
                aspectRatio: 1.0, 
                facingMode: currentFacingMode 
            }
        };
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = stream;
        currentStream = stream; // Save stream to stop it later
        
        // --- On success, show camera and hide start button ---
        videoWrapper.style.display = 'flex';
        snapButton.style.display = 'block';
        switchCamButton.style.display = 'block'; // Show switch button
        startCamButton.style.display = 'none';

        // --- NEW: Handle video flip (mirroring) ---
        // Mirror the video if it's the front camera so it feels natural
        if (currentFacingMode === 'user') {
            video.style.transform = 'scaleX(-1)';
        } else {
            video.style.transform = 'scaleX(1)';
        }
        
    } catch (err) {
        console.error("Error accessing camera: ", err);
        alert("Could not access camera. Please grant permission in your browser settings.");
    }
}

// --- NEW: Function to switch camera ---
function switchCamera() {
    // Toggle the facing mode
    currentFacingMode = (currentFacingMode === 'environment') ? 'user' : 'environment';
    // Restart the camera with the new mode
    startCamera();
}

// --- Attach event listeners ---
startCamButton.addEventListener('click', startCamera);
switchCamButton.addEventListener('click', switchCamera); // Add listener for new button
snapButton.addEventListener('click', snapAndProcess);


async function snapAndProcess() {
    resultsContainer.innerHTML = "<h3>Processing 5 Photos...</h3>";
    finalResultDiv.innerHTML = "";
    
    const formData = new FormData();
    const capturedImages = [];

    // --- 3. Capture 5 Images ---
    for (let i = 0; i < 5; i++) {
        const canvas = document.createElement('canvas');
        
        canvas.width = video.videoWidth;
        canvas.height = video.videoWidth; // Use width for both
        
        const ctx = canvas.getContext('2d');
        
        const size = Math.min(video.videoWidth, video.videoHeight);
        const x = (video.videoWidth - size) / 2;
        const y = (video.videoHeight - size) / 2;

        // --- NEW: Conditionally flip the canvas for selfie cam ---
        // This ensures the saved image matches what the user sees
        if (currentFacingMode === 'user') {
            ctx.translate(canvas.width, 0);
            ctx.scale(-1, 1);
        }

        // Draw the image (it will be flipped if selfie cam, normal if back cam)
        ctx.drawImage(video, x, y, size, size, 0, 0, canvas.width, canvas.height);
        
        capturedImages.push(canvas.toDataURL('image/jpeg'));

        await new Promise(resolve => {
            canvas.toBlob(blob => {
                formData.append('files', blob, `snapshot_${i}.jpg`);
                resolve();
            }, 'image/jpeg');
        });
        
        await new Promise(resolve => setTimeout(resolve, 200));
    }

    // --- 4. Send to Backend ---
    try {
        const response = await fetch('/detect/', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        displayResults(data, capturedImages);

    } catch (err) {
        console.error("Error sending images: ", err);
        resultsContainer.innerHTML = "<h3>Error processing images.</h3>";
    }
}

function displayResults(data, images) {
    resultsContainer.innerHTML = "<h2>Individual Results:</h2>"; 
    
    data.individual_results.forEach((result, index) => {
        const img = document.createElement('img');
        img.src = images[index]; 

        const resultText = document.createElement('div');
        resultText.innerHTML = `
            <p><b>Result:</b> ${result.class_name}</p>
            <p><b>Confidence:</b> ${(result.confidence * 100).toFixed(2)}%</p>
        `;
        
        const itemDiv = document.createElement('div');
        itemDiv.className = 'result-item';
        itemDiv.appendChild(img);
        itemDiv.appendChild(resultText);
        resultsContainer.appendChild(itemDiv);
    });

    finalResultDiv.innerHTML = `
        <h3>Final Diagnosis (Majority Vote): ${data.final_result}</h3>
        <h3>Average Confidence Score: ${(data.average_confidence * 100).toFixed(2)}%</h3>
    `;
}