const fs = require('fs');
const h = fs.readFileSync('tools/quote-generator.html', 'utf-8');
const i1 = h.indexOf('const categories = {');
const i2 = h.indexOf('</script>', i1);
const js = h.substring(i1, i2);
const lines = js.split('\n');

console.log('Total JS lines:', lines.length);

// Find which line causes "Unexpected string" 
// This error means two string literals next to each other with no operator between them
// Common cause: missing comma between array elements

// Check for lines that end a string but have no comma
for (let i = 0; i < lines.length; i++) {
  const line = lines[i].trimEnd();
  // A quote string line should end with ', or '],
  if (line.match(/'$/) && !line.match(/,$/) && !line.match(/\[$/) && !line.match(/\{$/) && i > 0) {
    // This line ends with a quote but no comma
    const nextLine = (lines[i + 1] || '').trim();
    if (nextLine.startsWith("'") || nextLine.startsWith('"')) {
      console.log('MISSING COMMA at line ' + (i + 1) + ':');
      console.log('  > ' + line.substring(0, 150));
      console.log('  NEXT: ' + nextLine.substring(0, 150));
    }
  }
}

// Final full syntax check
console.log('Running full syntax check...');
try {
  new Function(js);
  console.log('FULL JS SYNTAX: OK');
} catch (e) {
  console.log('FULL JS SYNTAX ERROR: ' + e.message);
}
console.log('Done.');
