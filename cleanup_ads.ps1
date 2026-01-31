# PowerShell script to remove any remaining orphaned old ad scripts
$toolsDir = "d:\ToolsMatic\tools"
$files = Get-ChildItem -Path $toolsDir -Filter "*.html"

# Pattern for orphaned script tags with highperformanceformat
$orphanedPattern = '<script src="https://www\.highperformanceformat\.com/e61a3745429623f25315f86052a3ab7b/invoke\.js"></script>'

$updatedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content
    
    # Remove all orphaned script references
    $content = $content -replace $orphanedPattern, ''
    
    # Also remove empty div containers that were left behind
    $content = $content -replace '<div style="text-align: center; margin: \d+px 0;"></div>\s*', ''
    
    # Check if file was modified
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Cleaned: $($file.Name)"
        $updatedCount++
    }
}

Write-Host "`nTotal files cleaned: $updatedCount"
