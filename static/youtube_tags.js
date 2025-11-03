document.getElementById('tagsForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const url = document.getElementById('youtubeUrl').value;
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    const tagsList = document.getElementById('tagsList');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    try {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Loading...';
        errorDiv.style.display = 'none';
        
        const response = await fetch('/get-youtube-tags', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `url=${encodeURIComponent(url)}`
        });
        
        const data = await response.json();
        
        if (data.success) {
            tagsList.innerHTML = data.tags.length > 0 
                ? data.tags.map(tag => `<span class="badge bg-primary">${tag}</span>`).join('')
                : '<p>No tags available for this video</p>';
                
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
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Get Tags';
    }
});

function copyTags() {
    const tags = Array.from(document.querySelectorAll('#tagsList .badge'))
                     .map(badge => badge.innerText)
                     .join(', ');
    
    navigator.clipboard.writeText(tags)
        .then(() => {
            const btn = document.querySelector('#copyBtn');
            btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy All';
            }, 2000);
        })
        .catch(err => {
            console.error('Failed to copy:', err);
        });
} 