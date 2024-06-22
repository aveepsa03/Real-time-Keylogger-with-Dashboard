document.addEventListener("DOMContentLoaded", function () {
    function fetchScreenshots() {
        fetch('/get_screenshots')
            .then(response => response.json())
            .then(data => {
                const screenshotsContainer = document.getElementById('screenshots-container');
                screenshotsContainer.innerHTML = ''; // Clear existing screenshots
                data.forEach(screenshot => {
                    const img = document.createElement('img');
                    img.src = `/screenshots/${screenshot}`;
                    img.alt = screenshot;
                    img.style.maxWidth = '100%';
                    img.style.height = 'auto';
                    img.style.marginBottom = '10px';
                    screenshotsContainer.appendChild(img);
                });
            })
            .catch(error => console.error('Error fetching screenshots:', error));
    }

    // Fetch screenshots every 5 seconds
    setInterval(fetchScreenshots, 5000);

    // Initial fetch
    fetchScreenshots();
});