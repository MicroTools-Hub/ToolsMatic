const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('d:/ToolsMatic/tools/quote-generator.html', 'utf8');
const tag = '<script>\r\n    const categories';
const startIdx = html.indexOf(tag);
console.log('Script start index:', startIdx);

if (startIdx < 0) {
  console.log('Could not find script tag');
  process.exit(1);
}

const jsStart = startIdx + '<script>\r\n'.length;
const jsEnd = html.indexOf('</script>', jsStart);
console.log('JS end index:', jsEnd);

const js = html.substring(jsStart, jsEnd);
console.log('JS length:', js.length);
console.log('First 200 chars:', js.substring(0, 200));
console.log('Last 200 chars:', js.substring(js.length - 200));

try {
  new vm.Script(js);
  console.log('SYNTAX: OK');
} catch (err) {
  console.log('SYNTAX ERROR:', err.message);
  // Find the line
  const lines = js.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes("'") && lines[i].split("'").length % 2 === 0) {
      // Odd number of single quotes - might be unescaped
      console.log('Suspicious line ' + (i+1) + ':', lines[i].trim().substring(0, 100));
    }
  }
}
