import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Mapping of chapter number to (Section, Subsection)
mapping = {}
for i in range(1, 4):
    mapping[i] = ("INICIO", "CONCEPTOS FUNDAMENTALES")
for i in range(4, 17):
    mapping[i] = ("SECCIÓN 1 - CREENCIAS", "DOCTRINA")
for i in range(17, 27):
    mapping[i] = ("SECCIÓN 1 - CREENCIAS", "CONVICCIONES")
for i in range(27, 30):
    mapping[i] = ("SECCIÓN 2 - DISTINTIVOS", "ESTRUCTURA Y VISIÓN")
for i in range(30, 34):
    mapping[i] = ("SECCIÓN 3 - EL PACTO", "COMPROMISOS")

for filename in files:
    # Extract chapter number from filename (e.g., 'chapter_1.html' -> 1)
    match = re.search(r'chapter_(\d+)', filename)
    if not match:
        continue
    
    chap_num = int(match.group(1))
    if chap_num not in mapping:
        continue
    
    section, subsection = mapping[chap_num]
    path = os.path.join(directory, filename)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The script needs to find the current title and subtitle. 
    # Since titles vary per chapter, we use regex to find the h1 inside .chapter-container 
    # and the h3 following the <hr>.
    
    # 1. Replace the Section Title (h1)
    # Target: <h1 class="display-5 fw-bold chapter-title">...</h1>
    content = re.sub(r'<h1 class="display-5 fw-bold chapter-title">.*?</h1>', 
                    f'<h1 class="display-5 fw-bold chapter-title">{section}</h1>', content)
    
    # 2. Replace the Subsection Title (h3)
    # Target: <h3 class="fw-bold" style="color: var(--primary);">.*?</h3>
    content = re.sub(r'<h3 class="fw-bold" style="color: var(--primary);">.*?</h3>', 
                    f'<h3 class="fw-bold" style="color: var(--primary);"><i class="fa-solid fa-circle-info me-2" style="font-size: 0.8rem; opacity: 0.7;"></i>{subsection}</h3>', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}: {section} > {subsection}")

print("All chapters mapped to sections and subsections successfully.")
