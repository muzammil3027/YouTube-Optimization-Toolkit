document.getElementById('descriptionGeneratorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const keywords = document.getElementById('keywords').value;
    const container = document.getElementById('descriptionsContainer');
    const errorDiv = document.getElementById('descriptionError');
    const resultsDiv = document.getElementById('generatedDescriptions');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    try {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Generating...';
        errorDiv.style.display = 'none';
        
        const response = await fetch('/generate-descriptions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `keywords=${encodeURIComponent(keywords)}`
        });
        
        const data = await response.json();
        
        if (data.success) {
            container.innerHTML = data.descriptions.map(desc => `
                <div class="list-group-item">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <pre class="mb-0" style="white-space: pre-wrap">${desc}</pre>
                        <button onclick="copyDescription(\`${desc}\`)" class="btn btn-sm btn-outline-secondary ms-3">
                            <i class="bi bi-clipboard"></i>
                        </button>
                    </div>
                </div>
            `).join('');
            
            resultsDiv.style.display = 'block';
        } else {
            errorDiv.textContent = data.message;
            errorDiv.style.display = 'block';
        }
    } catch (error) {
        errorDiv.textContent = 'Failed to generate descriptions';
        errorDiv.style.display = 'block';
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Generate Descriptions';
    }
});

function copyDescription(desc) {
    navigator.clipboard.writeText(desc)
        .then(() => {
            const btn = event.target.closest('button');
            btn.innerHTML = '<i class="bi bi-check2"></i>';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i>';
            }, 1000);
        });
}

function copyAllDescriptions() {
    const descriptions = Array.from(document.querySelectorAll('pre'))
                            .map(pre => pre.textContent);
    
    navigator.clipboard.writeText(descriptions.join('\n\n'))
        .then(() => {
            const btn = document.querySelector('#copyAllBtn');
            btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy All';
            }, 2000);
        });
} 