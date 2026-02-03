import re
import glob

# Ad codes
native_ad = '''    <div style="text-align: center; margin: 20px 0;">
      <script async="async" data-cfasync="false" src="https://pl28604956.effectivegatecpm.com/ec3790ad17aa114a9ec21293450604cc/invoke.js"></script>
      <div id="container-ec3790ad17aa114a9ec21293450604cc"></div>
    </div>'''

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
    </div>'''

# Tool file mappings with descriptions
tool_info = {
    'word-counter': {'title': 'Advanced Word Counter', 'desc': 'Get detailed text statistics including word count, character count,<br>readability scores, reading time, and more. Real-time analysis<br>for writers, students, and content creators.'},
    'ascii-art-generator': {'title': 'ASCII Art Generator', 'desc': 'Transform plain text into stunning ASCII art with multiple<br>font styles and formatting options. Perfect for creating<br>text-based graphics and decorative headers.'},
    'base64-encoder': {'title': 'Base64 Encoder/Decoder', 'desc': 'Quickly encode text and data to Base64 format or decode<br>Base64 strings back to plain text. Useful for data transmission<br>and encoding sensitive information.'},
    'bmi-calculator': {'title': 'BMI Calculator', 'desc': 'Calculate your Body Mass Index instantly with metric or<br>imperial units. Get instant health metrics and BMI category<br>classification in real-time.'},
    'case-converter': {'title': 'Case Converter', 'desc': 'Convert text between uppercase, lowercase, title case,<br>sentence case, and more. Perfect for standardizing text<br>formatting across your documents.'},
    'color-picker': {'title': 'Color Picker', 'desc': 'Select and convert colors between HEX, RGB, and HSL formats.<br>Get color codes instantly and explore color palettes<br>with real-time color preview.'},
    'contrast-checker': {'title': 'Contrast Checker', 'desc': 'Check color contrast ratios for web accessibility compliance.<br>Ensure your text and backgrounds meet WCAG standards<br>for readability and accessibility.'},
    'csv-inspector': {'title': 'CSV Inspector', 'desc': 'Inspect, validate, and analyze CSV files instantly. View<br>data in a clean table format and identify formatting issues<br>quickly and easily.'},
    'csv-to-json': {'title': 'CSV to JSON Converter', 'desc': 'Convert CSV data to JSON format instantly. Perfect for<br>transforming spreadsheet data into API-ready JSON<br>with proper formatting.'},
    'gradient-generator': {'title': 'Gradient Generator', 'desc': 'Create beautiful CSS gradients with live preview. Generate<br>linear, radial, and conic gradients with custom colors<br>and export ready-to-use CSS code.'},
    'html-minifier': {'title': 'HTML Minifier', 'desc': 'Reduce HTML file size by removing unnecessary whitespace<br>and comments. Speed up your website by minifying HTML<br>code instantly and easily.'},
    'image-compressor': {'title': 'Image Compressor', 'desc': 'Compress images while maintaining quality. Reduce file sizes<br>for faster loading times without losing visual quality<br>in your photos and graphics.'},
    'json-formatter': {'title': 'JSON Formatter', 'desc': 'Format, validate, and beautify JSON data instantly. Identify<br>syntax errors and convert minified JSON into readable<br>formatted code with proper indentation.'},
    'jwt-inspector': {'title': 'JWT Inspector', 'desc': 'Decode and inspect JWT tokens instantly. View payload,<br>header, and signature information for authentication<br>tokens in a clear, readable format.'},
    'lorem-ipsum-generator': {'title': 'Lorem Ipsum Generator', 'desc': 'Generate placeholder text for design mockups and prototypes.<br>Create custom paragraphs, sentences, or words instantly<br>for your design and development projects.'},
    'markdown-previewer': {'title': 'Markdown Previewer', 'desc': 'Write Markdown and see live preview side-by-side. Convert<br>Markdown to HTML instantly with real-time rendering<br>and syntax highlighting.'},
    'number-converter': {'title': 'Number Converter', 'desc': 'Convert numbers between decimal, binary, hexadecimal,<br>and octal formats instantly. Perfect for programmers<br>and anyone working with different number systems.'},
    'password-generator': {'title': 'Password Generator', 'desc': 'Create strong, secure passwords with custom options.<br>Control length, characters, and complexity to generate<br>unique passwords instantly.'},
    'qr-code-maker': {'title': 'QR Code Generator', 'desc': 'Generate QR codes from text or URLs instantly. Download<br>as PNG or customize size and error correction levels<br>for your marketing and tracking needs.'},
    'quote-generator': {'title': 'Random Quote Generator', 'desc': 'Get inspired with random motivational and famous quotes.<br>Perfect for social media posts, presentations, and<br>daily inspiration.'},
    'regex-tester': {'title': 'Regex Tester', 'desc': 'Test and debug regular expressions with instant feedback.<br>Check matches, replacements, and pattern validation<br>with real-time results and explanations.'},
    'text-diff-checker': {'title': 'Text Diff Checker', 'desc': 'Compare two texts and highlight differences instantly.<br>Perfect for spotting changes and reviewing text variations<br>side-by-side with clear visual markers.'},
    'timezone-converter': {'title': 'Timezone Converter', 'desc': 'Convert times between different timezones instantly.<br>Never miss meetings or events across time zones<br>with accurate time conversion.'},
    'unit-converter': {'title': 'Unit Converter', 'desc': 'Convert between various units of measurement instantly.<br>Length, weight, temperature, volume and more<br>with accurate conversions.'},
    'url-encoder': {'title': 'URL Encoder/Decoder', 'desc': 'Encode text to URL-safe format or decode encoded URLs.<br>Perfect for API calls, query parameters, and web<br>development tasks.'},
    'uuid-maker': {'title': 'UUID Generator', 'desc': 'Generate unique UUIDs (v1, v4) instantly for your<br>applications. Copy with one click and create multiple<br>UUIDs in batch.'},
    'contact': {'title': 'Contact', 'desc': 'Get in touch with the ToolsMatic team. We''d love to hear<br>from you about feedback, suggestions, or collaborations.<br>Reach out anytime.'},
    'privacy': {'title': 'Privacy Policy', 'desc': 'Learn how we protect your data and privacy. Our commitment<br>to transparency and security in everything we do.<br>Your privacy is our priority.'},
    'terms': {'title': 'Terms of Service', 'desc': 'Review our terms and conditions for using ToolsMatic.<br>Important information about your rights and<br>responsibilities when using our tools.'},
}

print("Structuring all HTML files...")

all_files = glob.glob(r'd:\ToolsMatic\tools\*.html') + [r'd:\ToolsMatic\index.html', r'd:\ToolsMatic\contact.html', r'd:\ToolsMatic\privacy.html', r'd:\ToolsMatic\terms.html']

for f in all_files:
    filename = f.split('\\')[-1].replace('.html', '')
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Get info
    if filename in tool_info:
        info = tool_info[filename]
        title = info['title']
        desc = info['desc']
    else:
        title = filename.replace('-', ' ').title()
        desc = 'Fast online utility.<br>Easy to use and completely free.<br>No installation or signup required.'
    
    # Find main section and insert structure
    if '<main>' in content:
        new_section = f'''
    <h1 style="text-align: center; font-size: 2em; margin: 20px 0;">{title}</h1>
    <p style="text-align: center; margin-bottom: 30px; line-height: 1.6;">
      {desc}
    </p>

{native_ad}

{banner_ad}
'''
        content = content.replace('<main>\n', '<main>\n' + new_section + '\n')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Successfully structured {len(all_files)} files")
print("\nStructure on each page:")
print("✓ H1 heading (page name)")
print("✓ 3-line description")
print("✓ Native ad (pl28604956)")
print("✓ ONE banner ad (highperformanceformat)")

