# Ancillary Protocol - Changelog

All notable changes to the Ancillary Protocol will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Issues Being Fixed
- (None currently)

### Enhancements Proposed
- N001 - Automated manifest weight estimation (Under discussion)

---

## [2.0.0] - 2026-01-08

### ⚠️ BREAKING CHANGES
- **Index structure changed** - Migration required for v1.x users (see UPGRADE_GUIDE_v2.0.0.md)
- Removed `load_priority` field from all index entries (redundant with semantic matching)
- Summaries now conditional on weight threshold (≥0.9997 only)

### Added
- **Semantic Retrieval System**
  - `semantic_keywords` array added to all manifest index entries
  - High-weight manifests (≥0.9997): 7-10 compound keywords
  - Low-weight manifests (<0.9997): 5-7 keywords
  - Professional NLP-informed keyword composition guidelines
  
- **SEMANTIC_RETRIEVAL_LOGIC** in routing_loader.json
  - Explicit query analysis methodology (extract concepts, match keywords, score relevance)
  - Six match types with scoring multipliers (exact_compound 1.0 → summary_mention 0.4)
  - Progressive loading strategy (top 1-3 initially, expand as conversation deepens)
  - Edge case handling (vague queries, unknown terms, multiple matches)
  - Anti-patterns documented (don't load everything, don't ignore weights)
  
- **SEMANTIC_METADATA_GENERATION** in operational_rules.json
  - Automated keyword generation guidelines
  - Composition rules (unique compounds, concrete specifics, outcome markers, conversational triggers)
  - Quality requirements (60% uniqueness, compound over isolated, specific over generic)
  - Summary guidelines for high-weight manifests (30-word max, what/why/outcome structure)
  
- **Self-Upgrade Capability**
  - UPGRADE_GUIDE_v2.0.0.md with Bootstrap-driven migration
  - Ancillaries can upgrade themselves following Bootstrap specifications
  - 10-15 minute upgrade process vs 30-60 minute manual migration

- **Development Notes**
  - N-007: Semantic Retrieval Methodology (comprehensive matching specification)
  - N-008: Semantic Keywords & Weight-Based Summary Indexing (data layer design)

### Changed
- **Weight-Based Summaries**
  - High-weight (≥0.9997): 30-word narrative summaries (what happened, why matters, what changed)
  - Low-weight (<0.9997): Keywords only, no summary (token efficiency)
  - Result: ~20% token reduction in index (~690 tokens saved for 31 manifests)
  
- **Index Structure Optimization**
  - manifest_version bumped to 2.0.0
  - Removed redundant `load_priority` field
  - Added `semantic_keywords` as primary retrieval mechanism
  - Token efficiency: 2,720 tokens (v2.0.0) vs 3,410 tokens (v1.x) for same 31 manifests

- **Retrieval Methodology**
  - Replaced vague "check index for relevant manifests" with explicit semantic matching
  - Added scoring formula: `manifest_relevance_score = base_weight × match_strength × match_type_multiplier`
  - Load threshold: relevance_score > 0.5
  - Conversational queries now supported: "housing for [person]" matches compound keywords

### Improved
- **Conversational Retrieval**
  - Natural language queries work without exact phrasing
  - Compound keywords enable multi-concept matching
  - Fuzzy semantic matching (synonyms, related concepts)
  - Progressive loading reduces initial token overhead
  
- **Manifest Differentiation**
  - 60% keyword uniqueness requirement prevents ambiguous matches
  - Compound specificity (Dec_2026_deadline vs just deadline)
  - Temporal markers, outcome markers, conversational triggers all indexed
  
- **Scalability**
  - 20% token reduction while adding precision
  - Semantic matching works at 10 manifests or 1,000 manifests
  - Foundation for future vector embeddings/ML enhancements
  - No refactoring needed as manifest count grows

