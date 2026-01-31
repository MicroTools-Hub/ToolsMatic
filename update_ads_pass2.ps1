# PowerShell script to update all HTML files with new banner ads - Second pass
$toolsDir = "d:\ToolsMatic\tools"
$files = Get-ChildItem -Path $toolsDir -Filter "*.html"

# Pattern for old single ad blocks with different margins
$oldSingleAdPattern = '<div style="text-align: center; margin: (\d+)px 0;">\s*<script>\s*atOptions = \{[^}]+\};\s*</script>\s*<script src="https://www\.highperformanceformat\.com/[^"]+/invoke\.js"></script>\s*</div>'

$newSingleAd = @"
<div style="text-align: center; margin: 20px 0;">
      <script async="async" data-cfasync="false" src="https://pl28604956.effectivegatecpm.com/ec3790ad17aa114a9ec21293450604cc/invoke.js"></script>
      <div id="container-ec3790ad17aa114a9ec21293450604cc"></div>
    </div>
"@

$updatedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content
    
    # Replace old single ad blocks (with any margin value)
    $content = [regex]::Replace($content, $oldSingleAdPattern, $newSingleAd, [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    # Check if file was modified
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated: $($file.Name)"
        $updatedCount++
    }
}

Write-Host "`nTotal files updated in second pass: $updatedCount"
