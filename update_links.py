import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.startswith('chapter_') and f.endswith('.html')]

# Use a raw string or a different way to handle the curly braces in JS
# We'll use a simple string replace for {id} instead of .format() to avoid brace conflicts
js_template = """
    <script>
        const CHAPTER_ID = "ID_PLACEHOLDER"; 

        // Update Sidebar Active State
        document.querySelectorAll('.nav-chapter-link').forEach(link => {
            if(link.getAttribute('data-id') === CHAPTER_ID) {
                link.classList.add('active');
            }
        });

        // Dynamic Navigation Logic
        function setupNavigation() {
            const prevBtn = document.querySelector('.btn-outline-secondary');
            const nextBtn = document.querySelector('.btn-membership:not(#completeBtn)');
            
            const currentId = parseInt(CHAPTER_ID);
            
            if (currentId > 1) {
                prevBtn.href = `chapter_${currentId - 1}.html`;
            } else {
                prevBtn.style.display = 'none';
            }
            
            if (currentId < 33) {
                nextBtn.href = `chapter_${currentId + 1}.html`;
            } else {
                nextBtn.style.display = 'none';
            }
        }

        // Progress Tracking Logic
        function updateStatus() {
            const completed = JSON.parse(localStorage.getItem('membership_progress') || '[]');
            document.querySelectorAll('.nav-chapter-link').forEach(link => {
                const id = link.getAttribute('data-id');
                const statusEl = document.getElementById('status-' + id);
                if (statusEl && completed.includes(id)) {
                    statusEl.innerHTML = '✓';
                    statusEl.classList.add('completed');
                }
            });
        }

        document.getElementById('completeBtn').addEventListener('click', function() {
            let completed = JSON.parse(localStorage.getItem('membership_progress') || '[]');
            if (!completed.includes(CHAPTER_ID)) {
                completed.push(CHAPTER_ID);
                localStorage.setItem('membership_progress', JSON.stringify(completed));
                this.innerHTML = '<i class="fa-solid fa-check-double me-2"></i> ¡Completado!';
                this.classList.replace('btn-membership', 'btn-success');
            }
            updateStatus();
        });

        window.onload = () => {
            setupNavigation();
            updateStatus();
        };
    </script>
"""

for filename in files:
    match = re.search(r'chapter_(\d+)\.html', filename)
    if match:
        chapter_id = match.group(1)
        path = os.path.join(directory, filename)
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_js = js_template.replace("ID_PLACEHOLDER", chapter_id)
        updated_content = re.sub(r'<script>.*?</script>', new_js, content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated {filename}")

print("All chapters processed successfully.")
