# ToolsMatic UUID Generator — VS Code Extension Guide

**Version:** 3.0.0  
**Last Updated:** January 2025  
**Status:** Production Ready

---

## 📦 Overview

The ToolsMatic UUID Generator VS Code extension brings enterprise-grade UUID generation directly into your code editor. Generate UUIDs (v1-v8), validate formats, parse fields, extract timestamps, and manage UUID history — all without leaving VS Code.

### ✨ Key Features

- **All UUID Versions**: Generate v1, v3, v4, v5, v6, v7, v8 UUIDs
- **Instant Generation**: Insert UUIDs at cursor with keyboard shortcuts
- **Validation & Parsing**: Hover tooltips show UUID version, timestamp, and validity
- **Bulk Generation**: Create thousands of UUIDs with one command
- **History Management**: Track and reuse previously generated UUIDs
- **Format Conversion**: Convert between standard, hex, base64, URN, binary formats
- **Timestamp Extraction**: Decode timestamps from v1/v6/v7 UUIDs
- **Team Sync**: Share UUID libraries across your development team
- **Dark/Light Theme**: Seamless integration with VS Code themes

---

## 🚀 Installation

### Method 1: VS Code Marketplace (Recommended)

1. Open VS Code
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
3. Search for "ToolsMatic UUID Generator"
4. Click **Install**

### Method 2: Quick Open

1. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (macOS)
2. Type: `ext install toolsmatic.uuid-generator`
3. Press Enter

### Method 3: Command Line

```bash
code --install-extension toolsmatic.uuid-generator
```

### Method 4: Manual Installation

