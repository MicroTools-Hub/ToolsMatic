import os
import re
import glob

# ALL old ads to remove
old_ad_patterns = [
    # Vignette
    r'<script\s+src="https://www\.gizokraijaw\.net[^"]*"[^>]*></script>',
    # Popunder
    r'<script[^>]*src="[^"]*pl28613409[^"]*"[^>]*></script>',
    # Quge5 notifications
    r'<script[^>]*src="[^"]*quge5\.com[^"]*"[^>]*></script>',
    # Old ad containers
    r'<div[^>]*id="(ac|placer|placement)[^"]*"[^>]*>[^<]*</div>',
]

def remove_old_ads(content):
    """Remove all old ad code"""
    for pattern in old_ad_patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    return content

def clean_tool_file(filepath):
    """Clean a tool HTML file completely and rebuild"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old ads
    content = remove_old_ads(content)
    
    # Remove ALL atOptions banner ads - we'll add ONE back
    content = re.sub(
        r'<div[^>]*style="text-align: center; margin: 20px 0;"[^>]*>\s*<script>\s*atOptions\s*=\s*\{[^}]+\};\s*</script>\s*<script[^>]+highperformanceformat\.com[^>]*></script>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Get tool name from title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    tool_name = title_match.group(1) if title_match else "Tool"
    
    # Find the native ad div
    native_ad = '''<div id="container-ec3790ad17aa114a9ec21293450604cc"></div>'''
    native_ad_index = content.find(native_ad)
    
    if native_ad_index != -1:
        # Find the end of the native ad closing div (</div> after the native ad)
        end_native = content.find('</div>', native_ad_index + len(native_ad)) + 6
        
        # Insert ONE banner after native ad
        banner = '''
      <div style="text-align: center; margin: 20px 0;">
        <script>
          atOptions = {
            "key": "e61a3745429623f25315f86052a3ab7b",
            "format": "iframe",
            "height": 90,
            "width": 728,
            "params": {}
          };
        </script>
        <script src="https://www.highperformanceformat.com/e61a3745429623f25315f86052a3ab7b/invoke.js"></script>
      </div>'''
        
        # Insert banner right after native ad
        content = content[:end_native] + banner + content[end_native:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Cleaned: {os.path.basename(filepath)}")

# Clean all tool files
tool_files = glob.glob(r'd:\ToolsMatic\tools\*.html')
for tool_file in tool_files:
    try:
        clean_tool_file(tool_file)
    except Exception as e:
        print(f"✗ Error with {tool_file}: {e}")

# Clean index.html
def clean_index():
    with open(r'd:\ToolsMatic\index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old ads
    content = remove_old_ads(content)
    
    # Remove all old atOptions banners
    content = re.sub(
        r'<div[^>]*style="text-align: center; margin: 20px 0;"[^>]*>\s*<script>\s*atOptions\s*=\s*\{[^}]+\};\s*</script>\s*<script[^>]+highperformanceformat\.com[^>]*></script>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove duplicate H1 - keep only one "ToolsMatic" heading
    # Remove the page-intro div
    content = re.sub(r'<div class="page-intro">\s*<h1>ToolsMatic</h1>[^}]+?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Add ONE banner after native ad
    native_ad = '''<div id="container-ec3790ad17aa114a9ec21293450604cc"></div>'''
    native_ad_index = content.find(native_ad)
    
    if native_ad_index != -1:
        end_native = content.find('</div>', native_ad_index + len(native_ad)) + 6
        banner = '''
    <div style="text-align: center; margin: 20px 0;">
      <script>
        atOptions = {
          "key": "e61a3745429623f25315f86052a3ab7b",
          "format": "iframe",
          "height": 90,
          "width": 728,
          "params": {}
        };
      </script>
      <script src="https://www.highperformanceformat.com/e61a3745429623f25315f86052a3ab7b/invoke.js"></script>
    </div>'''
        content = content[:end_native] + banner + content[end_native:]
    
    with open(r'd:\ToolsMatic\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Cleaned: index.html")

clean_index()

# Clean other pages
for page in ['contact.html', 'privacy.html', 'terms.html']:
    try:
        path = rf'd:\ToolsMatic\{page}'
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = remove_old_ads(content)
        content = re.sub(
            r'<div[^>]*style="text-align: center; margin: 20px 0;"[^>]*>\s*<script>\s*atOptions\s*=\s*\{[^}]+\};\s*</script>\s*<script[^>]+highperformanceformat\.com[^>]*></script>\s*</div>',
            '',
            content,
            flags=re.DOTALL
        )
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Cleaned: {page}")
    except Exception as e:
        print(f"✗ Error with {page}: {e}")

print("\n✓ ALL FILES CLEANED - OLD ADS REMOVED, ONE BANNER PER PAGE")
