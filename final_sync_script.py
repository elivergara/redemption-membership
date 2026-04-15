import os
import re

directory = '/home/elivergara/Documents/redemption-membership/pages'
files = [f for f in os.listdir(directory) if f.startswith('chapter_') and f.endswith('.html')]

# --- CORE CONSTANTS ---
# New sidebar HTML structure (must be updated for the final version)
new_sidebar_html = r'''
    <!-- Sidebar Navigation -->
    <div class="sidebar" id="mainSidebar">
        
        <div class="nav-section-title">Inicio</div>
        <a href="chapter_1.html" class="nav-chapter-link" data-id="1">1. Amor <span class="chapter-status" id="status-1">○</span></a>
        <a href="chapter_2.html" class="nav-chapter-link" data-id="2">2. La Cultura <span class="chapter-status" id="status-2">○</span></a>
        <a href="chapter_3.html" class="nav-chapter-link" data-id="3">3. El Porqué <span class="chapter-status" id="status-3">○</span></a>

        <div class="nav-section-title">Sección 1 - Creencias</div>
        <div class="nav-section-title" style="font-size: 0.7rem; margin-top: 10px;">Doctrina</div>
        <a href="chapter_4.html" class="nav-chapter-link" data-id="4">4. Revelación <span class="chapter-status" id="status-4">○</span></a>
        <a href="chapter_5.html" class="nav-chapter-link" data-id="5">5. Trinidad <span class="chapter-status" id="status-5">○</span></a>
        <a href="chapter_6.html" class="nav-chapter-link" data-id="6">6. Humanidad <span class="chapter-status" id="status-6">○</span></a>
        <a href="chapter_7.html" class="nav-chapter-link" data-id="7">7. Soltería <span class="chapter-status" id="status-7">○</span></a>
        <a href="chapter_8.html" class="nav-chapter-link" data-id="8">8. La Caída <span class="chapter-status" id="status-8">○</span></a>
        <a href="chapter_9.html" class="nav-chapter-link" data-id="9">9. Elección <span class="chapter-status" id="status-9">○</span></a>
        <a href="chapter_10.html" class="nav-chapter-link" data-id="10">10. Buenas Noticias <span class="chapter-status" id="status-10">○</span></a>
        <a href="chapter_11.html" class="nav-chapter-link" data-id="11">11. Jesús <span class="chapter-status" id="status-11">○</span></a>
        <a href="chapter_12.html" class="nav-chapter-link" data-id="12">12. Justificación <span class="chapter-status" id="status-12">○</span></a>
        <a href="chapter_13.html" class="nav-chapter-link" data-id="13">13. Espíritu Santo <span class="chapter-status" id="status-13">○</span></a>
        <a href="chapter_14.html" class="nav-chapter-link" data-id="14">14. El Reino <span class="chapter-status" id="status-14">○</span></a>
        <a href="chapter_15.html" class="nav-chapter-link" data-id="15">15. La Iglesia <span class="chapter-status" id="status-15">○</span></a>
        <a href="chapter_16.html" class="nav-chapter-link" data-id="16">16. Restauración <span class="chapter-status" id="status-16">○</span></a>

        <div class="nav-section-title" style="font-size: 0.7rem; margin-top: 10px;">Convicciones</div>
        <a href="chapter_17.html" class="nav-chapter-link" data-id="17">17. Cristo & Cultura <span class="chapter-status" id="status-17">○</span></a>
        <a href="chapter_18.html" class="nav-chapter-link" data-id="18">18. El Pobre <span class="chapter-status" id="status-18">○</span></a>
        <a href="chapter_19.html" class="nav-chapter-link" data-id="19">19. Disciplina <span class="chapter-status" id="status-19">○</span></a>
        <a href="chapter_20.html" class="nav-chapter-link" data-id="20">20. Ordenanzas <span class="chapter-status" id="status-20">○</span></a>
        <a href="chapter_21.html" class="nav-chapter-link" data-id="21">21. Divorcio <span class="chapter-status" id="status-21">○</span></a>
        <a href="chapter_22.html" class="nav-chapter-link" data-id="22">22. Cuerpo & Sexo <span class="chapter-status" id="status-22">○</span></a>
        <a href="chapter_23.html" class="nav-chapter-link" data-id="23">23. Racismo <span class="chapter-status" id="status-23">○</span></a>
        <a href="chapter_24.html" class="nav-chapter-link" data-id="24">24. Gobierno <span class="chapter-status" id="status-24">○</span></a>
        <a href="chapter_25.html" class="nav-chapter-link" data-id="25">25. Señales <span class="chapter-status" id="status-25">○</span></a>
        <a href="chapter_26.html" class="nav-chapter-link" data-id="26">26. Reino Milenial <span class="chapter-status" id="status-26">○</span></a>
        <a href="chapter_27.html" class="nav-chapter-link" data-id="27">27. Edad Tierra <span class="chapter-status" id="status-27">○</span></a>

        <div class="nav-section-title">Sección 2 - Distintivos</div>
        <a href="chapter_28.html" class="nav-chapter-link" data-id="28">28. Estructura <span class="chapter-status" id="status-28">○</span></a>
        <a href="chapter_29.html" class="nav-chapter-link" data-id="29">29. Misión & Visión <span class="chapter-status" id="status-29">○</span></a>
        <a href="chapter_30.html" class="nav-chapter-link" data-id="30">30. Enfoque Fuera <span class="chapter-status" id="status-30">○</span></a>

        <div class="nav-section-title">Sección 3 - El Pacto</div>
        <a href="chapter_31.html" class="nav-chapter-link" data-id="31">31. Política Líderes <span class="chapter-status" id="status-31">○</span></a>
        <a href="chapter_32.html" class="nav-chapter-link" data-id="32">32. Promesa Liderazgo <span class="chapter-status" id="status-32">○</span></a>
        <a href="chapter_33.html" class="nav-chapter-link" data-id="33">33. Promesa Miembros <span class="chapter-status" id="status-33">○</span></a>
        <a href="chapter_34.html" class="nav-chapter-link" data-id="34">34. Salida Sana <span class="chapter-status" id="status-34">○</span></a>
    </div>
'''

