# PowerShell script to add proper ads to all tool pages
$toolsDir = "d:\ToolsMatic\tools"
$files = @("password-generator.html", "base64-encoder.html", "case-converter.html", "color-picker.html", "contrast-checker.html", "csv-inspector.html", "csv-to-json.html", "gradient-generator.html", "html-minifier.html", "image-compressor.html", "jwt-inspector.html", "lorem-ipsum-generator.html", "markdown-previewer.html", "number-converter.html", "qr-code-maker.html", "quote-generator.html", "regex-tester.html", "text-diff-checker.html", "timezone-converter.html", "unit-converter.html", "url-encoder.html", "uuid-maker.html", "ascii-art-generator.html", "bmi-calculator.html")

$nativeBanner = @"
    <div style="text-align: center; margin: 20px 0;">
      <script async="async" data-cfasync="false" src="https://pl28604956.effectivegatecpm.com/ec3790ad17aa114a9ec21293450604cc/invoke.js"></script>
      <div id="container-ec3790ad17aa114a9ec21293450604cc"></div>
    </div>
"@

$regularBanner = @"
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
    </div>
"@

foreach ($filename in $files) {
    $filepath = Join-Path $toolsDir $filename
    if (-not (Test-Path $filepath)) { continue }
    
    $content = [System.IO.File]::ReadAllText($filepath, [System.Text.Encoding]::UTF8)
    $original = $content
    
    # Count current native banners to find pattern
    $nativeCount = ([regex]::Matches($content, "pl28604956\.effectivegatecpm\.com")).Count
    
    # If only 1 native banner at top, add regular banner after it
    if ($nativeCount -eq 1) {
        $content = $content -replace '(<div style="text-align: center; margin: 20px 0;">\s*<script async="async"[^<]*pl28604956[^<]*</div>\s*</div>)(\s*<section class="tool-shell")', "`$1`n" + $regularBanner + "`n`$2"
    }
    
    # If more than 1, replace extras with proper pattern (1 native + 1 regular at top, then 3 ads before section)
    if ($nativeCount -gt 1) {
        # This handles cases where there are multiple native banners
        $content = $content -replace '(?s)<div style="text-align: center; margin: 20px 0;">\s*<script async="async"[^}]*effectivegatecpm[^<]*</div>\s*</div>(\s*<div style="text-align: center; margin: 20px 0;">\s*<script async="async"[^}]*effectivegatecpm[^<]*</div>\s*</div>)*', $nativeBanner + "`n" + $regularBanner
    }
    
    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($filepath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated: $filename"
    }
}

Write-Host "`nDone!"
