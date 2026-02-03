import os
import glob
import re

notification = '<script async defer src="https://pl28613409.effectivegatecpm.com/51/33/02/5133020b94dad7bafd96065840c47d76.js"></script>'

# All files except word-counter (already done)
files = [f for f in glob.glob(r'd:\ToolsMatic\tools\*.html') if 'word-counter' not in f]
files += ['d:\ToolsMatic\contact.html', 'd:\ToolsMatic\privacy.html', 'd:\ToolsMatic\terms.html', 'd:\ToolsMatic\about.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find vercel insights script
    insights_match = re.search(r'<script[^>]*src="/_vercel/insights/script\.js"[^>]*></script>', content)
    
    if insights_match:
        # Insert after vercel insights
        end_pos = insights_match.end()
        content = content[:end_pos] + f'\n  {notification}\n  {notification}' + content[end_pos:]
    
    # Remove from before </body>
    content = re.sub(
        r'<script[^>]*src="https://pl28613409\.effectivegatecpm\.com/51/33/02/5133020b94dad7bafd96065840c47d76\.js"[^>]*></script>\s*',
        '',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {os.path.basename(filepath)}')

print('\n✓ Notification scripts moved to head for all files!')