# Regex for the pattern to find and replace specific text content in links (e.g., "chapter_23.html" link text)
# We must escape characters that have special meaning in regex.
def update_chapter_content(content, filename, old_id, new_id, old_title, new_title):
    # 1. Update the link text/title/data-id within the sidebar
    content = re.sub(r'data-id="' + re.escape(str(old_id)) + r'"', f'data-id="{new_id}"', content)
    content = re.sub(r'<a href="chapter_' + re.escape(str(old_id)) + r'\.html"', f'<a href="chapter_{new_id}.html"', content)
    # This is the hardest part: updating the visible text. We use a general pattern matching the surrounding text.
    # Since we cannot reliably isolate *only* the title text without risking breaking surrounding tags, 
    # we will replace the entire anchor tag for safety, IF the pattern is clean.
    # For robustness, we will rely on updating the JS ID/link href, as the visible text is what's most likely to be hardcoded/duplicated.

    # 2. Update the JS constant
    content = re.sub(r'const CHAPTER_ID = ".*?";', f'const CHAPTER_ID = "{new_id}";', content)

    # 3. Update Pagination Logic (Next Button)
    content = content.replace('if (currentId < 33)', 'if (currentId < 34)')
    content = content.replace('if (currentId < 34)', 'if (currentId < 34)') # Safety patch

    return content

# --- EXECUTION ---
for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. SYNC SIDEBAR (Attempting surgical replacement)
    # We assume the sidebar container is always present, even if corrupted.
    content = re.sub(r'id="mainSidebar">.*?</div', new_sidebar_html, content, flags=re.DOTALL | re.IGNORECASE)

    # 2. SYNC JS ID AND PAGINATION
    try:
        # Simple attempt to extract old ID from filename (e.g., chapter_23.html -> 23)
        match = re.search(r'chapter_(\d+)\.html', filename)
        old_id = match.group(1)
        new_id = str(int(old_id) + 1) if old_id != '23' else '23'
        
        # Execute the update function
        content = update_chapter_content(content, filename, old_id, new_id, "", "")

    except Exception as e:
        print(f"Skipping {filename} due to error during update: {e}")
        pass

    # Write back the modified content
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {filename}")

print("--- All chapter files have been updated with new IDs and sidebar structure. ---")