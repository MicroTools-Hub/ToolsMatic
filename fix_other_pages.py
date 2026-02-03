import os
import re

for f in ['contact.html', 'privacy.html', 'terms.html']:
    path = f'd:\\ToolsMatic\\{f}'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        match = re.search(r'(<div[^>]*id="container-ec3790ad17aa114a9ec21293450604cc"[^>]*></div>\s*</div>)', content)
        if match:
            native_end = match.end()
            after = content[native_end:]
            
            indices = []
            for p in ['<section', '<textarea', 'tool-shell']:
                idx = after.lower().find(p.lower())
                if idx > 0:
                    indices.append(idx)
            
            if indices:
                content_start = min(indices)
                ad_section = after[:content_start]
                banner_pattern = r'<div style="text-align: center; margin: 20px 0;">[^<]*<script[^>]*>[\s\S]*?</script>[\s\S]*?</div>'
                banners = list(re.finditer(banner_pattern, ad_section))
                
                if len(banners) > 1:
                    for banner in banners[1:]:
                        ad_section = ad_section.replace(banner.group(0), '', 1)
                    content = content[:native_end] + ad_section + content[native_end + len(after) - len(ad_section):]
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'✓ {f}')
    except Exception as e:
        print(f'✗ {f}: {e}')
