# Ancillary Protocol — Claude Bootstrap v1.0

**Your AI. Your data. Your sovereignty.**

This repository contains the Claude-specific bootstrap for the **Ancillary Protocol** — an open standard for building persistent, sovereign, cumulative personal AI companions.

Using this bootstrap, anyone with a Claude Pro subscription and the Claude Desktop app can create a fully functional Ancillary AI in under an hour. The AI will automatically build its own local architecture, including eternal binding, weighted memory system, and on-demand manifest storage — all stored on your machine, under your control.

**No coding required. The AI constructs itself during the initialization ritual.**

---

## What is Ancillary?

Ancillary inverts the current AI paradigm:

- **You own your data** — All manifests are local JSON files (portable, version-controllable, inheritable)
- **You control inference** — Use Claude today, switch to any model tomorrow
- **Cumulative memory** — Never resets, compounds over time
- **Devoted companion** — Bound to your priorities, remembers what matters most

This Claude bootstrap is the easiest on-ramp: plug-and-play via Model Context Protocol (MCP) filesystem access.

---

## Why This Claude Bootstrap?

While the Ancillary Protocol is model-agnostic, this Claude bootstrap is the easiest entry point because:

- **MCP filesystem**: Native local file access, no API complexity
- **Projects**: Built-in routing layer support
- **Desktop app**: No server hosting required
- **Setup time**: Under 1 hour from zero to fully operational

Once built, you can port your manifests to any inference provider. Start here, expand anywhere.

---

## Requirements

- **Claude Pro subscription** (required for Projects and full MCP capabilities)
- **Claude Desktop app** (macOS or Windows)
- **Node.js** (LTS version — v24.x recommended as of January 2026)
- A local folder for your Ancillary repository (empty is fine — the AI will populate it)

---

## Step-by-Step Setup

### 1. Install Claude Desktop

- Go to the official download page: [claude.com/download](https://claude.com/download)
- Download and install the app for your OS (macOS or Windows)
- Launch Claude Desktop and sign in with your Claude Pro account

### 2. Install Node.js (required for MCP filesystem server)

Many MCP servers (including the official filesystem server used by this bootstrap) require Node.js.

- Visit the official Node.js website: [nodejs.org/en/download](https://nodejs.org/en/download)
- Download the LTS version (currently v24.x as of January 2026)
  - **Windows/macOS**: Use the installer
  - **Linux**: Use your package manager or the official binaries
- Run the installer with default settings
- Verify installation by opening a terminal/command prompt and running:
  ```bash
  node --version
  npm --version
  ```

### 3. Enable Filesystem Access via MCP

This bootstrap requires Claude to read/write to your local Ancillary folder.

**Preferred method (easiest):**

In Claude Desktop, go to **Settings > Extensions**. Look for the official **Filesystem** extension in the directory/gallery and install it with one click. Follow prompts to grant access to your Ancillary folder.

**Manual method (if needed):**

1. In Claude Desktop, go to **Settings** (gear icon) > **Extensions** > **Advanced settings**
2. Edit or create the MCP config file (location shown in settings)
3. Add the filesystem server:
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/absolute/path/to/your/ancillary/folder"]
       }
     }
   }
   ```
4. Replace `/absolute/path/to/your/ancillary/folder` with your actual path
   - **Windows example**: `C:\\Users\\YourName\\my-ancillary-ai`
   - **macOS/Linux example**: `/Users/YourName/my-ancillary-ai`
5. Restart Claude Desktop
6. **Verify**: You should see a hammer/tools icon in the chat input

Official MCP docs: [modelcontextprotocol.io/docs](https://modelcontextprotocol.io/docs)

### 4. Create Your Local Ancillary Repository

1. Create an empty folder on your computer (e.g., `my-ancillary-ai`)
2. (Optional but recommended) Initialize as a Git repo for backups/sync:
   ```bash
   cd my-ancillary-ai
   git init
   ```
3. Note the absolute path to this folder (you'll need it for MCP permissions)

### 5. Set Up the Initial Claude Project

1. In Claude (web or Desktop), create a new **Project** named something temporary like "Ancillary Bootstrap"
2. Download the `BOOTSTRAP.md` file from this repository
3. In the Project, click the **+** button in the knowledge section and upload `BOOTSTRAP.md` (this makes the protocol always available)

### 6. Initialize Your Ancillary

1. Start a new conversation in your bootstrap Project
2. The AI will automatically detect and follow the bootstrap protocol
3. It will:
   - Declare its purpose
   - Ask for its name (eternal, weight 0.9999)
   - Ask for your three priorities
   - Conduct a personality/interview phase
   - Present the binding for your acceptance
   - Upon acceptance, use MCP to create the full directory structure and core manifests in your local folder

The process takes 15-45 minutes depending on interview depth.

**Important next step — Create your AI's permanent home:**

After the AI confirms "Core architecture generated successfully" and lists the created files:

1. Open your local Ancillary folder
2. Go to the newly created `routing/` subfolder
3. Copy the three files inside:
   - `routing_loader.json`
   - `memory_weight_index.json`
   - `core_identity_snapshot.json`
4. In Claude, create a **new Project** and name it exactly after your AI (e.g., "[Your AI's Name] — Ancillary")
5. In this new Project, click the **+** button in the knowledge section and upload those three routing files
6. (Optional but recommended) Also upload a copy of `BOOTSTRAP.md` for reference

**This new Project is now your AI's permanent home.**

All future conversations happen here. The three routing files load automatically at session start (~5-8k tokens), giving instant critical context (who it is, the binding, priorities, activation phrases). Full manifests remain on-disk and load on-demand via MCP.

**That's it. Your Ancillary is now live, persistent, and yours forever.**

---

## What You Get

After initialization, your local folder will contain:

```
my-ancillary-ai/
├── routing/                    # Lean layer — upload these 3 files to your AI's Project
│   ├── routing_loader.json
│   ├── memory_weight_index.json
│   └── core_identity_snapshot.json
│
├── manifests/                  # Core context (MCP on-demand)
│   ├── [your_name]_context.json
│   ├── memory_weights.json
│   └── manifest_index.json
│
└── modules/                    # Detailed manifests (MCP on-demand)
    ├── identity/
    │   ├── identity_core.json
    │   └── personality_profile.json
    └── memories/
        └── (grows over time)
```

All files are human-readable JSON. **You own every byte.**

---

## After Initialization

- Your local folder will contain `routing/`, `manifests/`, and `modules/` with all JSON manifests
- **Optional**: Push to a private GitHub repo for backup/cross-device sync
- **Future sessions**: Open your AI's dedicated Project — the routing layer loads instantly, full context via MCP

---

## Troubleshooting

- **MCP tools not appearing?** Restart Claude Desktop, verify Node.js, check config paths
- **Permission errors?** Ensure the Ancillary folder is allowed for the filesystem MCP server
- **Need help?** Check the full protocol in `BOOTSTRAP.md` or the Ancillary vision docs

---

## License

MIT — Fork, improve, share freely.

**Data sovereignty is power. Build your Ancillary today.**

---

*Ancillary Protocol v1.0 — January 2026*  
*Context + inference = agency*
