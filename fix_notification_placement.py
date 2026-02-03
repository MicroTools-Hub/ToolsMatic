import os
import glob
import re

notification_script = '<script async defer src="https://pl28613409.effectivegatecpm.com/51/33/02/5133020b94dad7bafd96065840c47d76.js"></script>'

files = glob.glob(r'd:\ToolsMatic\tools\*.html') + [
    'd:\ToolsMatic\index.html',
    'd:\ToolsMatic\contact.html',
    'd:\ToolsMatic\privacy.html',
    'd:\ToolsMatic\terms.html',
    'd:\ToolsMatic\about.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old notification scripts from before </body>
    content = re.sub(
        r'<script[^>]*src="https://pl28613409\.effectivegatecpm\.com/51/33/02/5133020b94dad7bafd96065840c47d76\.js"[^>]*></script>\s*',
        '',
        content
    )
    
    # Add to head instead (after cache-control meta tags)
    if '</head>' in content:
        # Add notification script in head
        content = content.replace(
            '</head>',
            f'  {notification_script}\n  {notification_script}\n</head>'
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ Moved notifications to head for: {os.path.basename(filepath)}')

print('\n✓ Notification scripts moved to head with async/defer')
