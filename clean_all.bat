@echo off
REM This script removes orphaned atOptions blocks from all HTML files

cd /d "d:\ToolsMatic\tools"

for %%f in (*.html) do (
    powershell -Command "$content = [System.IO.File]::ReadAllText('%%f'); $content = $content -replace '<div style=\"text-align: center; margin: 24px 0;\">\s*</div>', ''; $content = $content -replace '<script>\s*atOptions\s*=\s*\{[^}]*\};\s*</script>', ''; $content = $content -replace '<div style=\"text-align: center; margin: 24px 0;\">\s*<script>\s*atOptions\s*=\s*\{[^}]*\};\s*</script>\s*\s*</div>', ''; [System.IO.File]::WriteAllText('%%f', $content)"
)

echo Done cleaning all files
