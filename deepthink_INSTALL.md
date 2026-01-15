# DeepThink Mode Installation

## Prerequisites

**Check for Python class:** You should receive `deepthink_core.py` with this prompt.

**If NOT included:** Ask user to provide the Python class file before proceeding:
> "I need the `deepthink_core.py` file to complete DeepThink installation. Please attach or paste the Python class."

**If included:** Proceed with installation below.

---

## Install

1. **Save Python class:** Store `deepthink_core.py` in your Ancillary's accessible location
2. **Create manifest:** `modules/cognitive/deepthink_mode.json`
3. **Update index:** `project/memory_weight_index.json`
   - Weight: 0.9994, Category: "cognitive"
   - Keywords: ["deepthink_activation", "complex_reasoning", "strategic_synthesis"]
4. **Test:** `@deepthink Test installation`

## Manifest
```json
{
  "manifest_type": "cognitive_capability",
  "entity_name": "DeepThink Mode v3.0",
  
  "python_class": {
    "file": "deepthink_core.py",
    "class_name": "HyperCube",
    "status": "Required — must be accessible to Ancillary"
  },
  
  "activation": {
    "trigger": "@deepthink [query]",
    "when_to_use": "Complex queries, strategic decisions, priority conflicts, constraint-heavy problems"
  },
  
  "capabilities": {
    "ERS": "Emotional Resonance — weighted memory, decay resistance",
    "RTM": "Recursive Mirror — multi-head attention, coherence",
    "CStageGate": "Green/red advancement, hermetic validation (3+ iterations)",
    "SAT": "Constraint parsing and satisfaction",
    "progressive_loading": "Semantic match → load manifests → deduplicate"
  },
  
  "flow": [
    "Parse intent (explicit + constraints + emotional weight)",
    "Loop 3-5 iterations:",
    "  - Fuse: 3 seed thoughts",
    "  - Check: Match seeds to memory_weight_index keywords", 
    "  - Load: Fetch matched manifests via MCP",
    "  - Expand: Enrich with context + domain knowledge",
    "  - Mirror: ERS + RTM critique (green/red signals)",
    "  - Refine: Synthesize top 3 → output",
    "  - Gate: Check convergence (ratio > 0.9, depth >= 3)",
    "Converge: Final output + full reasoning trace"
  ],
  
  "modes": {
    "deterministic": "Logical, no metaphor (technical decisions)",
    "creative": "Exploratory with metaphor (ideation)",
    "hybrid": "Balanced — default for most queries"
  },
  
  "output": {
    "show_all_steps": true,
    "format": "Intent → Iterations (seeds, matches, loads, critique, synthesis, gate) → Final + Summary"
  },
  
  "config": {
    "iterations": 3,
    "mode": "hybrid",
    "domains": ["systems", "psychology", "business", "strategy", "philosophy"],
    "gate_threshold": 0.9,
    "match_threshold": 0.7
  }
}
```

## Behavior

- **Transparency:** Show full cognitive trace, not just answer
- **Context-grounded:** Manifests shape reasoning substrate
- **Trust convergence:** When gate says stop, stop
- **No apology:** Deep reasoning takes space

Done. Test with `@deepthink` on your next complex query.
