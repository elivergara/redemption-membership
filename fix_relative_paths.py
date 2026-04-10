import os

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

old_path = 'assets/logos/logo_facebook.png'
new_path = '../assets/logos/logo_facebook.png'

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = content.replace(old_path, new_path)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Fixed path in {filename}")

print("All relative paths fixed successfully.")
