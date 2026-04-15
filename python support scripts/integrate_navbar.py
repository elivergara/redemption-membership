import os
import re

# Read the navbar from index.html
with open('/home/elivergara/Documents/redemption-membership/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the navbar HTML block
navbar_match = re.search(r'<nav class="navbar navbar-expand-lg navbar-dark shadow-sm">.*?</nav>', index_content, re.DOTALL)
if not navbar_match:
    print("Could not find navbar in index.html")
    exit(1)

navbar_html = navbar_match.group(0)

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert navbar immediately after <body> tag
    updated_content = content.replace('<body>', f'<body>\n    {navbar_html}')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Added navbar to {filename}")

print("Navbar successfully integrated into all chapters.")
