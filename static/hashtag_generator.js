document.getElementById('hashtagGeneratorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const keywords = document.getElementById('keywords').value;
    const container = document.getElementById('hashtagsContainer');
    const errorDiv = document.getElementById('hashtagError');
    const resultsDiv = document.getElementById('generatedHashtags');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    try {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Generating...';
        errorDiv.style.display = 'none';
        
        const response = await fetch('/generate-hashtags', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `keywords=${encodeURIComponent(keywords)}`
        });
        
        const data = await response.json();
        
        if (data.success) {
            container.innerHTML = data.hashtags.map(hashtag => `
                <div class="hashtag-item badge bg-info d-flex align-items-center gap-2">
                    ${hashtag}
                    <button onclick="copyHashtag('${hashtag}')" class="btn btn-sm btn-light p-0 px-1">
                        <i class="bi bi-clipboard"></i>
                    </button>
                </div>
            `).join('');
            
            resultsDiv.style.display = 'block';
        } else {
            errorDiv.textContent = data.message;
            errorDiv.style.display = 'block';
        }
    } catch (error) {
        errorDiv.textContent = 'Failed to generate hashtags';
        errorDiv.style.display = 'block';
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Generate Hashtags';
    }
});

function copyHashtag(hashtag) {
    navigator.clipboard.writeText(hashtag)
        .then(() => {
            const btn = event.target.closest('button');
            btn.innerHTML = '<i class="bi bi-check2"></i>';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i>';
            }, 1000);
        });
}

function copyAllHashtags() {
    const hashtags = Array.from(document.querySelectorAll('.hashtag-item'))
                        .map(item => item.textContent.trim().replace('Copy', ''));
    
    navigator.clipboard.writeText(hashtags.join(' '))
        .then(() => {
            const btn = document.querySelector('#copyAllBtn');
            btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy All';
            }, 2000);
        });
} 