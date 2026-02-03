# Script to replace native banner ads with 2x banner ads

$replacement = @'
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
'@

$pattern = '\s*<script async="async" data-cfasync="false" src="https://pl28604956\.effectivegatecpm\.com/ec3790ad17aa114a9ec21293450604cc/invoke\.js"></script>\s*<div id="container-ec3790ad17aa114a9ec21293450604cc"></div>\s*'

Write-Host "Starting replacement in tools directory..."

$files = Get-ChildItem -Path "D:\ToolsMatic\tools\*.html"
$totalReplaced = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    $count = ([regex]::Matches($content, 'ec3790ad17aa114a9ec21293450604cc')).Count
    
    if ($count -gt 0) {
        $newContent = $content -replace $pattern, $replacement
        $newCount = ([regex]::Matches($newContent, 'ec3790ad17aa114a9ec21293450604cc')).Count
        Set-Content -Path $file.FullName -Value $newContent -NoNewline
        $totalReplaced += $count
        Write-Host "$($file.Name): Replaced $count native ads (verified: $newCount remaining should be 0)"
    }
}

Write-Host "`nTotal: Replaced $totalReplaced native ads across all tool files"
Write-Host "Complete!"
