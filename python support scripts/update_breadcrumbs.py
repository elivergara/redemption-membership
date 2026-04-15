import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Current breadcrumb HTML
old_breadcrumb = r'<nav aria-label="breadcrumb">\s*<ol class="breadcrumb">\s*<li class="breadcrumb-item"><a href="../index.html">Inicio</a></li>\s*<li class="breadcrumb-item active" aria-current="page">Capítulo</li>\s*</ol>\s*</nav>'

# New breadcrumb using Bootstrap buttons
# We use btn-sm for a subtle look and btn-outline-light because it's on a dark background
new_breadcrumb = """
        <div class="d-flex align-items-center mb-4">
            <a href="../index.html" class="btn btn-sm btn-outline-light px-3 py-1 rounded-pill shadow-sm">
                <i class="fa-solid fa-house me-2"></i> Inicio
            </a>
            <span class="mx-2 text-white-50">/</span>
            <span class="text-white-50 fw-medium">Capítulo Actual</span>
        </div>
"""

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the breadcrumb nav with the new button-based version
    updated_content = re.sub(old_breadcrumb, new_breadcrumb, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated breadcrumbs in {filename}")

print("All chapter breadcrumbs converted to buttons successfully.")
