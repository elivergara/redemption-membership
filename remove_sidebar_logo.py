import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# The pattern targets the sidebar brand link which is the "little navbar" inside the sidebar
pattern_sidebar_brand = r'<a href="\.\./index\.html" class="sidebar-brand d-flex align-items-center">.*?</a>'

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the sidebar brand link entirely
    updated_content = re.sub(pattern_sidebar_brand, '', content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Removed sidebar brand from {filename}")

print("All sidebar brand logos removed successfully.")
