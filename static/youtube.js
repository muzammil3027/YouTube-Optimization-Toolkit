document.getElementById('youtubeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const url = document.getElementById('youtubeUrl').value;
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    
    try {
        const response = await fetch('/get-youtube-thumbnail', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `url=${encodeURIComponent(url)}`
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('thumbnail').src = data.thumbnail;
            document.getElementById('downloadBtn').href = `/download/youtube/${data.video_id}`;
            resultDiv.style.display = 'block';
            errorDiv.style.display = 'none';
        } else {
            errorDiv.textContent = data.message;
            errorDiv.style.display = 'block';
            resultDiv.style.display = 'none';
        }
    } catch (error) {
        errorDiv.textContent = 'An error occurred. Please try again.';
        errorDiv.style.display = 'block';
        resultDiv.style.display = 'none';
    }
}); 