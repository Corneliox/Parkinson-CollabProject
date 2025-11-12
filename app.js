// Get elements
const video = document.getElementById('video-feed');
const snapButton = document.getElementById('snap-button');
const resultsContainer = document.getElementById('results-container');
const finalResultDiv = document.getElementById('final-result');

// --- NEW Elements ---
const startCamButton = document.getElementById('start-cam-button');
const videoWrapper = document.getElementById('video-wrapper');


// 1. Turn on the camera (NOW CALLED BY BUTTON)
async function startCamera() {
    try {
        // --- UPDATED to request 1:1 aspect ratio ---
        const constraints = {
            video: { 
                aspectRatio: 1.0, 
                facingMode: 'user' 
            }
        };
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = stream;
        
        // --- On success, show camera and hide start button ---
        videoWrapper.style.display = 'flex';
        snapButton.style.display = 'block';
        startCamButton.style.display = 'none';
        
    } catch (err) {
        console.error("Error accessing camera: ", err);
        alert("Could not access camera. Please grant permission in your browser settings.");
    }
}

// --- NEW: Attach camera logic to the button ---
startCamButton.addEventListener('click', startCamera);

// (The rest of the file is the same)

// --- Event Listener ---
snapButton.addEventListener('click', snapAndProcess);

async function snapAndProcess() {
    resultsContainer.innerHTML = "<h3>Processing 5 Photos...</h3>";
    finalResultDiv.innerHTML = "";
    
    const formData = new FormData();
    const capturedImages = [];

    // --- 3. Capture 5 Images ---
    for (let i = 0; i < 5; i++) {
        const canvas = document.createElement('canvas');
        
        // --- Make canvas square to match video ---
        canvas.width = video.videoWidth;
        canvas.height = video.videoWidth; // Use width for both
        
        const ctx = canvas.getContext('2d');
        
        // --- Center the 1:1 video feed onto the 1:1 canvas ---
        // (This logic handles if the feed isn't perfectly square)
        const size = Math.min(video.videoWidth, video.videoHeight);
        const x = (video.videoWidth - size) / 2;
        const y = (video.videoHeight - size) / 2;

        // Draw and flip
        ctx.translate(canvas.width, 0);
        ctx.scale(-1, 1);
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