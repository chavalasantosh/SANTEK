"""
Train Improved SanTOK SLM - Next 7 Days Plan
=============================================

Implements the immediate improvements:
1. Expanded vocabulary (5K-8K tokens with general English)
2. Rewritten facts into variants (10-20 per fact)
3. Repetition penalty in generation
4. 50 epochs training
"""

import sys
import os
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

# Import expansion utilities
try:
    from santok_cognitive.slm.EXPAND_TRAINING_DATA import expand_santok_knowledge_base
    from santok_cognitive.slm.VOCAB_EXPANSION import add_general_english_to_texts
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    from EXPAND_TRAINING_DATA import expand_santok_knowledge_base
    from VOCAB_EXPANSION import add_general_english_to_texts

print("\n" + "=" * 70)
print("Train Improved SanTOK SLM - Next 7 Days Plan")
print("=" * 70)
print()
print("Implementing immediate improvements:")
print("  1. Expanded vocabulary (5K-8K tokens)")
print("  2. Rewritten facts into variants (15 per fact)")
print("  3. Repetition penalty in generation")
print("  4. 50 epochs training")
print()

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM, SanTOKLGMConfig
    
    print("[OK] SanTOK LGM imported\n")
    
    # Create model with larger vocab capacity
    config = SanTOKLGMConfig(
        vocab_size=8000,  # Target 5K-8K tokens
        d_model=256,
        n_layers=4,
        n_heads=4,
        d_ff=1024,
        learning_rate=1e-4,
        batch_size=16
    )
    model = SanTOKLGM(config)
    print("[OK] Model created\n")
    
    # Load base SanTOK knowledge
    print("Loading SanTOK knowledge base...")
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
        "SanTOK has four core systems: tokenization, embeddings, semantic processing, and training.",
        "SanTOK tokenization system uses 9 methods with xorshift64 UIDs.",
        "SanTOK embedding system extracts features from TokenRecord without pretrained models.",
        "SanTOK semantic system uses self-supervised co-occurrence learning like GloVe.",
        "SanTOK training system implements pure NumPy transformer architecture.",
        "SanTOK is a complete self-contained NLP system that doesn't depend on external AI models.",
        "SanTOK doesn't use OpenAI, Hugging Face, or any external AI models for core functionality.",
        "SanTOK Cognitive provides System 2 reasoning to complement System 1 LLM capabilities.",
        "SanTOK Cognitive makes LLMs speakers, not thinkers, by providing structured knowledge.",
        "SanTOK is designed to be safe - new modules don't modify existing working code.",
    ]
    
    print(f"Base facts: {len(santok_knowledge)}")
    
    # Expand facts into variants (15 per fact)
    print("\nExpanding facts into variants (15 per fact)...")
    expanded_facts = expand_santok_knowledge_base(santok_knowledge, variants_per_fact=15)
    
    print(f"Expanded facts: {len(expanded_facts)}")
    
    # Add general English for grammar learning (65% SanTOK / 35% grammar)
    print("\nAdding general English sentences for grammar...")
    print("Ratio: 65% SanTOK / 35% grammar (optimal for early-stage models)")
    texts = add_general_english_to_texts(expanded_facts, ratio=0.35)
    
    # OPTIONAL: Load external data (Wikipedia, books, etc.)
    # Uncomment to use downloaded external data:
    """
    try:
        from santok_cognitive.slm.LOAD_EXTERNAL_DATA import load_text_file, mix_santok_and_external
        
        print("\nLoading external training data...")
        external_texts = []
        
        # Load Wikipedia data (if available)
        if os.path.exists('wikipedia_text.txt'):
            wiki_texts = load_text_file('wikipedia_text.txt', max_lines=50000)
            external_texts.extend(wiki_texts)
        
        # Load other sources...
        # if os.path.exists('books_text.txt'):
        #     book_texts = load_text_file('books_text.txt', max_lines=30000)
        #     external_texts.extend(book_texts)
        
        if external_texts:
            # Mix: 65% SanTOK, 35% external (includes grammar)
            texts = mix_santok_and_external(expanded_facts, external_texts, santok_ratio=0.65)
            print(f"[OK] Using {len(external_texts):,} external sentences!")
    except ImportError:
        print("[INFO] External data loader not available, using grammar examples only")
    """
    
    print(f"Total training sentences: {len(texts)}")
    print(f"  - SanTOK variants: {len(expanded_facts)}")
    print(f"  - General English: {len(texts) - len(expanded_facts)}")
    santok_pct = len(expanded_facts) / len(texts) * 100
    grammar_pct = (len(texts) - len(expanded_facts)) / len(texts) * 100
    print(f"  - Actual ratio: {santok_pct:.1f}% SanTOK / {grammar_pct:.1f}% grammar")
    print()
    
    # Train for 50 epochs
    print("=" * 70)
    print("Training Improved SanTOK SLM - 50 Epochs")
    print("=" * 70)
    print()
    print("This will:")
    print("  [OK] Build vocabulary with general English words")
    print("  [OK] Train on rewritten variants (better language learning)")
    print("  [OK] Train for 50 epochs")
    print("  [OK] Save improved model")
    print()
    
    model.train(texts, epochs=50, use_trainer=True)
    
    # Save model
    model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_improved.pkl")
    model.save(model_path)
    
    print()
    print("=" * 70)
    print("[OK] Improved Model Ready!")
    print("=" * 70)
    print()
    print(f"Model saved to: {os.path.abspath(model_path)}")
    print(f"Size: {os.path.getsize(model_path) / (1024*1024):.2f} MB")
    print(f"Parameters: {model.count_parameters():,}")
    print(f"Vocabulary: {model.config.vocab_size} tokens")
    print()
    
    # Test with repetition penalty
    print("=" * 70)
    print("Testing with Repetition Penalty")
    print("=" * 70)
    print()
    
    test_prompts = ["SanTOK is", "SanTOK tokenization", "SanTOK Cognitive"]
    
    for prompt in test_prompts:
        print(f"Prompt: '{prompt}'")
        print("  Without penalty:")
        result1 = model.generate(prompt, max_tokens=30, temperature=0.8, repetition_penalty=1.0)
        print(f"    {result1[:100]}...")
        print("  With penalty (1.2):")
        result2 = model.generate(prompt, max_tokens=30, temperature=0.8, repetition_penalty=1.2)
        print(f"    {result2[:100]}...")
        print()
    
    print("=" * 70)
    print("[OK] Training Complete!")
    print("=" * 70)
    print()
    print("Your improved model is ready!")
    print("Expected improvements:")
    print("  - Better grammar (general English words)")
    print("  - Less repetition (repetition penalty)")
    print("  - Better coherence (rewritten variants)")
    print()
    
except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