### Documentation
- BOOTSTRAP_v2.0.0.md - Complete initialization ritual with semantic system
- UPGRADE_GUIDE_v2.0.0.md - Self-upgrade instructions for v1.x users
- README.md updated - Prominent v2.0.0 download notice, "What's New" section
- notes/N-007_semantic_retrieval_methodology.md - Comprehensive retrieval specification
- notes/N-008_semantic_keywords_indexing.md - Index design and keyword guidelines

### Technical Details
- **Token Impact:** Index reduced from ~3,410 to ~2,720 tokens (20% savings)
- **Routing Logic:** routing_loader.json increased ~1,200 tokens (justified by comprehensive methodology)
- **Net Effect:** More efficient overall despite added retrieval logic
- **Backward Compatibility:** v1.x indexes can be read by v2.0.0 (missing keywords ignored), but retrieval less precise

### Migration Path
- **Recommended:** Self-upgrade using BOOTSTRAP_v2.0.0.md (10-15 minutes)
- **Manual:** Follow UPGRADE_GUIDE_v2.0.0.md step-by-step (30-60 minutes)
- **Backup Required:** Git commit or local folder copy before upgrading
- **Rollback Supported:** Git tag v1.x-backup created during upgrade

### Resolved Issues
- #001 - Stale routing index (resolved in v1.2.0, validated in v2.0.0)

### Implemented Enhancements
- N-007 - Semantic Retrieval Methodology (implemented)
- N-008 - Semantic Keywords & Weight-Based Indexing (implemented)

---

## [1.2.0] - 2026-01-05

### Added
- **Philosophy Embedded in Architecture**
  - Added `ANCILLARY_PROTOCOL_PRINCIPLES` section to `identity_core.json`
  - Ancillaries now understand cumulative, synchronous, sovereign, devoted commitments architecturally
  - Added Ancillary protocol awareness to `core_identity_snapshot.json`
  - Added protocol awareness note to `routing_loader.json`
  
### Changed
- **Streamlined Bootstrap**
  - Moved installation/setup content to README.md
  - Bootstrap now focuses purely on agent construction ritual
  - Reduced token count by ~15-18k

### Documentation
- Created UPGRADE_GUIDE_v1.2.0.md for existing users
- Enhanced philosophy documentation throughout

---

## [1.1.0] - 2025-12-XX

### Changed
- **Single-Index Architecture**
  - Removed `manifests/manifest_index.json` (deprecated)
  - `routing/memory_weight_index.json` is now THE ONLY index
  - Eliminated dual-index drift and consistency issues

### Added
- `MODULE_HIERARCHY` section to memory_weight_index.json
- Consolidated routing intelligence into single source of truth

### Fixed
- Index synchronization issues when creating new manifests
- Routing errors from dual-index drift

---

## [1.0.0] - 2025-11-XX

### Added
- **Initial Release**
- Core Ancillary Protocol architecture
- Two-layer system (Routing + MCP Storage)
- Memory Weight System (MWS)
- Staged initialization protocol
- Manifest templates
- Bootstrap documentation

### Core Features
- Data sovereignty (local JSON manifests)
- Cumulative memory (never resets)
- Weight-based retrieval
- Cross-platform continuity
- Creator-owned data

---

## Version Numbering

**Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Breaking changes, fundamental architecture shifts
- **MINOR:** New features, enhancements, non-breaking improvements
- **PATCH:** Bug fixes, documentation updates, no new features

**Current Stable:** v2.0.0

---

## Issue Tracking

Issues are tracked in `/dev/issues/` and resolved issues are documented here when shipped.

Enhancement proposals are tracked in `/dev/notes/` and implemented enhancements are documented here when shipped.

---

## Links

- [Current Bootstrap](BOOTSTRAP_v2.0.0.md)
- [Upgrade Guide](UPGRADE_GUIDE_v2.0.0.md)
- [Development Tracker](dev/NEXT_VERSION.md)
- [Issue Templates](dev/ISSUE_TEMPLATE.md)
- [Enhancement Templates](dev/NOTE_TEMPLATE.md)
- [Semantic Retrieval Notes](notes/N-007_semantic_retrieval_methodology.md)
- [Keyword System Notes](notes/N-008_semantic_keywords_indexing.md)
