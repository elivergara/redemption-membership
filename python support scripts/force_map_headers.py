import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

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
    
    # Fix 1: The H1 might be "Título del Capítulo" but without the class "chapter-title" in some files
    # We search for the h1 inside the chapter-container
    # We use a regex that looks for h1 and replaces its content regardless of the specific class
    content = re.sub(r'(<h1[^>]*class="[^"]*display-5[^"]*"[^>]*>).*?</h1>', 
                    fr'\1{section}</h1>', content)
    
    # Fix 2: The H3 might be "Subtítulo de Ejemplo" without the custom styles
    content = re.sub(r'(<h3[^>]*>).*?</h3>', 
                    fr'\1<i class="fa-solid fa-circle-info me-2" style="font-size: 0.8rem; opacity: 0.7;"></i>{subsection}</h3>', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Force updated {filename}: {section} > {subsection}")

print("All chapters force-updated with section headers successfully.")
