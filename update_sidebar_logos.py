import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# The specific replacement for the sidebar logo
old_logo = 'assets/logos/logo_main.png'
new_logo = 'assets/logos/Redemption Facebook.png'

for filename in files:
    path = os.path.join(directory, filename)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the logo source in the sidebar-brand link
    updated_content = content.replace(old_logo, new_logo)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated logo in {filename}")

print("All chapter files updated successfully.")
