import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Target the new breadcrumb structure and keep only the Inicio button
# Old: <div class="d-flex align-items-center mb-4">...</div>
# New: Only the button, removing the / Capítulo Actual part

pattern_breadcrumb = r'<div class="d-flex align-items-center mb-4">.*?<a href="\.\./index\.html" class="btn btn-sm btn-outline-light px-3 py-1 rounded-pill shadow-sm">.*?</a>.*?</div>'

replacement = r'''        <div class="d-flex align-items-center mb-4">
            <a href="../index.html" class="btn btn-sm btn-outline-light px-3 py-1 rounded-pill shadow-sm">
                <i class="fa-solid fa-house me-2"></i> Inicio
            </a>
        </div>'''

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = re.sub(pattern_breadcrumb, replacement, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Cleaned breadcrumbs in {filename}")

print("All chapter breadcrumbs cleaned successfully.")
