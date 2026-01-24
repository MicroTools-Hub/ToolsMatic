
# Fix corrupted emoji encoding
$files = Get-ChildItem -Path "d:\ToolsMatic\tools\*.html"

$fixes = @(
    @{Pattern = '(?s)ðŸŒ™'; Replacement = '🌙'},
    @{Pattern = '(?s)ðŸ"Š'; Replacement = '📊'},
    @{Pattern = '(?s)ðŸ"–'; Replacement = '📖'},
    @{Pattern = '(?s)ðŸ"''; Replacement = '📑'},
    @{Pattern = '(?s)ðŸ"‹'; Replacement = '📋'},
    @{Pattern = '(?s)ðŸŽ²'; Replacement = '🎲'},
    @{Pattern = '(?s)ðŸ¦'; Replacement = '🦅'},
    @{Pattern = '(?s)ðŸ'«'; Replacement = '👫'},
    @{Pattern = '(?s)ðŸ—.ï¸'; Replacement = '🗑️'},
    @{Pattern = '(?s)ðŸ"'; Replacement = '🔓'}
)

foreach ($file in $files) {
    Write-Host "Processing: $($file.Name)"
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalLength = $content.Length
    
    foreach ($fix in $fixes) {
        $content = $content -replace $fix.Pattern, $fix.Replacement
    }
    
    if ($content.Length -ne $originalLength) {
        Set-Content $file.FullName -Value $content -Encoding UTF8
        Write-Host "✅ Fixed: $($file.Name)"
    } else {
        Write-Host "No changes: $($file.Name)"
    }
}
