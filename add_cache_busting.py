import os
import time
import glob

timestamp = str(int(time.time()))

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
    
    if '<head>' in content:
        content = content.replace(
            '<head>',
            f'<head>\n  <!-- Cache Buster: {timestamp} -->\n  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n  <meta http-equiv="Pragma" content="no-cache">\n  <meta http-equiv="Expires" content="0">'
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ Added cache busting to: {os.path.basename(filepath)}')

print('\n✓ Cache busting added to all files')
