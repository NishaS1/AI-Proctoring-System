const video = document.getElementById('webcam');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const statusDiv = document.getElementById('status');
const scoreDiv = document.getElementById('score');

// Start webcam
navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => video.srcObject = stream);

document.getElementById('start').addEventListener('click', () => {
    setInterval(async () => {
        // Capture frame
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0);
        const image = canvas.toDataURL('image/jpeg');

        // Send to backend
        const res = await fetch('http://localhost:5000/analyze-frame', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image })
        });
        const data = await res.json();
        statusDiv.innerText = data.face_ok ? '✅ Face OK' : '❌ Suspicious';
        scoreDiv.innerText = `Suspicious Score: ${data.score}`;
        if (data.score > 15) {
            statusDiv.innerText = '⚠️ Flagged!';
        }
    }, 2000); // every 2 seconds
});