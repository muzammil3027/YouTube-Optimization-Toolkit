document.getElementById('titleGeneratorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const keywords = document.getElementById('keywords').value;
    const container = document.getElementById('titlesContainer');
    const errorDiv = document.getElementById('titleError');
    const resultsDiv = document.getElementById('generatedTitles');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    try {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Generating...';
        errorDiv.style.display = 'none';
        
        const response = await fetch('/generate-titles', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `keywords=${encodeURIComponent(keywords)}`
        });
        
        const data = await response.json();
        
        if (data.success) {
            container.innerHTML = data.titles.map(title => `
                <div class="list-group-item d-flex justify-content-between align-items-center">
                    ${title}
                    <button onclick="copyTitle('${title}')" class="btn btn-sm btn-outline-secondary">
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
        errorDiv.textContent = 'Failed to generate titles';
        errorDiv.style.display = 'block';
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Generate Titles';
    }
});

function copyTitle(title) {
    navigator.clipboard.writeText(title)
        .then(() => {
            const btn = event.target.closest('button');
            btn.innerHTML = '<i class="bi bi-check2"></i>';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i>';
            }, 1000);
        });
}

function copyAllTitles() {
    const titles = Array.from(document.querySelectorAll('.list-group-item'))
                      .map(item => item.textContent.trim().replace('Copy', ''));
    
    navigator.clipboard.writeText(titles.join('\n'))
        .then(() => {
            const btn = document.querySelector('#copyAllBtn');
            btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
            setTimeout(() => {
                btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy All';
            }, 2000);
        });
} 