1. Download `.vsix` file from [releases page](https://github.com/toolsmatic/uuid-vscode/releases)
2. In VS Code: `Ctrl+Shift+P` → "Install from VSIX..."
3. Select downloaded file

---

## ⌨️ Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Generate UUID v4 | `Ctrl+Shift+U` → `4` | `Cmd+Shift+U` → `4` |
| Generate UUID v7 | `Ctrl+Shift+U` → `7` | `Cmd+Shift+U` → `7` |
| Open UUID Panel | `Ctrl+Alt+U` | `Cmd+Opt+U` |
| Validate UUID | `Ctrl+Shift+V` → `U` | `Cmd+Shift+V` → `U` |
| UUID History | `Ctrl+Alt+H` | `Cmd+Opt+H` |
| Bulk Generate | `Ctrl+Shift+U` → `B` | `Cmd+Shift+U` → `B` |

### Customizing Shortcuts

1. Open Keyboard Shortcuts: `Ctrl+K Ctrl+S`
2. Search for "UUID"
3. Click pencil icon to customize

---

## 📖 Usage Guide

### 1. Generate UUID at Cursor

**Quick Insert:**
```
1. Place cursor where you want UUID
2. Press Ctrl+Shift+U
3. Select version (1-8)
4. UUID inserted instantly
```

**Example:**
```javascript
const userId = "f47ac10b-58cc-4372-a567-0e02b2c3d479"; // ← Generated with Ctrl+Shift+U → 4
```

### 2. Command Palette Usage

Press `Ctrl+Shift+P` (or `Cmd+Shift+P`) and type:

- `UUID: Generate v4` — Insert random UUID v4
- `UUID: Generate v7` — Insert time-ordered UUID v7
- `UUID: Generate v1` — Insert timestamp UUID v1
- `UUID: Generate v3 (MD5)` — Create namespace-based UUID
- `UUID: Generate v5 (SHA-1)` — Create SHA-1 namespace UUID
- `UUID: Validate Selected` — Check if selected text is valid UUID
- `UUID: Parse Selected` — Show UUID details (version, timestamp, fields)
- `UUID: Format Convert` — Change UUID format (hex, base64, URN, etc.)
- `UUID: Show History` — View all generated UUIDs in current session
- `UUID: Bulk Generate` — Create multiple UUIDs at once

### 3. UUID Panel (Side Panel)

**Open Panel:** `Ctrl+Alt+U` or click UUID icon in Activity Bar

**Panel Features:**
- Version selector dropdown
- One-click generation
- Format converter
- UUID history list (last 100)
- Validation input
- Timestamp decoder
- Collision probability calculator
- Quick actions toolbar

### 4. Hover Tooltips

**Hover over any UUID** in your code to see:
- ✅ Valid/Invalid status
- 📊 Version (v1-v8)
- ⏱️ Timestamp (for v1/v6/v7)
- 🔧 Field breakdown
- 📋 Quick actions (Copy, Parse, Convert)

**Example:**
```typescript
const id = "018d5c7f-3b1a-7000-8000-123456789abc";
//       ↑ Hover shows: "UUID v7 | Timestamp: 2025-01-15T10:30:00Z"
```

### 5. Bulk Generation

**Command Palette:**
1. `Ctrl+Shift+P` → `UUID: Bulk Generate`
2. Enter quantity (1 - 10,000)
3. Select version and format
4. UUIDs inserted as array or list

**Output Options:**
- JavaScript array: `["uuid1", "uuid2", ...]`
- JSON array: `["...", "..."]`
- Plain list (one per line)
- CSV format: `uuid,timestamp`
- SQL INSERT statements

**Example Output:**
```javascript
const uuids = [
  "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "a3b12f90-1234-4abc-8def-0123456789ab",
  "7c9e6679-7425-40de-944b-e07fc1f90ae7"
];
```

### 6. UUID Validation

**Select UUID text** → Right-click → "Validate UUID"

**Or use Command Palette:**
1. Select UUID string
2. `Ctrl+Shift+P` → `UUID: Validate Selected`
3. View validation result in notification

**Validation Checks:**
- RFC 4122 format compliance
- Version field correctness
- Variant field correctness
- Character set validity
- Length verification

### 7. UUID Parsing & Analysis

**Select UUID** → `Ctrl+Shift+P` → `UUID: Parse Selected`

**Parse Output Example:**
```
UUID: 018d5c7f-3b1a-7000-8000-123456789abc
├─ Version: v7 (Unix epoch time-ordered)
├─ Variant: RFC 4122
├─ Timestamp: 2025-01-15T10:30:00.000Z
├─ Fields:
│  ├─ unix_ts_ms: 1736938200000
│  ├─ rand_a: 3b1a
│  ├─ rand_b: 0000123456789abc
└─ Valid: ✓ Yes
```

### 8. Format Conversion

**Select UUID** → Right-click → "Convert UUID Format"

**Available Formats:**
- **Standard**: `f47ac10b-58cc-4372-a567-0e02b2c3d479`
- **Hex**: `0xf47ac10b58cc4372a5670e02b2c3d479`
- **Base64**: `9HrBC1jMQ3KlZw4CssP0eQ==`
- **URN**: `urn:uuid:f47ac10b-58cc-4372-a567-0e02b2c3d479`
- **Binary**: `11110100 01111010 11000001 ...`
- **No Hyphens**: `f47ac10b58cc4372a5670e02b2c3d479`

### 9. Timestamp Extraction

**For v1/v6/v7 UUIDs:**

Select UUID → `Ctrl+Shift+P` → `UUID: Extract Timestamp`

**Output:**
```
UUID: 018d5c7f-3b1a-7000-8000-123456789abc
Timestamp: 2025-01-15T10:30:00.000Z
Epoch: 1736938200000
Version: v7
Time Source: Unix epoch milliseconds
```

### 10. UUID History

**View History:** `Ctrl+Alt+H` or click "History" in UUID Panel

**Features:**
- Last 100 generated UUIDs
- Searchable and filterable
- Copy any UUID with one click
- Export history as JSON/CSV
- Clear history option
- Pin favorites

**History Panel:**
```
┌─────────────────────────────────────────────────────────┐
│ UUID History (100)                           [Clear All]│
├─────────────────────────────────────────────────────────┤
│ 🕐 10:30:15  v7  018d5c7f-3b1a-7000-8000-1234...  📋 ⭐│
│ 🕐 10:28:43  v4  f47ac10b-58cc-4372-a567-0e02...  📋  │
│ 🕐 10:25:12  v1  6ba7b810-9dad-11d1-80b4-00c0...  📋 ⭐│
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Configuration

### Settings

Open Settings (`Ctrl+,`) and search for "UUID":

```json
{
  // Default UUID version for quick generate
  "toolsmatic.uuid.defaultVersion": "v4",
  
  // Auto-lowercase generated UUIDs
  "toolsmatic.uuid.lowercase": true,
  
  // Include hyphens in generated UUIDs
  "toolsmatic.uuid.includeHyphens": true,
  
  // Default format for bulk generation
  "toolsmatic.uuid.bulkFormat": "array",
  
  // Maximum history items to store
  "toolsmatic.uuid.historyLimit": 100,
  
  // Show validation tooltips on hover
  "toolsmatic.uuid.hoverValidation": true,
  
  // Namespace for v3/v5 generation
  "toolsmatic.uuid.defaultNamespace": "dns",
  
  // Auto-copy generated UUID to clipboard
  "toolsmatic.uuid.autoCopy": false,
  
  // Enable team sync (requires login)
  "toolsmatic.uuid.teamSync": false,
  
  // Collision probability warnings
  "toolsmatic.uuid.collisionWarnings": true
}
```

### Full Settings Reference

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `defaultVersion` | string | `"v4"` | Version for quick generate (v1-v8) |
| `lowercase` | boolean | `true` | Generate lowercase UUIDs |
| `includeHyphens` | boolean | `true` | Include hyphens in output |
| `bulkFormat` | string | `"array"` | Format: array, list, json, csv, sql |
| `historyLimit` | number | `100` | Max history items (10-1000) |
| `hoverValidation` | boolean | `true` | Show hover tooltips |
| `defaultNamespace` | string | `"dns"` | Namespace: dns, url, oid, x500 |
| `autoCopy` | boolean | `false` | Auto-copy to clipboard |
| `teamSync` | boolean | `false` | Enable team synchronization |
| `collisionWarnings` | boolean | `true` | Warn about collision probability |
| `timestampFormat` | string | `"iso"` | Timestamp format: iso, unix, relative |
| `validationSound` | boolean | `false` | Play sound on validation failure |

---

## 🎯 Advanced Features

### Team Synchronization

**Setup:**
1. Sign in to ToolsMatic account
2. Enable `toolsmatic.uuid.teamSync` in settings
3. Share UUID libraries with team members
4. Track team UUID generation statistics

**Benefits:**
- Shared UUID namespace management
- Team-wide collision tracking
- Centralized UUID history
- Usage analytics dashboard

### Code Snippets

**Built-in Snippets:**

Type these prefixes and press `Tab`:

- `uuid4` → `"${uuid4}"`
- `uuid7` → `"${uuid7}"`
- `uuidvar` → `const uuid = require('uuid'); const id = uuid.v4();`
- `uuidts` → `import { v4 as uuidv4 } from 'uuid';`

### Multi-Cursor Support

**Generate unique UUID for each cursor:**
1. Create multiple cursors (`Alt+Click`)
2. Press `Ctrl+Shift+U` → `4`
3. Each cursor gets unique UUID

**Example:**
```javascript
const user1 = "018d5c7f-3b1a-7000-8000-123456789abc";
const user2 = "018d5c7f-4c2b-7000-8000-234567890bcd";
const user3 = "018d5c7f-5d3c-7000-8000-345678901cde";
// All generated simultaneously with multi-cursor
```

### Workspace-Specific Settings

**Per-project configuration:**

Create `.vscode/settings.json` in project root:

```json
{
  "toolsmatic.uuid.defaultVersion": "v7",
  "toolsmatic.uuid.bulkFormat": "sql",
  "toolsmatic.uuid.teamSync": true
}
```

### Language-Specific Integration

**Automatic format detection:**

Extension detects language and formats accordingly:

```javascript
// JavaScript/TypeScript — quotes added
const id = "f47ac10b-58cc-4372-a567-0e02b2c3d479";
```

```python
# Python — quotes added
user_id = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
```

```go
// Go — formatted as string
userID := "f47ac10b-58cc-4372-a567-0e02b2c3d479"
```

```sql
-- SQL — formatted for INSERT
INSERT INTO users (id) VALUES ('f47ac10b-58cc-4372-a567-0e02b2c3d479');
```

---

## 🔧 Troubleshooting

### Common Issues

**Issue: Keyboard shortcut not working**
- **Solution**: Check for conflicts in Keyboard Shortcuts (`Ctrl+K Ctrl+S`)
- Reassign shortcut if needed

**Issue: Hover tooltips not showing**
- **Solution**: Enable `toolsmatic.uuid.hoverValidation` in settings
- Restart VS Code

**Issue: Invalid UUIDs generated**
- **Solution**: Clear cache with `Ctrl+Shift+P` → "Developer: Reload Window"
- Update extension to latest version

**Issue: History not saving**
- **Solution**: Check workspace storage permissions
- Increase `historyLimit` if at maximum

**Issue: Team sync not connecting**
- **Solution**: Verify internet connection
- Re-authenticate: `UUID: Sign In to ToolsMatic`

### Performance Optimization

For large-scale UUID generation:

```json
{
  "toolsmatic.uuid.historyLimit": 50,  // Reduce history
  "toolsmatic.uuid.hoverValidation": false,  // Disable hover
  "toolsmatic.uuid.autoCopy": false  // Disable auto-copy
}
```

### Diagnostic Mode

**Enable logging:**
```json
{
  "toolsmatic.uuid.debug": true
}
```

View logs: `Ctrl+Shift+P` → "Developer: Show Logs" → "Extension Host"

---

## 📚 API Reference

### Extension API (for other extensions)

```typescript
import * as vscode from 'vscode';

// Get UUID extension API
const uuidExt = vscode.extensions.getExtension('toolsmatic.uuid-generator');
if (uuidExt) {
  const api = uuidExt.exports;
  
  // Generate UUID
  const uuid = api.generate('v7');
  
  // Validate
  const isValid = api.validate('f47ac10b-58cc-4372-a567-0e02b2c3d479');
  
  // Parse
  const info = api.parse('018d5c7f-3b1a-7000-8000-123456789abc');
  console.log(info.version); // "v7"
  console.log(info.timestamp); // Date object
  
  // Bulk generate
  const batch = api.bulk(1000, 'v4');
  
  // Convert format
  const hex = api.convert(uuid, 'hex');
}
```

---

## 🎓 Best Practices

### When to Use Each Version

- **v1**: Timestamp-based, includes MAC address (privacy concern)
- **v3**: MD5 namespace-based, deterministic but collision-prone
- **v4**: Random, most widely supported, industry standard
- **v5**: SHA-1 namespace-based, deterministic and secure
- **v6**: Reordered v1, better for database sorting
- **v7**: **Recommended** — Unix timestamp + random, sortable, modern
- **v8**: Custom/experimental formats

### Database Primary Keys

**Best choice: UUID v7**

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid_v7(),
  -- Benefits: Time-ordered for B-tree index efficiency
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### Distributed Systems

**Use v7 for:**
- Microservices IDs
- Event sourcing event IDs
- Message queue correlation IDs
- Distributed tracing span IDs

**Why v7:**
- Sortable by creation time
- Database index-friendly
- No coordination needed
- Millisecond precision

### Code Review Guidelines

**✅ Good:**
```typescript
const orderId = uuidv7(); // Time-ordered, sortable
```

**❌ Avoid:**
```typescript
const orderId = Math.random().toString(); // Not a UUID, collisions possible
```

---

## 🔐 Security & Privacy

### Data Privacy

- **Zero Telemetry**: No usage data collected
- **Local Processing**: All generation happens client-side
- **No Network Calls**: Works 100% offline
- **Private History**: Stored only in workspace storage

### Cryptographic Security

- **v4**: Uses `crypto.randomUUID()` or `crypto.getRandomValues()`
- **122-bit randomness**: Collision probability < 10^-36
- **CSPRNG**: Cryptographically secure pseudo-random number generator

### Best Practices

1. **Never use UUIDs as secrets**: They are identifiers, not passwords
2. **v1 leaks MAC address**: Prefer v7 for privacy
3. **Deterministic UUIDs (v3/v5)**: Use only when needed (idempotency)
4. **Validate untrusted input**: Always validate UUIDs from external sources

---

## 🌟 Contributing

We welcome contributions to the VS Code extension!

**Repository:** https://github.com/toolsmatic/uuid-vscode

**Report Issues:** https://github.com/toolsmatic/uuid-vscode/issues

**Feature Requests:** https://github.com/toolsmatic/uuid-vscode/discussions

### Development Setup

```bash
# Clone repository
git clone https://github.com/toolsmatic/uuid-vscode.git
cd uuid-vscode

# Install dependencies
npm install

# Run extension in debug mode
# Press F5 in VS Code
```

---

## 📜 License

MIT License — Free for personal and commercial use

---

## 📞 Support

- **Documentation**: https://toolsmatic.me/docs/uuid-vscode
- **Discord Community**: https://discord.gg/toolsmatic
- **Email**: support@toolsmatic.me
- **GitHub Issues**: https://github.com/toolsmatic/uuid-vscode/issues

---

## 🎉 Changelog

### v3.0.0 (2025-01-15)
- ✨ Added UUID v6, v7, v8 support
- 🚀 Bulk generation up to 10,000 UUIDs
- 📊 UUID history panel with search
- 🎨 Improved hover tooltips with timestamp extraction
- ⚡ Performance optimizations (5x faster)
- 🔧 Team synchronization support
- 🌐 Multi-cursor support for unique UUIDs

### v2.5.0 (2024-12-01)
- Added format conversion (hex, base64, URN, binary)
- UUID validation improvements
- Timestamp extraction for v1 UUIDs
- Bug fixes and stability improvements

### v2.0.0 (2024-09-15)
- Complete UI redesign
- Side panel integration
- Bulk generation feature
- Enhanced keyboard shortcuts

---

**Made with ❤️ by the ToolsMatic team**

*Helping developers generate UUIDs faster and smarter*
