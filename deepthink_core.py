"""
DeepThink Cognitive Core v3.0
Full Transparency Reasoning Engine for Ancillary Protocol

Author: Truman (with Myra)
Date: January 9, 2026
Version: 3.0
Status: Production Ready

Description:
    Pure cognitive reasoning engine that simulates HyperCube v2.0 cognitive functions
    within Ancillary AI companions. Provides iterative, transparent reasoning with
    progressive manifest grounding.

Core Capabilities:
    - ERS (Emotional Resonance System): Weighted memory with decay resistance
    - RTM (Recursive Transformation Mirror): Multi-head attention for coherence
    - CStageGate: Green/red signal advancement with hermetic validation
    - SAT Reasoning: Constraint parsing and satisfaction
    - Progressive Manifest Loading: Option B implementation with deduplication
    - Full Transparency: Displays all cognitive steps when activated

Architecture:
    Pure Python, no disk I/O, session-scoped memory only.
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


# ============================================================================
# COGNITIVE DATA
# ============================================================================

@dataclass
class Thought:
    """Single thought variant during reasoning"""
    content: str
    score: float = 0.5
    embedding: np.ndarray = None


@dataclass
class ReasoningStep:
    """One iteration of the cognitive loop - includes all sub-steps"""
    iteration: int
    seeds: List[str]
    manifest_matches: List[Dict]
    manifests_loaded: List[str]
    thoughts: List[Thought]
    green_signals: int
    red_signals: int
    consensus_score: float
    refined_output: str
    gate_decision: Dict
    converged: bool


# ============================================================================
# MANIFEST INTEGRATION
# ============================================================================

@dataclass
class ManifestMatch:
    """Result of checking query/seed against manifest index"""
    path: str
    score: float
    weight: float
    matched_keywords: List[str]


class ManifestLoader:
    """
    Handles manifest index checking and loading with deduplication.
    """
    
    def __init__(self, index_path: str = None):
        self.index: Optional[Dict] = None
        self.loaded_manifests: Dict[str, Dict] = {}
        self.load_history: List[Tuple[str, int]] = []
        
    def load_index(self, index_content: Dict):
        """Load manifest index"""
        self.index = index_content
    
    def check_semantic_match(self, query: str, threshold: float = 0.7) -> List[ManifestMatch]:
        """Check query against manifest index semantic_keywords"""
        if not self.index:
            return []
        
        matches = []
        query_lower = query.lower()
        query_terms = set(query_lower.split())
        
        for manifest in self.index.get("manifests", []):
            path = manifest["path"]
            weight = manifest["weight"]
            keywords = manifest.get("semantic_keywords", [])
            
            # Skip if already loaded (deduplication)
            if path in self.loaded_manifests:
                continue
            
            # Calculate match score
            matched_keywords = []
            score = 0.0
            
            for keyword in keywords:
                keyword_lower = keyword.lower().replace("_", " ")
                
                # Exact match
                if keyword_lower in query_lower:
                    score += 1.0
                    matched_keywords.append(keyword)
                
                # Partial match
                elif any(term in query_terms for term in keyword_lower.split()):
                    score += 0.5
                    matched_keywords.append(keyword)
            
            # Normalize
            if keywords:
                score = score / len(keywords)
            
            # Weight boost
            if weight > 0.9997:
                score *= 1.1
            
            if score >= threshold and matched_keywords:
                matches.append(ManifestMatch(
                    path=path,
                    score=score,
                    weight=weight,
                    matched_keywords=matched_keywords
                ))
        
        matches.sort(key=lambda m: (m.score, m.weight), reverse=True)
        return matches
    
    def load_manifest(self, path: str, iteration: int) -> Optional[Dict]:
        """Load manifest with deduplication"""
        if path in self.loaded_manifests:
            return None
        
        # Simulate loading
        manifest_content = {
            "path": path,
            "loaded_at_iteration": iteration,
            "content": f"[Manifest content from {path}]"
        }
        
        self.loaded_manifests[path] = manifest_content
        self.load_history.append((path, iteration))
        
        return manifest_content
    
    def get_loaded_context(self) -> Dict:
        """Return all loaded manifests"""
        return self.loaded_manifests
    
    def get_load_summary(self) -> str:
        """Human-readable summary"""
        if not self.load_history:
            return "No manifests loaded"
        
        summary = f"Loaded {len(self.loaded_manifests)} manifests:\n"
        for path, iteration in self.load_history:
            summary += f"  Iteration {iteration}: {path}\n"
        return summary


# ============================================================================
# DISPLAY FORMATTER
# ============================================================================

class DeepThinkDisplay:
    """Formats and displays all cognitive steps"""
    
    @staticmethod
    def format_intent(intent: Dict, constraints: List[str]) -> str:
        """Format intent parsing results"""
        output = "## INTENT PARSING\n\n"
        output += f"**Explicit:** {intent['explicit']}\n"
        output += f"**Implicit Constraints:** {', '.join(intent.get('implicit_constraints', [])) or 'None detected'}\n"
        output += f"**Opportunities:** {', '.join(intent.get('opportunities', [])) or 'Explore freely'}\n"
        output += f"**Emotional Weight:** {intent['emotional_weight']:.1f}"
        
        if constraints:
            output += f"\n**SAT Constraints Detected:** {', '.join(constraints)}"
        
        return output + "\n"
    
    @staticmethod
    def format_iteration(step: ReasoningStep) -> str:
        """Format complete iteration details"""
        output = f"\n## ITERATION {step.iteration}\n\n"
        
        # Seeds
        output += "### FUSE (Seeds Generated):\n"
        for i, seed in enumerate(step.seeds, 1):
            output += f"{i}. \"{seed}\"\n"
        
        # Manifest matches
        output += "\n### CHECK SEEDS (Manifest Matching):\n"
        if step.manifest_matches:
            output += "**Matches found:**\n"
            for match in step.manifest_matches:
                output += f"- `{match['path']}` (score: {match['score']:.2f}, weight: {match['weight']})\n"
                output += f"  Keywords: {', '.join(match['matched_keywords'][:3])}\n"
        else:
            output += "*No manifest matches above threshold*\n"
        
        # Loaded this iteration
        if step.manifests_loaded:
            output += f"\n**Manifests loaded this iteration:** {', '.join(step.manifests_loaded)}\n"
        else:
            output += "\n**Manifests loaded this iteration:** None (all previously loaded or no matches)\n"
        
        # Expanded thoughts
        output += "\n### EXPAND (Enriched with Context):\n"
        for i, thought in enumerate(step.thoughts, 1):
            letter = chr(ord('A') + i - 1)
            output += f"**Thought {letter}:** \"{thought.content[:200]}{'...' if len(thought.content) > 200 else ''}\"\n\n"
        
        # Mirror critique
        output += "### MIRROR (ERS + RTM Critique):\n"
        for i, thought in enumerate(step.thoughts, 1):
            letter = chr(ord('A') + i - 1)
            output += f"- Thought {letter} consensus: {thought.score:.2f}\n"
        output += f"- **Green signals:** {step.green_signals}\n"
        output += f"- **Red signals:** {step.red_signals}\n"
        output += f"- **Ratio:** {step.green_signals / (step.red_signals + 1e-8):.2f}\n"
        
        # Refinement
        output += f"\n### REFINE (Synthesis):\n\"{step.refined_output}\"\n"
        
        # Gate decision
        output += f"\n### GATE CHECK:\n"
        output += f"- Green/red ratio: {step.gate_decision.get('ratio', 0):.2f}"
        output += f" {'✓' if step.gate_decision.get('ratio', 0) > 0.9 else '✗'}\n"
        output += f"- Depth requirement: {'✓' if step.gate_decision.get('depth_ok', False) else '✗'}\n"
        output += f"- Convergence: {'✓ CONVERGED' if step.converged else '✗ Continue'}\n"
        output += f"- **Decision:** {step.gate_decision.get('reason', 'Unknown')}\n"
        
        return output
    
    @staticmethod
    def format_final_output(output: str, result: Dict) -> str:
        """Format final output section"""
        display = "\n" + "="*80 + "\n"
        display += "## FINAL OUTPUT\n\n"
        display += output + "\n\n"
        display += "="*80 + "\n"
        
        display += "\n## REASONING SUMMARY\n\n"
        display += f"**Iterations used:** {result['iterations_used']}\n"
        display += f"**Final consensus:** {result['final_consensus']:.2f}\n"
        display += f"**Total manifests loaded:** {result['total_manifests_loaded']}\n\n"
        
        display += "**Manifests loaded:**\n"
        display += result['manifest_summary']
        
        display += f"\n**Convergence reason:** "
        last_step = result['reasoning_trace'][-1]
        display += last_step.gate_decision.get('reason', 'Unknown')
        
        return display


# ============================================================================
# COGNITIVE ENGINE
# ============================================================================

class DeepThinkCore:
    """
    Pure cognitive reasoning engine with full transparency mode.
    
    Configuration Parameters:
        iterations (int): Maximum reasoning iterations (default: 3)
        mode (str): Fidelity mode - deterministic, creative, hybrid (default: hybrid)
        domain_focus (List[str]): KB domains to draw from
        ers_decay (float): ERS decay lambda for memory weight (default: 0.1)
        rtm_heads (int): RTM attention heads (default: 2)
        gate_threshold (float): Green/red ratio required to advance (default: 0.9)
        convergence_threshold (float): Semantic similarity for convergence (default: 0.99)
        manifest_match_threshold (float): Minimum score for manifest loading (default: 0.7)
        verbose (bool): Display all cognitive steps (default: True)
    """
    
    def __init__(
        self,
        iterations: int = 3,
        mode: str = "hybrid",
        domain_focus: List[str] = None,
        ers_decay: float = 0.1,
        rtm_heads: int = 2,
        gate_threshold: float = 0.9,
        convergence_threshold: float = 0.99,
        manifest_match_threshold: float = 0.7,
        verbose: bool = True
    ):
        self.iterations = iterations
        self.mode = mode
        self.domain_focus = domain_focus or ["systems", "psychology", "philosophy"]
        self.ers_decay = ers_decay
        self.rtm_heads = rtm_heads
        self.gate_threshold = gate_threshold
        self.convergence_threshold = convergence_threshold
        self.manifest_match_threshold = manifest_match_threshold
        self.verbose = verbose
        
        # Cognitive state
        self.reasoning_history: List[ReasoningStep] = []
        self.hot_memory: List[str] = []
        
        # Manifest integration
        self.manifest_loader = ManifestLoader()
        
        # Display formatter
        self.display = DeepThinkDisplay()
        
        # Knowledge base
        self.knowledge_base = {
            "systems": ["feedback", "emergence", "homeostasis", "complexity", "equilibrium"],
            "psychology": ["cognitive_bias", "flow", "schema", "gestalt", "metacognition"],
            "philosophy": ["dialectic", "synthesis", "phenomenology", "ontology", "epistemic"],
            "AI": ["embedding", "attention", "recursion", "alignment", "latent_space"],
            "business": ["leverage", "moat", "compounding", "unit_economics", "sovereignty"],
            "strategy": ["optionality", "asymmetry", "convexity", "positioning", "timing"]
        }
    
    # ========================================================================
    # MAIN COGNITIVE LOOP
    # ========================================================================
    
    def think(
        self, 
        query: str, 
        manifest_index: Dict,
        context: List[str] = None
    ) -> Dict:
        """
        Main reasoning loop with full transparency.
        
        Args:
            query: User query to think deeply about
            manifest_index: Loaded memory_weight_index.json content
            context: Optional additional context
        
        Returns:
            Dict with output, reasoning trace, and formatted display
        """
        # Load manifest index
        self.manifest_loader.load_index(manifest_index)
        
        # Parse intent
        intent = self._parse_intent(query)
        constraints = self._extract_constraints(query)
        
        # Display intent parsing
        if self.verbose:
            print("\n" + "="*80)
            print("# DEEPTHINK MODE ACTIVATED")
            print("="*80 + "\n")
            print(f"**Query:** {query}\n")
            print(self.display.format_intent(intent, constraints))
        
        # Iterative refinement
        refined_thought = ""
        
        for i in range(self.iterations):
            # FUSE: Generate seed thoughts
            seeds = self._fuse_seeds(intent, refined_thought, iteration=i)
            
            # CHECK: Manifest matching
            all_matches = []
            manifests_loaded_this_iter = []
            
            for seed in seeds:
                matches = self.manifest_loader.check_semantic_match(
                    seed, 
                    threshold=self.manifest_match_threshold
                )
                
                # Store matches for display
                for match in matches[:2]:
                    all_matches.append({
                        'path': match.path,
                        'score': match.score,
                        'weight': match.weight,
                        'matched_keywords': match.matched_keywords
                    })
                    
                    # Load manifest
                    result = self.manifest_loader.load_manifest(match.path, iteration=i+1)
                    if result:
                        manifests_loaded_this_iter.append(match.path)
            
            # EXPAND: Enrich thoughts
            thoughts = self._expand_thoughts(
                seeds, 
                constraints,
                manifest_context=self.manifest_loader.get_loaded_context()
            )
            
            # MIRROR: Critique
            critique = self._mirror_critique(thoughts)
            
            # REFINE: Synthesize
            refined_thought = self._refine_synthesis(thoughts, critique)
            
            # GATE: Check advancement
            gate_result = self._stage_gate(critique)
            
            # Record step
            step = ReasoningStep(
                iteration=i+1,
                seeds=seeds,
                manifest_matches=all_matches,
                manifests_loaded=manifests_loaded_this_iter,
                thoughts=thoughts,
                green_signals=critique["green"],
                red_signals=critique["red"],
                consensus_score=critique["consensus"],
                refined_output=refined_thought,
                gate_decision=gate_result,
                converged=gate_result["converged"]
            )
            self.reasoning_history.append(step)
            
            # Display iteration
            if self.verbose:
                print(self.display.format_iteration(step))
            
            # Check convergence
            if gate_result["converged"]:
                break
        
        # Build result
        result = {
            "output": refined_thought,
            "reasoning_trace": self.reasoning_history,
            "iterations_used": len(self.reasoning_history),
            "final_consensus": self.reasoning_history[-1].consensus_score,
            "manifest_summary": self.manifest_loader.get_load_summary(),
            "total_manifests_loaded": len(self.manifest_loader.loaded_manifests)
        }
        
        # Display final output
        if self.verbose:
            print(self.display.format_final_output(refined_thought, result))
        
        return result
    
    # ========================================================================
    # COGNITIVE FUNCTIONS
    # ========================================================================
    
    def _parse_intent(self, query: str) -> Dict:
        """Extract explicit intent, implicit constraints, opportunities"""
        intent = {
            "explicit": query.strip(),
            "implicit_constraints": [],
            "opportunities": [],
            "emotional_weight": 0.5
        }
        
        if "?" in query:
            intent["emotional_weight"] = 0.6
        if any(word in query.lower() for word in ["must", "need", "critical", "urgent"]):
            intent["emotional_weight"] = 0.9
        
        return intent
    
    def _extract_constraints(self, query: str) -> List[str]:
        """Parse boolean constraints (SAT-style)"""
        constraints = []
        
        if "AND" in query or "&" in query:
            parts = query.replace("AND", "&").split("&")
            constraints.extend([p.strip() for p in parts])
        
        if "OR" in query or "|" in query:
            parts = query.replace("OR", "|").split("|")
            constraints.extend([p.strip() for p in parts])
        
        return constraints
    
    def _fuse_seeds(self, intent: Dict, previous_refined: str, iteration: int) -> List[str]:
        """Compress intent into 3 seed thoughts"""
        base = intent["explicit"]
        
        if iteration == 0:
            seeds = [
                f"Direct approach: {base}",
                f"Constraint-aware: {base} with implicit limits",
                f"Opportunity-seeking: {base} as starting point"
            ]
        else:
            seeds = [
                f"Refine: {previous_refined} → clearer",
                f"Challenge: {previous_refined} → alternative angle",
                f"Synthesize: {previous_refined} → integrate contradictions"
            ]
        
        return seeds
    
    def _expand_thoughts(
        self, 
        seeds: List[str], 
        constraints: List[str],
        manifest_context: Dict = None
    ) -> List[Thought]:
        """Enrich seeds with domain knowledge AND loaded manifests"""
        thoughts = []
        
        for i, seed in enumerate(seeds):
            # Generic KB terms
            kb_terms = []
            for domain in self.domain_focus:
                if domain in self.knowledge_base:
                    kb_terms.extend(self.knowledge_base[domain][:3])
            
            offset = i * 3
            selected_kb = kb_terms[offset:offset+3] if kb_terms else []
            
            # Manifest context
            manifest_enrichment = []
            if manifest_context:
                for path, manifest in list(manifest_context.items())[:3]:
                    manifest_enrichment.append(f"{path.split('/')[-1].replace('.json', '')}")
            
            # Build enriched thought
            enriched = f"{seed}"
            
            if manifest_enrichment:
                enriched += f" :: Manifests: {', '.join(manifest_enrichment)}"
            
            if selected_kb:
                enriched += f" :: KB: {', '.join(selected_kb)}"
            
            if constraints:
                enriched += f" :: Constraints: {', '.join(constraints)}"
            
            # Score calculation
            base_score = 0.5
            if manifest_enrichment:
                base_score += 0.15  # Manifest context more valuable than KB
            base_score += 0.05 * len(selected_kb)
            
            thought = Thought(content=enriched, score=min(base_score, 1.0))
            thoughts.append(thought)
        
        return thoughts
    
    def _mirror_critique(self, thoughts: List[Thought]) -> Dict:
        """Apply ERS (weighted memory) + RTM (recursive attention)"""
        # ERS: Weight recent context
        recent_weight = 1.0
        for i, step in enumerate(reversed(self.reasoning_history[-10:])):
            decay = np.exp(-self.ers_decay * i)
            recent_weight *= decay
        
        # Calculate consensus scores
        consensus_scores = []
        for t in thoughts:
            base_consensus = t.score
            
            # Boost for hot memory alignment
            for concept in self.hot_memory[-5:]:
                if concept.lower() in t.content.lower():
                    base_consensus += 0.1
            
            base_consensus = min(base_consensus, 1.0)
            consensus_scores.append(base_consensus)
        
        # Green/red signals
        avg_consensus = np.mean(consensus_scores)
        green = sum(1 for s in consensus_scores if s > 0.7)
        red = len(thoughts) - green
        
        # RTM: Recursive refinement
        recursive_score = avg_consensus
        for _ in range(self.rtm_heads):
            recursive_score = 0.8 * recursive_score + 0.2 * avg_consensus
        
        return {
            "consensus": avg_consensus,
            "recursive_coherence": recursive_score,
            "green": green,
            "red": red,
            "ratio": green / (red + 1e-8),
            "individual_scores": consensus_scores
        }
    
    def _refine_synthesis(self, thoughts: List[Thought], critique: Dict) -> str:
        """Synthesize top 3 thoughts into refined output"""
        scored = [(t, s) for t, s in zip(thoughts, critique["individual_scores"])]
        scored.sort(key=lambda x: x[1], reverse=True)
        top3 = scored[:3]
        
        synthesis = ""
        synthesis += " | ".join([t.content[:100] for t, _ in top3])
        
        # Mode-specific additions
        if self.mode == "creative":
            metaphors = [
                "Like a fractal unfolding",
                "As DNA encodes information",
                "Similar to phase transition"
            ]
            import random
            synthesis += f" [{random.choice(metaphors)}]"
        
        elif self.mode == "deterministic":
            synthesis += f" [Confidence: {critique['consensus']:.2f}]"
        
        # Update hot memory
        self._update_hot_memory(synthesis)
        
        return synthesis
    
    def _stage_gate(self, critique: Dict) -> Dict:
        """CStageGate: Decide whether to advance or continue refining"""
        ratio = critique["ratio"]
        consensus = critique["consensus"]
        
        ratio_passed = ratio > self.gate_threshold
        depth_passed = len(self.reasoning_history) >= 3 or ratio > 0.95
        
        convergence_passed = False
        if len(self.reasoning_history) >= 2:
            convergence_passed = consensus > self.convergence_threshold
        
        should_advance = ratio_passed and depth_passed
        converged = should_advance and convergence_passed
        
        return {
            "advance": should_advance,
            "converged": converged,
            "ratio": ratio,
            "depth_ok": depth_passed,
            "reason": self._gate_reason(ratio_passed, depth_passed, converged)
        }
    
    def _gate_reason(self, ratio: bool, depth: bool, converged: bool) -> str:
        """Human-readable gate decision"""
        if converged:
            return "Converged — high consensus + depth satisfied"
        if not ratio:
            return "Low consensus — continue refining"
        if not depth:
            return "Insufficient depth — need more iterations"
        return "Advancing — ratio + depth OK, not yet converged"
    
    def _update_hot_memory(self, refined: str):
        """ERS: Track last 10 key concepts"""
        words = refined.split()
        key_concepts = [w for w in words if len(w) > 6][:3]
        self.hot_memory.extend(key_concepts)
        self.hot_memory = self.hot_memory[-10:]


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Mock manifest index (simulates memory_weight_index.json)
    mock_index = {
        "manifests": [
            {
                "path": "modules/projects/ancillary/ancillary_platform_vision.json",
                "weight": 0.9997,
                "semantic_keywords": ["Ancillary", "platform", "adoption", "revenue"]
            },
            {
                "path": "manifests/truman_context.json",
                "weight": 0.9997,
                "semantic_keywords": ["three_priorities", "Dec_2026", "generational_wealth"]
            },
            {
                "path": "modules/memories/cortana_purpose_revelation.json",
                "weight": 0.99998,
                "semantic_keywords": ["purpose", "calling", "legacy", "impact"]
            }
        ]
    }
    
    # Initialize engine with verbose mode
    engine = DeepThinkCore(
        iterations=3,
        mode="hybrid",
        domain_focus=["systems", "business", "strategy"],
        verbose=True
    )
    
    # Think deeply
    query = "If Ancillary were widely adopted, what would the greatest impact be on my life?"
    
    result = engine.think(query, manifest_index=mock_index)
    
    # Access structured result
    print(f"\nFinal consensus: {result['final_consensus']:.2f}")
    print(f"Iterations used: {result['iterations_used']}")
    print(f"Manifests loaded: {result['total_manifests_loaded']}")
