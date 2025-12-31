#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SanTOK First Model - Quick Demo
================================

Run: python QUICK_DEMO.py
"""

import sys
import os

# Setup paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

# Force output
import sys
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

print("\n" + "="*70)
print("SanTOK First Model - Quick Demo")
print("="*70 + "\n")

# Test basic imports
print("Step 1: Testing imports...")
try:
    from santok_cognitive.slm.small_slm import (
        SanTOKTokenizerWrapper,
        ConstraintEngine,
        SanTOKSequenceOptimizer,
        ConstrainedDecoder,
        SLMConfig
    )
    print("✅ Core components imported")
except Exception as e:
    print(f"❌ Import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test tokenizer
print("\nStep 2: Testing SanTOK tokenizer...")
try:
    tokenizer = SanTOKTokenizerWrapper()
    test_text = "SanTOK is a tokenization system"
    tokens = tokenizer.tokenize(test_text)
    print(f"✅ Tokenized '{test_text}'")
    print(f"   Tokens: {tokens}")
except Exception as e:
    print(f"❌ Tokenizer error: {e}")
    import traceback
    traceback.print_exc()

# Test constraint engine
print("\nStep 3: Testing constraint engine...")
try:
    facts = ["SanTOK is a tokenization system", "SanTOK has custom embeddings"]
    engine = ConstraintEngine(facts)
    allowed = engine.get_allowed_tokens()
    print(f"✅ Constraint engine created")
    print(f"   Facts: {len(facts)}")
    print(f"   Allowed tokens: {len(allowed)}")
    print(f"   Sample tokens: {list(allowed)[:10]}")
except Exception as e:
    print(f"❌ Constraint engine error: {e}")
    import traceback
    traceback.print_exc()

# Test full model
print("\nStep 4: Testing full model...")
try:
    from santok_cognitive.slm.santok_slm_model import create_santok_slm_model
    
    model = create_santok_slm_model(
        vocab_size=1000,
        d_model=32,
        n_layers=1,
        use_cognitive=False
    )
    print("✅ Model created")
    
    # Train
    facts = [
        "SanTOK is a tokenization system",
        "SanTOK has custom embeddings",
        "SanTOK uses 9-centric numerology"
    ]
    print(f"\nTraining on {len(facts)} facts...")
    model.train(facts)
    
    # Generate
    print("\nGenerating...")
    result = model.generate("What is SanTOK?", max_tokens=15)
    print(f"✅ Generated: {result}")
    
    # Stats
    stats = model.get_stats()
    print(f"\nModel Stats:")
    print(f"  Vocab size: {stats.get('vocab_size', 'N/A')}")
    print(f"  Allowed tokens: {stats.get('allowed_tokens', 'N/A')}")
    print(f"  Parameters: {stats.get('model_parameters', 'N/A'):,}" if stats.get('model_parameters') else "  Parameters: N/A")
    
except Exception as e:
    print(f"❌ Model error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("✅ SanTOK First Model Demo Complete!")
print("="*70 + "\n")
