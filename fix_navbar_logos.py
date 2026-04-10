import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We need to change the logo path in the navbar we just injected
# The navbar came from index.html, so it has "assets/logos/R.jpeg"
# In /pages/, it must be "../assets/logos/R.jpeg"
old_path = 'assets/logos/R.jpeg'
new_path = '../assets/logos/R.jpeg'

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only replace the one in the navbar context to be safe
    updated_content = content.replace(old_path, new_path)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Fixed navbar logo path in {filename}")

print("All navbar logo paths fixed successfully.")
