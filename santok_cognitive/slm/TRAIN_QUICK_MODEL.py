"""
Train SanTOK LGM QUICKLY - Get Model Fast!
===========================================

This trains with fewer epochs to get you a model quickly.
You can train longer later for better results.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("SanTOK LGM - QUICK Training (5 Epochs)")
print("=" * 70)
print()
print("Training quickly to get you a model NOW!")
print("You can train longer later for better results.")
print()

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM, SanTOKLGMConfig
    
    print("[OK] SanTOK LGM imported\n")
    
    # Create SanTOK LGM
    config = SanTOKLGMConfig(
        vocab_size=10000,
        d_model=256,
        n_layers=4,
        n_heads=4,
        d_ff=1024,
        learning_rate=1e-4,
        batch_size=16
    )
    model = SanTOKLGM(config)
    print("[OK] SanTOK LGM created\n")
    
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
    
    # Expand training data (less repetition for faster training)
    texts = santok_knowledge * 50  # 50x repetition for quick training
    
    print(f"[OK] Loaded {len(texts)} training sentences")
    print(f"    Unique facts: {len(santok_knowledge)}")
    print()
    
    # Train with 5 EPOCHS for quick results
    print("=" * 70)
    print("Training SanTOK LGM - 5 Epochs (QUICK)")
    print("=" * 70)
    print()
    print("This will train quickly to get you a model NOW!")
    print("You can train longer later (50 epochs) for better results.")
    print()
    
    model.train(texts, epochs=5, use_trainer=True)
    
    # Save the model
    model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_trained_on_santok.pkl")
    model.save(model_path)
    
    print()
    print("=" * 70)
    print("[OK] MODEL READY!")
    print("=" * 70)
    print()
    print(f"Model saved to: {os.path.abspath(model_path)}")
    print(f"Size: {os.path.getsize(model_path) / (1024*1024):.2f} MB")
    print(f"Parameters: {model.count_parameters():,}")
    print()
    print("You can now use it with:")
    print("  python FIND_AND_LOAD_MODEL.py")
    print("  python GET_MODEL.py")
    print()
    
    # Quick test
    print("=" * 70)
    print("Quick Test")
    print("=" * 70)
    print()
    
    test_prompts = ["SanTOK is", "SanTOK tokenization"]
    for prompt in test_prompts:
        print(f"Prompt: '{prompt}'")
        try:
            result = model.generate(prompt, max_tokens=20, temperature=0.8)
            print(f"Generated: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    print("=" * 70)
    print("[OK] MODEL IS READY TO USE!")
    print("=" * 70)
    print()
    
except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
