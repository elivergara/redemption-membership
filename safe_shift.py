import os
import shutil

directory = '/home/elivergara/Documents/redemption-membership/pages'

# Shift from 33 down to 23
for num in range(33, 22, -1):
    old_path = os.path.join(directory, f'chapter_{num}.html')
    new_path = os.path.join(directory, f'chapter_{num+1}.html')
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Moved chapter_{num}.html -> chapter_{num+1}.html")

print("File shifting complete.")
