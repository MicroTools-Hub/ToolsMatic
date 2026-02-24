# ToolsMatic Regex Tester — VS Code Extension Integration Guide

## Quick Integration (5 minutes)

The ToolsMatic Regex Tester is now available for direct integration with VS Code. Test and debug regex patterns without leaving your editor.

## Installation Methods

### Method 1: Web View Extension (Recommended)
Create a lightweight VS Code extension that opens the regex tester in a side panel.

```javascript
// extension.js
const vscode = require('vscode');

module.exports = {
  activate(context) {
    const provider = new RegexTesterWebviewProvider(context.extensionUri);
    context.subscriptions.push(
      vscode.window.registerWebviewPanelSerializer('regexTester.panel', provider)
    );
    
    context.subscriptions.push(
      vscode.commands.registerCommand('regexTester.open', () => {
        provider.showPanel();
      })
    );
  }
};

class RegexTesterWebviewProvider {
  constructor(extensionUri) {
    this.extensionUri = extensionUri;
  }
  
  async showPanel() {
    const panel = vscode.window.createWebviewPanel(
      'regexTester',
      'Regex Tester',
      vscode.ViewColumn.Beside,
      { enableScripts: true }
    );
    
    panel.webview.html = `
      <iframe src="https://toolsmatic.me/tools/regex-tester.html" 
              style="width:100%;height:100%;border:none;"></iframe>
    `;
  }
}
```

### Method 2: Command Palette Integration
Add a command to quickly test selected text as a regex pattern.

```javascript
vscode.commands.registerCommand('regexTester.testSelection', async () => {
  const editor = vscode.window.activeTextEditor;
  if (!editor) return;
  
  const selection = editor.document.getText(editor.selection);
  const pattern = encodeURIComponent(selection);
  vscode.env.openExternal(vscode.Uri.parse(
    `https://toolsmatic.me/tools/regex-tester.html?pattern=${pattern}`
  ));
});
```

### Method 3: Hover Tooltips
Show pattern validation hints on hover for regex patterns.

```javascript
const hoverProvider = vscode.languages.registerHoverProvider('regex', {
  provideHover(document, position) {
    const wordRange = document.getWordRangeAtPosition(position);
    const word = document.getText(wordRange);
    
    // Call our validation API
    return fetch(`https://toolsmatic.me/api/regex/validate?pattern=${encodeURIComponent(word)}`)
      .then(r => r.json())
      .then(data => new vscode.Hover(
        `**Pattern Score:** ${data.score}/100\n\n${data.feedback}`
      ));
  }
});
```

## Official Extension Package via Marketplace

Search for **"ToolsMatic Regex Tester"** in the VS Code Extensions Marketplace.

**Extension ID:** `toolsmatic.regex-tester`

### Features
- 🔍 Test patterns in side panel without context switching
- ⚡ Real-time validation as you type in editor
- 📊 Pattern scoring and efficiency analysis
- 🏆 Challenge mode integration—compete in regex golf
- 🎯 Capture group highlighting in side panel
- 📋 Copy pattern as `/pattern/flags` to clipboard
- 🌍 Leaderboard integration—share your best patterns
- 🎖️ Achievement badges earned in VS Code

### Installation
```bash
code --install-extension toolsmatic.regex-tester
```

## API Integration

### Validate Pattern Endpoint
```bash
POST https://toolsmatic.me/api/regex/validate
Content-Type: application/json

{
  "pattern": "(?<email>[a-z0-9._%+-]+)@[a-z0-9.-]+\\.[a-z]{2,}",
  "flags": "gi",
  "testText": "Contact: admin@toolsmatic.me"
}
```

**Response:**
```json
{
  "valid": true,
  "score": 85,
  "matchCount": 1,
  "groupCount": 1,
  "efficiency": "Great",
  "timeMs": 0.34,
  "feedback": "Well-optimized pattern with named groups."
}
```

### Challenge Submission Endpoint
```bash
POST https://toolsmatic.me/api/regex/challenge/submit
Content-Type: application/json
Authorization: Bearer {user_token}

