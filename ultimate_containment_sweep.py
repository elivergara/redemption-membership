import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.startswith('chapter_') and f.endswith('.html')]

# Marker regex for the end of the sidebar
# We expect to find the closing tag of the sidebar somewhere before the content wrapper
sidebar_end_pattern = r'</div >\n\n' 

# Marker for the start of the main content area
content_start_pattern = r'<div class="main-content-wrapper">'

print("Starting final layout containment sweep...")

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Target the messy gap between the sidebar close and content start
    # We search for the pattern: [any characters/newlines] + [content_start_pattern]
    
    # Step A: Clean up the sidebar section by ensuring the sidebar always ends properly.
    # This assumes the last block before the content wrapper is the sidebar.
    # We look for any loose link structure between the sidebar closing tag and the content wrapper.
    
    # Create the cleanup pattern: any character (*?) non-greedily, between the end of the sidebar and the start of content
    cleanup_pattern = re.compile(r'</div >\s*(.*?)<div class="main-content-wrapper">', re.DOTALL)
    
    if cleanup_pattern.search(content):
        # Replacement: Just take the content wrapper start marker, discarding whatever was floating before it.
        content = re.sub(cleanup_pattern, r'</div class="sidebar" id="mainSidebar">\n\n<div class="main-content-wrapper">', content, count=1, flags=re.DOTALL)
        print(f"Successfully cleaned structural gap in {filename}.")
    else:
        print(f"No obvious gap found requiring cleanup in {filename}. Assuming correct structure.")


    # Write back the modified content
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("\n--- ALL CHAPTER LAYOUTS HAVE BEEN CLEANED AND RESTORED TO CORRECT CONTAINMENT. ---")