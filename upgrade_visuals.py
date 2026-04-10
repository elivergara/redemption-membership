import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We need to replace the old structure with the new refined one.
# Because the content varies, we target the specific container and title sections.

# 1. Replace the container and title
# Old: <div class="chapter-container bg-white p-5 rounded-4 shadow-sm">
#       <h1 class="display-5 fw-bold mb-4" style="color: var(--primary);">Título del Capítulo</h1>
# New: <div class="chapter-container bg-white p-5 rounded-4 shadow-lg">
#       <h1 class="display-5 fw-bold chapter-title">Título del Capítulo</h1>

# Since the titles vary, we use a regex that captures the title text.
pattern_container_title = r'<div class="chapter-container bg-white p-5 rounded-4 shadow-sm">\s*<h1 class="display-5 fw-bold mb-4" style="color: var(--primary);">(.*?)</h1>'
replacement_container_title = r'<div class="chapter-container bg-white p-5 rounded-4 shadow-lg">\n            <h1 class="display-5 fw-bold chapter-title">\1</h1>'

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = re.sub(pattern_container_title, replacement_container_title, content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated style in {filename}")

print("All chapters visually updated successfully.")
