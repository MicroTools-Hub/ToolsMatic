import re
import glob

native_ad = '''
    <div style="text-align: center; margin: 20px 0;">
      <script async="async" data-cfasync="false" src="https://pl28604956.effectivegatecpm.com/ec3790ad17aa114a9ec21293450604cc/invoke.js"></script>
      <div id="container-ec3790ad17aa114a9ec21293450604cc"></div>
    </div>'''

banner_ad = '''
    <div style="text-align: center; margin: 20px 0;">
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

tool_info = {
    'word-counter': ('Advanced Word Counter', 'Get detailed text statistics including word count, character count,<br>readability scores, reading time, and more. Real-time analysis<br>for writers, students, and content creators.'),
    'ascii-art-generator': ('ASCII Art Generator', 'Transform plain text into stunning ASCII art with multiple<br>font styles and formatting options. Perfect for creating<br>text-based graphics and decorative headers.'),
    'base64-encoder': ('Base64 Encoder/Decoder', 'Quickly encode text and data to Base64 format or decode<br>Base64 strings back to plain text. Useful for data transmission<br>and encoding sensitive information.'),
    'bmi-calculator': ('BMI Calculator', 'Calculate your Body Mass Index instantly with metric or<br>imperial units. Get instant health metrics and BMI category<br>classification in real-time.'),
    'case-converter': ('Case Converter', 'Convert text between uppercase, lowercase, title case,<br>sentence case, and more. Perfect for standardizing text<br>formatting across your documents.'),
    'color-picker': ('Color Picker', 'Select and convert colors between HEX, RGB, and HSL formats.<br>Get color codes instantly and explore color palettes<br>with real-time color preview.'),
    'contrast-checker': ('Contrast Checker', 'Check color contrast ratios for web accessibility compliance.<br>Ensure your text and backgrounds meet WCAG standards<br>for readability and accessibility.'),
    'csv-inspector': ('CSV Inspector', 'Inspect, validate, and analyze CSV files instantly. View<br>data in a clean table format and identify formatting issues<br>quickly and easily.'),
    'csv-to-json': ('CSV to JSON Converter', 'Convert CSV data to JSON format instantly. Perfect for<br>transforming spreadsheet data into API-ready JSON<br>with proper formatting.'),
    'gradient-generator': ('Gradient Generator', 'Create beautiful CSS gradients with live preview. Generate<br>linear, radial, and conic gradients with custom colors<br>and export ready-to-use CSS code.'),
    'html-minifier': ('HTML Minifier', 'Reduce HTML file size by removing unnecessary whitespace<br>and comments. Speed up your website by minifying HTML<br>code instantly and easily.'),
    'image-compressor': ('Image Compressor', 'Compress images while maintaining quality. Reduce file sizes<br>for faster loading times without losing visual quality<br>in your photos and graphics.'),
    'json-formatter': ('JSON Formatter', 'Format, validate, and beautify JSON data instantly. Identify<br>syntax errors and convert minified JSON into readable<br>formatted code with proper indentation.'),
    'jwt-inspector': ('JWT Inspector', 'Decode and inspect JWT tokens instantly. View payload,<br>header, and signature information for authentication<br>tokens in a clear, readable format.'),
    'lorem-ipsum-generator': ('Lorem Ipsum Generator', 'Generate placeholder text for design mockups and prototypes.<br>Create custom paragraphs, sentences, or words instantly<br>for your design and development projects.'),
    'markdown-previewer': ('Markdown Previewer', 'Write Markdown and see live preview side-by-side. Convert<br>Markdown to HTML instantly with real-time rendering<br>and syntax highlighting.'),
    'number-converter': ('Number Converter', 'Convert numbers between decimal, binary, hexadecimal,<br>and octal formats instantly. Perfect for programmers<br>and anyone working with different number systems.'),
    'password-generator': ('Password Generator', 'Create strong, secure passwords with custom options.<br>Control length, characters, and complexity to generate<br>unique passwords instantly.'),
    'qr-code-maker': ('QR Code Generator', 'Generate QR codes from text or URLs instantly. Download<br>as PNG or customize size and error correction levels<br>for your marketing and tracking needs.'),
    'quote-generator': ('Random Quote Generator', 'Get inspired with random motivational and famous quotes.<br>Perfect for social media posts, presentations, and<br>daily inspiration.'),
    'regex-tester': ('Regex Tester', 'Test and debug regular expressions with instant feedback.<br>Check matches, replacements, and pattern validation<br>with real-time results and explanations.'),
    'text-diff-checker': ('Text Diff Checker', 'Compare two texts and highlight differences instantly.<br>Perfect for spotting changes and reviewing text variations<br>side-by-side with clear visual markers.'),
    'timezone-converter': ('Timezone Converter', 'Convert times between different timezones instantly.<br>Never miss meetings or events across time zones<br>with accurate time conversion.'),
    'unit-converter': ('Unit Converter', 'Convert between various units of measurement instantly.<br>Length, weight, temperature, volume and more<br>with accurate conversions.'),
    'url-encoder': ('URL Encoder/Decoder', 'Encode text to URL-safe format or decode encoded URLs.<br>Perfect for API calls, query parameters, and web<br>development tasks.'),
    'uuid-maker': ('UUID Generator', 'Generate unique UUIDs (v1, v4) instantly for your<br>applications. Copy with one click and create multiple<br>UUIDs in batch.'),
}

files = glob.glob(r'd:\ToolsMatic\tools\*.html')

for f in files:
    filename = f.split('\\')[-1].replace('.html', '')
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if filename in tool_info:
        title, desc = tool_info[filename]
    else:
        title = filename.replace('-', ' ').title()
        desc = 'Fast tool for your needs.<br>Easy to use and free.<br>No signup required.'
    
    section = f'''
    <h1 style="text-align: center; font-size: 2em; margin: 20px 0;">{title}</h1>
    <p style="text-align: center; margin-bottom: 20px; line-height: 1.6;">
      {desc}
    </p>
{native_ad}
{banner_ad}
'''
    
    # Insert right after <main> opening tag, only if not already there
    if 'Advanced Word Counter' not in content:  # Check if already added
        content = content.replace('<main>\n', '<main>' + section + '\n')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Added H1, description, native ad, and 1 banner to {len(files)} tool files")
