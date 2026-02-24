const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('d:/ToolsMatic/tools/quote-generator.html', 'utf8');
const tag = '<script>\r\n    const categories';
const startIdx = html.indexOf(tag);
const jsStart = startIdx + '<script>\r\n'.length;
const jsEnd = html.indexOf('</script>', jsStart);
const js = html.substring(jsStart, jsEnd);
const lines = js.split('\n');

// Binary search for first error line
let lo = 0, hi = lines.length - 1;
let lastOk = -1;

for (let i = 1; i < lines.length; i++) {
  const partial = lines.slice(0, i + 1).join('\n');
  try {
    new vm.Script(partial + '\n');
    lastOk = i;
  } catch (e) {
    if (!e.message.includes('Unexpected end of input') && 
        !e.message.includes('missing') &&
        !e.message.includes('not defined')) {
      console.log('ERROR at line ' + (i+1) + ':', e.message);
      console.log('Previous lines:');
      for (let j = Math.max(0, i-3); j <= Math.min(lines.length-1, i+2); j++) {
        console.log('  ' + (j+1) + ': ' + lines[j].trimEnd());
      }
      break;
    }
  }
}
