import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.startswith('chapter_') and f.endswith('.html')]

reading_progress_html = '''
<div class="reading-progress">
  <div class="reading-progress-bar" id="readingProgressBar"></div>
</div>
'''

reading_progress_script = '''
<script>
  window.addEventListener('scroll', () => {
    const progressBar = document.getElementById('readingProgressBar');
    if (!progressBar) return;

    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;

    const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;

    progressBar.style.width = `${scrollPercent}%`;
  });
</script>
'''

for filename in files:
    path = os.path.join(directory, filename)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add reading progress div after the main-content-wrapper div opens (after container)
    # Find the position after the chapter-container div starts
    pattern_container = r'(<div class="chapter-container p-5 rounded-4 shadow-lg">)'
    replacement_container = r'\1\n' + reading_progress_html
    
    updated_content = re.sub(pattern_container, replacement_container, content, count=1, flags=re.DOTALL)
    
    # Add script before </body>
    pattern_body_end = r'(<\/body>)'
    replacement_body = reading_progress_script + r'\1'
    
    final_content = re.sub(pattern_body_end, replacement_body, updated_content, count=1)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Updated {filename}")

print(f"\nAll chapters processed successfully.")
print(f"Total chapters updated: {len(files)}")
