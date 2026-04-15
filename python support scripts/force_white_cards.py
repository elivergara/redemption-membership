import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We need to ensure the container has the correct classes and the background is handled by CSS
pattern_container = r'<div class="chapter-container bg-white p-5 rounded-4 shadow-lg">'
replacement_container = r'<div class="chapter-container p-5 rounded-4 shadow-lg">'

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = content.replace('bg-white', '') # Remove bg-white to let CSS handle it with !important
    updated_content = re.sub(pattern_container, replacement_container, updated_content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Fixed container in {filename}")

print("All chapters visually forced to white cards.")
