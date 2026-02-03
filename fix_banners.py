import os
import glob
import re

# Get all tool files
tool_files = glob.glob(r'd:\ToolsMatic\tools\*.html') + [
    'd:\ToolsMatic\index.html',
    'd:\ToolsMatic\contact.html', 
    'd:\ToolsMatic\privacy.html',
    'd:\ToolsMatic\terms.html'
]

for filepath in tool_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find native ad div
    native_pattern = r'(<div[^>]*id="container-ec3790ad17aa114a9ec21293450604cc"[^>]*></div>\s*</div>)'
    match = re.search(native_pattern, content)
    
    if not match:
        continue
    
    native_end = match.end()
    
    # Find ALL banner divs after native ad
    # Pattern: <div style="text-align: center...> through </div> containing atOptions
    after_native = content[native_end:]
    
    # Find where real content starts (first <section or tool-shell or <h1 or <textarea)
    content_start = len(after_native)
    for pattern in ['<section', '<textarea', 'tool-shell', '<div class="']:
        pos = after_native.lower().find(pattern.lower())
        if pos != -1 and pos < content_start:
            content_start = pos
    
    # Get the ad section (everything between native ad and real content)
    ad_section = after_native[:content_start]
    
    # Find all banner divs in this section
    banner_pattern = r'<div style="text-align: center; margin: 20px 0;">[^<]*<script[^>]*>[\s\S]*?</script>[\s\S]*?</div>'
    banners = list(re.finditer(banner_pattern, ad_section))
    
    if len(banners) > 1:
        # Keep first, remove rest
        to_remove = ad_section
        for i, banner in enumerate(banners[1:], 1):
            to_remove = to_remove.replace(banner.group(0), '', 1)
        
        # Replace in content
        new_ad_section = ad_section.replace(ad_section, to_remove)
        content = content[:native_end] + new_ad_section + content[native_end + len(ad_section):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Fixed: {os.path.basename(filepath)}")

print("\nAll duplicate banners removed!")
