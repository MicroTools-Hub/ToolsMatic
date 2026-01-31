# PowerShell script to replace ALL instances of old ad blocks
$toolsDir = "d:\ToolsMatic\tools"
$files = Get-ChildItem -Path $toolsDir -Filter "*.html"

# Pattern to match old ad blocks with flexible spacing
$pattern = @"
<div style="text-align: center; margin: \d+px 0;">
\s*<script>
\s*atOptions = \{
\s*'key'\s*:\s*'e61a3745429623f25315f86052a3ab7b',
\s*'format'\s*:\s*'iframe',
\s*'height'\s*:\s*90,
\s*'width'\s*:\s*728,
\s*'params'\s*:\s*\{\}
\s*\};
\s*</script>
\s*<script src="https://www\.highperformanceformat\.com/e61a3745429623f25315f86052a3ab7b/invoke\.js"></script>
\s*</div>
"@

$replacement = @"
<div style="text-align: center; margin: 20px 0;">
      <script async="async" data-cfasync="false" src="https://pl28604956.effectivegatecpm.com/ec3790ad17aa114a9ec21293450604cc/invoke.js"></script>
      <div id="container-ec3790ad17aa114a9ec21293450604cc"></div>
    </div>
"@

$updatedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content
    
    # Count how many old ads are in this file
    $oldAdCount = ([regex]::Matches($content, [regex]::Escape("'key' : 'e61a3745429623f25315f86052a3ab7b'"))).Count
    
    if ($oldAdCount -gt 0) {
        # Replace using regex with flexible whitespace
        $content = [regex]::Replace($content, $pattern, $replacement, [System.Text.RegularExpressions.RegexOptions]::IgnorePatternWhitespace -bor [System.Text.RegularExpressions.RegexOptions]::Singleline)
        
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated: $($file.Name) - Found $oldAdCount old ad blocks"
        $updatedCount++
    }
}

Write-Host "`nTotal files updated: $updatedCount"
