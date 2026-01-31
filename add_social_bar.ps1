$toolFiles = @(
    "tools/password-generator.html",
    "tools/quote-generator.html",
    "tools/ascii-art-generator.html",
    "tools/case-converter.html",
    "tools/gradient-generator.html",
    "tools/contrast-checker.html",
    "tools/json-formatter.html",
    "tools/base64-encoder.html",
    "tools/image-compressor.html",
    "tools/qr-code-maker.html",
    "tools/jwt-inspector.html",
    "tools/markdown-previewer.html",
    "tools/regex-tester.html",
    "tools/uuid-maker.html",
    "tools/url-encoder.html",
    "tools/color-picker.html",
    "tools/unit-converter.html",
    "tools/timezone-converter.html",
    "tools/text-diff-checker.html",
    "tools/lorem-ipsum-generator.html",
    "tools/csv-to-json.html",
    "tools/csv-inspector.html",
    "tools/html-minifier.html",
    "tools/bmi-calculator.html",
    "tools/number-converter.html"
)

$script = '    <script src="https://pl28613409.effectivegatecpm.com/51/33/02/5133020b94dad7bafd96065840c47d76.js"></script>'

foreach ($file in $toolFiles) {
    $filePath = "d:\ToolsMatic\$file"
    
    if (Test-Path $filePath) {
        $content = Get-Content $filePath -Raw
        
        # Check if script already added
        if ($content -notmatch "5133020b94dad7bafd96065840c47d76") {
            # Replace </head> with script + </head>
            $newContent = $content -replace '</head>', "$script`n</head>"
            Set-Content $filePath $newContent
            Write-Host "Added social bar to $file"
        } else {
            Write-Host "Social bar already exists in $file"
        }
    } else {
        Write-Host "File not found: $file"
    }
}

Write-Host "Done adding social bar to all tool pages"
