import os
import glob

notification_script = '<script src="https://pl28613409.effectivegatecpm.com/51/33/02/5133020b94dad7bafd96065840c47d76.js"></script>'

# All HTML files
files = glob.glob(r'd:\ToolsMatic\tools\*.html') + [
    'd:\ToolsMatic\index.html',
    'd:\ToolsMatic\contact.html',
    'd:\ToolsMatic\privacy.html',
    'd:\ToolsMatic\terms.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace </body> with the notification scripts + </body>
    # Add TWO notification scripts
    replacement = f'{notification_script}\n  {notification_script}\n</body>'
    content = content.replace('</body>', replacement)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Added notifications to: {os.path.basename(filepath)}")

print("\n✓ Two notification ads added to all pages!")
