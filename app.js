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

startCamera();