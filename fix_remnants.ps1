# PowerShell script to remove empty ad divs with orphaned atOptions
$toolsDir = "d:\ToolsMatic\tools"
$files = Get-ChildItem -Path $toolsDir -Filter "*.html"

$updatedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content
    
    # Remove the pattern: <div style="text-align: center; margin: ...px 0;"><script>atOptions...</script></div>
    # Using a simpler approach - find and remove divs that contain atOptions
    $content = $content -replace '(?s)<div style="text-align: center; margin: \d+px 0;?">\s*<script>\s*atOptions\s*=\s*\{[^}]+\};\s*</script>\s*</div>', ''
    
    # Also remove standalone atOptions scripts
    $content = $content -replace '(?s)\s*<script>\s*atOptions\s*=\s*\{[^}]+\};\s*</script>\s*', ''
    
    # Check if file was modified
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Fixed: $($file.Name)"
        $updatedCount++
    }
}

Write-Host "`nTotal files fixed: $updatedCount"
