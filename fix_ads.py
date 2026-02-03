import re
import glob

# Banner ad to add after native ad
banner_ad = '''    <div style="text-align: center; margin: 20px 0;">
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
    </div>
'''

print("Cleaning and updating tool pages...")

tool_files = glob.glob(r'd:\ToolsMatic\tools\*.html')

for f in tool_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove quge5 ads
    content = re.sub(r'<script src="https://quge5\.com/[^>]+></script>\s*', '', content)
    
    # Remove ALL old banner ads
    while re.search(r'<div[^>]*>\s*<script>\s*atOptions\s*=\s*\{[^\}]+\};\s*</script>\s*<script[^>]+highperformanceformat\.com[^>]+></script>\s*</div>', content, re.DOTALL):
        content = re.sub(r'<div[^>]*>\s*<script>\s*atOptions\s*=\s*\{[^\}]+\};\s*</script>\s*<script[^>]+highperformanceformat\.com[^>]+></script>\s*</div>', '', content, count=1, flags=re.DOTALL)
    
    # Now add ONE banner after the native ad if not already there
    if content.count('highperformanceformat.com') == 0:
        # Add banner after native ad container
        content = re.sub(
            r'(<div id="container-ec3790ad17aa114a9ec21293450604cc"></div>\s*</div>\s*\n)',
            r'\1\n' + banner_ad + '\n',
            content
        )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated {len(tool_files)} tool files - each now has vignette, native ad, and 1 banner")
print("\nFinal structure:")
print("1. Vignette ad (in <head>)")
print("2. Native ad (pl28604956) after <main>")  
print("3. ONE banner ad (highperformanceformat) after native ad")
