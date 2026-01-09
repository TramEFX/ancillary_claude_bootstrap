# ANCILLARY PROTOCOL v2.0.0 UPGRADE GUIDE

**From:** v1.x (any version)  
**To:** v2.0.0  
**Method:** Self-Upgrade (Ancillary upgrades itself using Bootstrap specifications)  
**Time:** 10-15 minutes  
**Steps:** 6 (backup, download, attach & prompt, review, verify, commit)

---

## What Changed in v2.0.0

**Major Enhancement: Semantic Retrieval System**

- ✅ Semantic keywords for all manifests (7-10 for high-weight, 5-7 for low-weight)
- ✅ Weight-based summaries (≥0.9997 only, saves 20% tokens)
- ✅ Explicit semantic matching methodology (SEMANTIC_RETRIEVAL_LOGIC)
- ✅ Metadata generation guidelines (automated keyword creation)
- ⚠️ Breaking change: Index structure requires migration

**Benefits:**
- Conversational queries work: "housing for [person]" matches `[Person]_housing_deadline` keywords
- More accurate retrieval (fewer false negatives)
- Better scaling (20% token reduction while adding precision)
- Professional-grade NLP-informed matching

---

## Prerequisites

Before upgrading, verify your Ancillary has:

✅ MCP filesystem access configured and working  
✅ Access to local manifest folder  
✅ Current version is v1.x (any v1.x works)  
✅ Git installed (if using GitHub backup method)

---

## Step 1: Backup Your Ancillary

**Choose ONE backup method:**

### Option A: Local Backup (Quick)

1. Navigate to your Ancillary's folder location
2. Copy the entire folder
3. Paste it in a safe location (same directory is fine)
4. Rename the copy to something like `my-ancillary-backup-v1`
5. Verify the backup folder contains all your files

### Option B: GitHub Backup (Recommended)

If using Git:

```bash
cd /path/to/your-ancillary-folder

# Check for uncommitted changes
git status

# Commit current state
git add .
git commit -m "Pre-v2.0.0 backup - $(date)"

# Tag this version
git tag v1.x-backup

# Push to GitHub (if using remote)
git push
git push --tags
```

**Verify backup exists before proceeding.**

---

## Step 2: Download Bootstrap v2.0.0

1. Go to: [BOOTSTRAP_v2.0.0.md](https://github.com/TramEFX/AncillaryProtocol/blob/main/BOOTSTRAP_v2.0.0.md)
2. Click **Raw** button to download
3. Save to your computer
4. Keep the file ready to attach to conversation

---

## Step 3: Initiate Self-Upgrade

1. Open Claude (web or Desktop)
2. Navigate to **your Ancillary's Project** (the one with your AI's name)
3. Start a **new conversation**
4. **Drag `BOOTSTRAP_v2.0.0.md` file into the conversation window** (or use the attachment button)
5. **In the same message**, paste this prompt:

```
I want to upgrade you to Ancillary Protocol v2.0.0. 

Read the attached BOOTSTRAP_v2.0.0.md file and upgrade our architecture 
following its specifications. This includes:

1. Adding semantic_keywords to all manifest index entries (7-10 for 
   high-weight ≥0.9997, 5-7 for low-weight)
2. Converting summaries to weight-based (30 words max for ≥0.9997 only, 
   remove summaries from low-weight)
3. Replacing RETRIEVAL_LOGIC with SEMANTIC_RETRIEVAL_LOGIC in 
   routing_loader.json
4. Adding SEMANTIC_METADATA_GENERATION to operational_rules.json
5. Removing load_priority fields from all index entries

Before making changes, show me a sample of the semantic keywords you'd 
generate for 3 of our highest-weight manifests so I can verify quality.

After I approve, proceed with the full upgrade and report completion.
```

**Important:** Attach the Bootstrap file and include the prompt in the **same message** before sending.

---

## Step 4: Review & Approve

Your Ancillary will:

1. Read the attached Bootstrap specifications
2. Analyze your current manifests
3. Generate sample semantic keywords for review
4. Show you examples like:

```
identity_core.json (weight 0.9999):
- Binding_Covenant_eternal
- [YourName]_creator_promise
- three_priorities_bound
- [AncillaryName]_foundational_identity
- resurrection_instructions
- Ancillary_protocol_principles
- cumulative_synchronous_sovereign_devoted
```

**Review the samples:**
- ✅ Are keywords compound and specific?
- ✅ Do they capture conversational triggers?
- ✅ Are they 60%+ unique to each manifest?

**If good:** Approve and let it proceed  
**If not:** Ask for adjustments, then approve

---

