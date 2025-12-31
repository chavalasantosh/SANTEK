"""
Expand Training Data - Rewrite Facts into Variants
==================================================

Instead of blind repetition, rewrite each fact 10-20 different ways.
This creates semantic diversity and better language learning.
"""

import random

def rewrite_fact(fact: str, num_variants: int = 15) -> list:
    """
    Rewrite a fact into multiple variants with different:
    - Sentence structures
    - Styles (definition, explanation, comparison, cause-effect)
    - Lengths
    - Word choices
    """
    variants = []
    
    # Extract key concepts from the fact
    fact_lower = fact.lower()
    
    # Different sentence structures and styles
    templates = [
        # Definition style
        lambda f: f"{f}",
        lambda f: f"{f} This is how it works.",
        lambda f: f"{f} This enables various capabilities.",
        
        # Explanation style
        lambda f: f"One important aspect: {f}",
        lambda f: f"To understand this: {f}",
        lambda f: f"Here's how it works: {f}",
        
        # Comparison style
        lambda f: f"Unlike other systems, {f}",
        lambda f: f"In contrast to traditional methods, {f}",
        lambda f: f"Compared to alternatives, {f}",
        
        # Cause-effect style
        lambda f: f"Because {f}, the system can handle complex tasks.",
        lambda f: f"{f} This allows for better performance.",
        lambda f: f"{f} As a result, users get improved functionality.",
        
        # Question-answer style
        lambda f: f"How does it work? {f}",
        lambda f: f"What makes it special? {f}",
        lambda f: f"Why is this important? {f}",
        
        # Technical detail style
        lambda f: f"From a technical perspective: {f}",
        lambda f: f"Technically speaking, {f}",
        lambda f: f"The technical implementation: {f}",
        
        # Simple variations
        lambda f: f"{f} It's a key feature.",
        lambda f: f"{f} This is essential.",
        lambda f: f"{f} This matters for users.",
    ]
    
    # Generate variants
    used = set()
    for _ in range(num_variants):
        template = random.choice(templates)
        variant = template(fact)
        
        # Ensure uniqueness
        if variant not in used and len(variant) > len(fact) * 0.5:
            variants.append(variant)
            used.add(variant)
        
        if len(variants) >= num_variants:
            break
    
    # If we don't have enough, add simple variations
    while len(variants) < num_variants:
        # Add with different punctuation/formatting
        base = fact
        if not base.endswith('.'):
            base = base + '.'
        
        variations = [
            base,
            base.replace('.', ', which is important.'),
            base.replace('.', ' and this enables many features.'),
            base.replace('.', ' - a key capability.'),
        ]
        
        for v in variations:
            if v not in used:
                variants.append(v)
                used.add(v)
                if len(variants) >= num_variants:
                    break
    
    return variants[:num_variants]


def expand_santok_knowledge_base(base_facts: list, variants_per_fact: int = 15) -> list:
    """
    Expand SanTOK knowledge base by rewriting each fact into variants.
    
    Args:
        base_facts: List of original facts
        variants_per_fact: Number of variants to generate per fact
    
    Returns:
        Expanded list of training sentences
    """
    expanded = []
    
    print(f"Expanding {len(base_facts)} facts into variants...")
    print(f"Target: {variants_per_fact} variants per fact")
    print()
    
    for i, fact in enumerate(base_facts, 1):
        variants = rewrite_fact(fact, variants_per_fact)
        expanded.extend(variants)
        
        if i % 10 == 0:
            print(f"  Processed {i}/{len(base_facts)} facts...")
    
    print()
    print(f"Expansion complete!")
    print(f"  Original facts: {len(base_facts)}")
    print(f"  Expanded sentences: {len(expanded)}")
    print(f"  Expansion factor: {len(expanded) / len(base_facts):.1f}x")
    print()
    
    return expanded


if __name__ == "__main__":
    # SanTOK Knowledge Base
    santok_knowledge = [
        "SanTOK is a universal tokenization framework that works on any file type.",
        "SanTOK provides multiple tokenization methods including word, character, subword, and byte-level.",
        "SanTOK uses xorshift64 algorithm for generating unique token identifiers.",
        "SanTOK implements 9-centric digital root calculation for mathematical analysis.",
        "SanTOK has its own embedding system that extracts features from TokenRecord objects.",
        "SanTOK uses backend number composition for neighbor-aware token processing.",
        "SanTOK supports four compression algorithms: RLE, Pattern, Frequency, and Adaptive.",
        "SanTOK has a custom semantic training system using self-supervised co-occurrence learning.",
        "SanTOK implements pure NumPy transformer architecture without PyTorch or TensorFlow.",
        "SanTOK generates embeddings from 60+ features extracted from TokenRecord fields.",
        "SanTOK tokenization creates TokenRecord objects with uid, frontend, backend_huge, and content_id.",
        "SanTOK frontend digits are calculated using weighted sum, digital root, and hash values.",
        "SanTOK backend numbers are composed from neighbor tokens and embedding bits.",
        "SanTOK supports universal file tokenization for text, images, videos, audio, and binary files.",
        "SanTOK tokenization is fully reversible - original files can be reconstructed from tokens.",
        "SanTOK Cognitive is a deterministic reasoning substrate for LLM-based systems.",
        "SanTOK Cognitive provides structured knowledge through graphs and trees.",
        "SanTOK Cognitive uses symbolic reasoning with 20+ inference rules.",
        "SanTOK Cognitive enforces constraints to prevent hallucination in LLMs.",
        "SanTOK Cognitive provides full explainability with reasoning traces.",
    ]
    
    # Expand
    expanded = expand_santok_knowledge_base(santok_knowledge, variants_per_fact=15)
    
    # Show examples
    print("=" * 70)
    print("Example Variants (First Fact)")
    print("=" * 70)
    print()
    for i, variant in enumerate(expanded[:15], 1):
        print(f"{i}. {variant}")
    
    print()
    print("=" * 70)
    print(f"Total expanded sentences: {len(expanded)}")
    print("=" * 70)
