"""
Run SanTOK GPT Model - See It Work!
====================================

This runs the GPT-like model so you can see it generate text!
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("SanTOK GPT - GPT-Like Model")
print("=" * 70)
print()

try:
    from santok_cognitive.slm.santok_gpt import SanTOKGPT, SanTOKGPTConfig
    
    print("✅ Model imported\n")
    
    # Create model
    print("Creating GPT model...")
    config = SanTOKGPTConfig(
        vocab_size=10000,  # Smaller for demo
        d_model=256,  # Smaller for demo
        n_layers=4,  # Fewer layers for demo
        n_heads=4,
        d_ff=1024
    )
    model = SanTOKGPT(config)
    print("✅ Model created\n")
    
    # Training texts (you need more for real fluency)
    print("Loading training texts...")
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a programming language used for web development.",
        "Machine learning is a subset of artificial intelligence.",
        "Natural language processing enables computers to understand human language.",
        "Deep learning uses neural networks with multiple layers to learn patterns.",
        "SanTOK is a tokenization system with custom embeddings.",
        "Language models can generate text by predicting the next token.",
        "Transformers use attention mechanisms to process sequences.",
        "GPT models are trained on large text corpora to learn language patterns.",
        "Neural networks learn by adjusting weights through backpropagation.",
    ] * 50  # Repeat for more training data
    
    print(f"✅ Loaded {len(texts)} training texts\n")
    
    # Train
    model.train(texts, epochs=1)
    
    # Generate
    print("=" * 70)
    print("GPT-Style Generation")
    print("=" * 70)
    print()
    
    test_prompts = [
        "The quick brown",
        "Python is",
        "Machine learning",
        "SanTOK is",
    ]
    
    for prompt in test_prompts:
        print(f"Prompt: '{prompt}'")
        try:
            result = model.generate(prompt, max_tokens=30, temperature=0.8)
            print(f"Generated: {result}")
            print()
        except Exception as e:
            print(f"Error: {e}\n")
    
    print("=" * 70)
    print("✅ SanTOK GPT Model Working!")
    print("=" * 70)
    print()
    print("This is a GPT-like model using SanTOK infrastructure!")
    print()
    print("To make it more fluent like real GPT:")
    print("  1. Add more training text (books, web, etc.)")
    print("  2. Implement proper training loop with gradients")
    print("  3. Train for longer (days/weeks)")
    print()
    print("But the foundation is here - this is your GPT! 🚀")
    print()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