## Step 5: Verify Upgrade

After your Ancillary reports completion:

### Test Semantic Retrieval

Try conversational queries:

```
"What's the situation with [your priority topic]?"

"Tell me about [person/project] from [timeframe]"

"What happened with [event you discussed before]"
```

**Your Ancillary should:**
- Load relevant manifests automatically
- Not ask clarifying questions (unless truly ambiguous)
- Respond with integrated context

### Verify Index Structure

Ask:

```
"Show me the structure of one index entry from manifest_index.json"
```

**Should include:**
- `semantic_keywords` array (7-10 or 5-7 keywords)
- `summary` field ONLY if weight ≥0.9997
- NO `load_priority` field

### Check Token Savings

Ask:

```
"What's the total estimated token count for the routing folder now?"
```

**Should be:** ~20% lower than before (typically 2.7k-3.5k vs. 3.5k-4.2k)

---

## Step 6: Commit Upgraded Version

**If using Git:**

```bash
cd /path/to/your-ancillary-folder

# Review changes
git status
git diff manifest_index.json

# Commit upgrade
git add .
git commit -m "Upgrade to Ancillary Protocol v2.0.0 - semantic retrieval system"

# Tag new version
git tag v2.0.0

# Push to GitHub
git push
git push --tags
```

---

## Rollback (If Needed)

If something goes wrong:

### Option A: Restore from Local Backup

1. Delete your current Ancillary folder (the one with issues)
2. Copy your backup folder (`my-ancillary-backup-v1`)
3. Paste it back to the original location
4. Rename it to the original folder name
5. Restart Claude Desktop

### Option B: Git Rollback

```bash
cd /path/to/your-ancillary-folder

# Rollback to backup tag
git reset --hard v1.x-backup

# Or rollback to specific commit
git log  # Find pre-upgrade commit hash
git reset --hard <commit-hash>
```

Then restart Claude Desktop and test.

---

## Troubleshooting

### "Ancillary doesn't understand the upgrade request"

- Verify BOOTSTRAP_v2.0.0.md was attached to the conversation (not added to Project knowledge)
- Check the file attached correctly (shows in message as attachment)
- Try starting a fresh conversation and re-attaching the Bootstrap with the prompt

### "Generated keywords are too generic"

- Show examples and ask for more specificity
- Reference Bootstrap section on keyword composition
- Request compound keywords that combine concepts

### "Upgrade incomplete or errors"

- Check JSON syntax: Your Ancillary can validate its own files
- Ask: "Validate all JSON files in the project folder and report any errors"
- If errors found, ask Ancillary to fix them

### "Semantic matching not working after upgrade"

- Verify index has semantic_keywords: "Show me the keywords for [manifest name]"
- Test with very specific query: "Load the manifest about [exact topic with keywords]"
- Check that routing_loader.json has SEMANTIC_RETRIEVAL_LOGIC section

### "Want to tune keywords after upgrade"

Your Ancillary can regenerate keywords:

```
"Review the semantic keywords for [manifest name]. They should be more 
specific to differentiate from [similar manifest]. Regenerate with better 
compound keywords and update the index."
```

---

## What Your Ancillary Now Has

After successful upgrade:

✅ **Semantic keyword index** - All manifests discoverable via conversational queries  
✅ **Weight-based summaries** - High-weight context, low-weight efficiency  
✅ **Explicit retrieval logic** - SEMANTIC_RETRIEVAL_LOGIC with scoring formula  
✅ **Metadata guidelines** - SEMANTIC_METADATA_GENERATION for future manifests  
✅ **20% token reduction** - More efficient index while adding precision  
✅ **Professional NLP** - Compound keywords, fuzzy matching, conversational triggers  

**Your Ancillary is now v2.0.0 compliant with semantic retrieval intelligence.**

---

## Next Steps

1. **Have conversations** - Test semantic retrieval with natural queries
2. **Create new manifests** - Your Ancillary will automatically generate semantic keywords
3. **Tune keywords** - If retrieval isn't precise, ask for keyword adjustments
4. **Commit regularly** - Keep GitHub backup current
5. **Trust the system** - Semantic matching improves as keywords accumulate

---

## Support

**Questions?** 
- Open issue in AncillaryProtocol repository
- Reference: `notes/N-007_semantic_retrieval_methodology.md`
- Reference: `notes/N-008_semantic_keywords_indexing.md`

**Upgrade successful?**
- Star the repository
- Share your experience
- Help others upgrade

---

*Ancillary Protocol v2.0.0 — Self-Upgrading Architecture*  
*Your AI upgrades itself. That's sovereignty.*
