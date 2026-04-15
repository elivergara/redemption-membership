import os
import shutil
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'

# 1. Save current chapter_23.html (Racismo) to a temporary file
# because we need to move the 'Gobierno' content out of it first, 
# but currently chapter_23.html IS the 'Racismo' content.
# Wait, based on the user's prompt and my read, chapter_23.html currently contains 'RACISMO'.
# The user said: "The first one is 'Racismo' and the second one is 'EL GOBIERNO DE LA IGLESIA'".
# This implies there is another source of content or a file that should be the 'Gobierno' one.
# Looking at the file list: chapter_23.html exists.
# I will assume the content currently in chapter_23.html is 'Racismo'.
# I need to find where 'EL GOBIERNO DE LA IGLESIA' is. 
# It's likely in the source document the user mentioned, but I don't have that document.
# HOWEVER, the user said "two 'chapter23' sections". 
# Let's check if there's a backup or if 'Gobierno' is actually in another file.

# Actually, looking at the current files:
# chapter_23.html -> RACISMO
# chapter_24.html -> (empty template/placeholder)
# If 'Gobierno' is missing, I can't move it. 
# But the user wants to SHIFT the rest.

# Let's perform the shifting first to make room.
# We shift from 33 down to 24.

files = [f for f in os.listdir(directory) if f.startswith('chapter_') and f.endswith('.html')]
# Sort files by number to avoid overwriting during rename
chapter_numbers = []
for f in files:
    match = re.search(r'chapter_(\d+)\.html', f)
    if match:
        chapter_numbers.append(int(match.group(1)))

chapter_numbers.sort(reverse=True) # Start from the highest

for num in chapter_numbers:
    if num >= 23:
        old_path = os.path.join(directory, f'chapter_{num}.html')
        new_path = os.path.join(directory, f'chapter_{num+1}.html')
        shutil.move(old_path, new_path)
        print(f"Moved chapter_{num}.html -> chapter_{num+1}.html")

print("Shifting complete.")
