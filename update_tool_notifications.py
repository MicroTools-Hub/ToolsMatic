import os
import glob
import re

notification = '<script async defer src="https://pl28613409.effectivegatecpm.com/51/33/02/5133020b94dad7bafd96065840c47d76.js"></script>'

# All tool files
files = glob.glob(r'd:\ToolsMatic\tools\*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add to head (before </head>)
    if '</head>' in content:
        content = content.replace(
            '</head>',
            f'  {notification}\n  {notification}\n</head>'
        )
    
    # Remove from bottom (before </body>)
    content = re.sub(
        r'<script[^>]*src="https://pl28613409\.effectivegatecpm\.com/51/33/02/5133020b94dad7bafd96065840c47d76\.js"[^>]*></script>\s*',
        '',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {os.path.basename(filepath)}')

print('\nAll tool files updated!')
