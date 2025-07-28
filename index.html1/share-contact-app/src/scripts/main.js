// This file contains the JavaScript code for the application. It handles the functionality for video recording, managing user interactions, and integrating with the service worker for offline capabilities.

const videoPreview = document.getElementById('videoPreview');
const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const messageBox = document.getElementById('messageBox');
const videoLinkInput = document.getElementById('videoLink');
const phoneNumberInput = document.getElementById('phoneNumber');
const emailAddressInput = document.getElementById('emailAddress');
const sendButton = document.getElementById('sendButton');

let mediaRecorder;
let recordedChunks = [];

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoPreview.srcObject = stream;
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
            recordedChunks.push(event.data);
        }
    };

    mediaRecorder.onstop = () => {
        const blob = new Blob(recordedChunks, { type: 'video/webm' });
        const url = URL.createObjectURL(blob);
        videoPreview.srcObject = null;
        videoPreview.src = url;
        recordedChunks = [];
    };

    mediaRecorder.start();
    recordButton.classList.add('hidden');
    stopButton.classList.remove('hidden');
}

function stopRecording() {
    mediaRecorder.stop();
    recordButton.classList.remove('hidden');
    stopButton.classList.add('hidden');
}

recordButton.addEventListener('click', startRecording);
stopButton.addEventListener('click', stopRecording);

sendButton.addEventListener('click', () => {
    const videoLink = videoLinkInput.value;
    const phoneNumber = phoneNumberInput.value;
    const emailAddress = emailAddressInput.value;

    if (!videoLink || !phoneNumber || !emailAddress) {
        showMessage('Please fill in all fields.', 'error');
        return;
    }

    // Here you would typically send the data to a server or handle it as needed
    showMessage('Contact information shared successfully!', 'success');
});

function showMessage(message, type) {
    messageBox.textContent = message;
    messageBox.className = `message-box ${type}`;
    messageBox.classList.remove('hidden');

    setTimeout(() => {
        messageBox.classList.add('fade-out');
        setTimeout(() => {
            messageBox.classList.add('hidden');
            messageBox.classList.remove('fade-out');
        }, 500);
    }, 3000);
}