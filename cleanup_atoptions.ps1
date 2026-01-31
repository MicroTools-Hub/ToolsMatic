# PowerShell script to remove orphaned atOptions blocks
$toolsDir = "d:\ToolsMatic\tools"
$files = Get-ChildItem -Path $toolsDir -Filter "*.html"

# Pattern for orphaned atOptions blocks
$atOptionsPattern = '<script>\s*atOptions = \{[^}]+\};\s*</script>'

$updatedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content
    
    # Remove all orphaned atOptions blocks
    $content = [regex]::Replace($content, $atOptionsPattern, '', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    # Check if file was modified
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Cleaned atOptions: $($file.Name)"
        $updatedCount++
    }
}

Write-Host "`nTotal files cleaned: $updatedCount"
