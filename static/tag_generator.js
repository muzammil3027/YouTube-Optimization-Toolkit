document.getElementById('tagGeneratorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const keywords = document.getElementById('keywords').value;
    const tagsContainer = document.getElementById('tagsContainer');
    const errorDiv = document.getElementById('tagError');
    const resultsDiv = document.getElementById('generatedTags');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    try {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Generating...';
        errorDiv.style.display = 'none';
        
        const response = await fetch('/generate-tags', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `keywords=${encodeURIComponent(keywords)}`
        });
        
        const data = await response.json();
        
        if (data.success) {
            tagsContainer.innerHTML = data.tags.map(tag => `
                <div class="tag-item badge bg-primary d-flex align-items-center gap-2">
                    ${tag}
                    <button onclick="copyTag('${tag}')" class="btn btn-sm btn-light p-0 px-1">
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
        errorDiv.textContent = 'Failed to generate tags';
        errorDiv.style.display = 'block';
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Generate Tags';
    }
});

function copyTag(tag) {
    navigator.clipboard.writeText(tag)
        .then(() => {
            const btn = event.target.closest('button');
            btn.innerHTML = '<i class="bi bi-check2"></i>';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i>';
            }, 1000);
        });
}

function copyAllTags() {
    const tags = Array.from(document.querySelectorAll('.tag-item'))
                     .map(item => item.textContent.trim().replace('Copy', ''));
    
    navigator.clipboard.writeText(tags.join(', '))
        .then(() => {
            const btn = document.querySelector('#copyAllBtn');
            btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy All';
            }, 2000);
        });
} 