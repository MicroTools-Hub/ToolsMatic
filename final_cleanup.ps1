$toolsDir = "d:\ToolsMatic\tools"
$files = Get-ChildItem -Path $toolsDir -Filter "*.html"

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $original = $content
    
    # Remove empty divs with margin: 24px
    $content = $content -replace '  <div style="text-align: center; margin: 24px 0;"></div>\s*', ''
    
    # Remove divs with just atOptions script
    $content = $content -replace '<div style="text-align: center; margin: 24px 0;">\s*<script>\s*atOptions = \{[^}]*\};\s*</script>\s*</div>\s*', ''
    
    # Remove stray script tags with atOptions
    $content = $content -replace '<script>\s*atOptions = \{[^}]*\};\s*</script>\s*', ''
    
    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Cleaned: $($file.Name)"
    }
}
