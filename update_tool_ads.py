#!/usr/bin/env python3
import os
import re
from pathlib import Path

tool_dir = Path("d:/ToolsMatic/tools")
native_banner = '''    <div style="text-align: center; margin: 20px 0;">
      <script async="async" data-cfasync="false" src="https://pl28604956.effectivegatecpm.com/ec3790ad17aa114a9ec21293450604cc/invoke.js"></script>
      <div id="container-ec3790ad17aa114a9ec21293450604cc"></div>
    </div>'''

regular_banner = '''    <div style="text-align: center; margin: 20px 0;">
      <script>
        atOptions = {
          'key' : 'e61a3745429623f25315f86052a3ab7b',
          'format' : 'iframe',
          'height' : 90,
          'width' : 728,
          'params' : {}
        };
      </script>
      <script src="https://www.highperformanceformat.com/e61a3745429623f25315f86052a3ab7b/invoke.js"></script>
    </div>'''

for html_file in tool_dir.glob("*.html"):
    if html_file.name == "word-counter.html":
        continue
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add regular banner after native banner at top
    pattern = r'(<main>\s*<div style="text-align: center; margin: 20px 0;">\s*<script async="async" data-cfasync="false".*?</div>\s*</div>)(\s*<section class="tool-shell")'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, r'\1\n' + regular_banner + r'\2', content, count=1, flags=re.DOTALL)
    
    # Add 3 ads before info section
    pattern_before_section = r'(</section>)(\s*<section class="section")'
    if re.search(pattern_before_section, content, re.DOTALL):
        three_ads = native_banner + '\n' + regular_banner + '\n' + native_banner
        content = re.sub(pattern_before_section, r'\1\n\n' + three_ads + r'\n\n\2', content, count=1, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {html_file.name}")

print("All files updated successfully!")
