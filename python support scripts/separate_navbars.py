import os

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change navbar class specifically for chapter pages
    updated_content = content.replace('<nav class="navbar navbar-expand-lg navbar-dark shadow-sm">', 
                                     '<nav class="navbar-chapter navbar-expand-lg navbar-dark shadow-sm">')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated navbar class in {filename}")

print("Navbar classes separated successfully.")
