import glob
import re
import os

SCRIPT_SRC = "https://pl28613409.effectivegatecpm.com/51/33/02/5133020b94dad7bafd96065840c47d76.js"
SCRIPT_TAG = f'<script src="{SCRIPT_SRC}"></script>'

files = glob.glob(r"d:\ToolsMatic\**\*.html", recursive=True)

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove any existing instances (with any attrs)
    content = re.sub(rf"<script[^>]*src=\"{re.escape(SCRIPT_SRC)}\"[^>]*></script>\s*", "", content, flags=re.IGNORECASE)

    # Insert once before </body>
    if "</body>" in content:
        content = content.replace("</body>", f"  {SCRIPT_TAG}\n</body>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ {os.path.basename(path)}")

print("\n✓ Social bar script normalized across all pages")