{
  "challengeId": "golf_email_extract",
  "pattern": "([a-z]+)@[a-z.]+",
  "patternLength": 23,
  "testsPassed": 8,
  "testsTotal": 10
}
```

**Response:**
```json
{
  "success": true,
  "ranking": 42,
  "personalBest": 18,
  "achievement": "golfWin",
  "globalLeaderboardPosition": 127
}
```

## Keyboard Shortcuts for VS Code Integration

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+R` | Open Regex Tester panel |
| `Ctrl+Shift+T` | Test selected text in regex tester |
| `Ctrl+Shift+V` | Validate pattern at cursor |
| `Ctrl+Shift+C` | Copy pattern from tester |

## TypeScript Declaration Files

For full IDE support:

```typescript
// regex-tester.d.ts
declare module 'toolsmatic-regex-tester' {
  interface RegexTestResult {
    valid: boolean;
    score: number;
    matchCount: number;
    groupCount: number;
    timeMs: number;
    matches: RegexMatch[];
    compatibility: {
      javascript: boolean;
      python: boolean;
      pcre: boolean;
    };
  }

  interface RegexMatch {
    index: number;
    length: number;
    text: string;
    groups: Record<string, string>;
  }

  export function testPattern(
    pattern: string,
    flags: string,
    text: string
  ): Promise<RegexTestResult>;
}
```

## Community Integration

### Share Patterns with Team
Generate shareable links that automatically open in teammates' VS Code:

```
vscode://open?url=https://toolsmatic.me/tools/regex-tester.html?pattern=%28%3F%3Cemail%3E...
```

### Embed in Team Documentation
```markdown
<!-- In your team's regex patterns documentation -->
Test this pattern: [🔗 Open in Regex Tester](https://toolsmatic.me/tools/regex-tester.html?pattern=YOUR_PATTERN)
```

### GitHub Integration
Add regex pattern files to GitHub and link directly:

```markdown
**Pattern:** Email Validation
[Test in Regex Tester](https://toolsmatic.me/tools/regex-tester.html?pattern=...&source=github)
```

## Enterprise Features

### Single Sign-On (Auth0)
```javascript
const auth0 = new Auth0Client({
  domain: 'toolsmatic.auth0.com',
  client_id: 'YOUR_CLIENT_ID'
});

await auth0.loginWithPopup();
const token = await auth0.getTokenSilently();
```

### Team Leaderboards
Private leaderboards for your organization's DevOps/DevTools team.

### Regex Pattern Library
Share approved regex patterns across your enterprise instance.

## Troubleshooting

### Extension Won't Open in Side Panel
1. Ensure VS Code is updated to latest version
2. Try: `Developer: Reload Window` (Ctrl+R)
3. Check firewall isn't blocking `toolsmatic.me`

### Pattern Not Validating
1. Verify JavaScript RegExp syntax (not PCRE/Python specific)
2. Check that flags are valid: `gimsuvy`
3. Try: `Clear Cache` in VS Code settings

### Missing Achievements
- Achievements sync via localStorage
- Clear browser cache if badges aren't showing
- Try logging out/in if using team dashboard

## Advanced: Custom Extension

Create your own branded regex tester for your organization:

```javascript
// Proxy VS Code Regex Tester through your backend
app.get('/api/test-regex', async (req, res) => {
  const { pattern, flags, text } = req.query;
  const result = await toolsmaticClient.testPattern(pattern, flags, text);
  
  // Add org-specific metadata
  result.org = 'acme-corp';
  result.team = req.user.team;
  
  res.json(result);
});
```

## Support & Feedback

**Report Issues:** [github.com/toolsmatic/regex-tester-vscode/issues](https://github.com/toolsmatic/regex-tester-vscode/issues)

**Feature Requests:** Use VS Code Extension community discussions

**Direct Support:** support@toolsmatic.me

---

**Version:** 2.0.0 | **Updated:** February 2026 | **Maintained by:** ToolsMatic Team
