import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.startswith('chapter_') and f.endswith('.html')]

# Correct sidebar HTML for the first few chapters
sidebar_start = r'''
    <!-- Sidebar Navigation -->
    <div class="sidebar" id="mainSidebar">
        
        <div class="nav-section-title">Inicio</div>
        <a href="chapter_1.html" class="nav-chapter-link" data-id="1">1. Amor <span class="chapter-status" id="status-1">○</span></a>
        <a href="chapter_2.html" class="nav-chapter-link" data-id="2">2. La Cultura <span class="chapter-status" id="status-2">○</span></a>
        <a href="chapter_3.html" class="nav-chapter-link" data-id="3">3. El Porqué <span class="chapter-status" id="status-3">○</span></a>
'''

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix the double sidebar opening tag corruption
    # Look for: <div class="sidebar" \n    <!-- Sidebar Navigation -->\n    <div class="sidebar" id="mainSidebar">
    # This pattern occurred in chapter_1.html
    content = re.sub(r'<div class="sidebar"\s+<!-- Sidebar Navigation -->\s+<div class="sidebar" id="mainSidebar">', 
                     '<div class="sidebar" id="mainSidebar">', 
                     content, flags=re.DOTALL)
    
    # Also fix the case where it's just slightly different
    content = re.sub(r'<div class="sidebar"\s+<div class="sidebar" id="mainSidebar">', 
                     '<div class="sidebar" id="mainSidebar">', 
                     content)

    # 2. Fix the first few links if they are wrong (specifically chapter_2.html repeated)
    # We look for the specific corrupted sequence found in chapter_1.html
    corrupted_links = r'<a href="chapter_2.html" class="nav-chapter-link" data-id="2">1. Amor <span class="chapter-status" id="status-1">○</span></a>\s+<a href="chapter_2.html" class="nav-chapter-link" data-id="2">2. La Cultura <span class="chapter-status" id="status-2">○</span></a>'
    corrected_links = r'<a href="chapter_1.html" class="nav-chapter-link" data-id="1">1. Amor <span class="chapter-status" id="status-1">○</span></a>\n        <a href="chapter_2.html" class="nav-chapter-link" data-id="2">2. La Cultura <span class="chapter-status" id="status-2">○</span></a>'
    content = re.sub(corrupted_links, corrected_links, content)

    # 3. Correct the CHAPTER_ID based on filename
    match = re.search(r'chapter_(\d+)\.html', filename)
    if match:
        correct_id = match.group(1)
        content = re.sub(r'const CHAPTER_ID = ".*?";', f'const CHAPTER_ID = "{correct_id}";', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sidebar and CHAPTER_ID cleanup complete.")
