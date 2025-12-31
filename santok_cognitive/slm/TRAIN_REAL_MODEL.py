"""
Train REAL SanTOK GPT Model - 50 Epochs
========================================

This trains your REAL GPT model with 50 epochs and saves it!
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("SanTOK GPT - Training REAL Model (50 Epochs)")
print("=" * 70)
print()

try:
    from santok_cognitive.slm.santok_gpt import SanTOKGPT, SanTOKGPTConfig
    
    print("[OK] Model imported\n")
    
    # Create model
    print("Creating GPT model...")
    config = SanTOKGPTConfig(
        vocab_size=10000,
        d_model=256,
        n_layers=4,
        n_heads=4,
        d_ff=1024,
        learning_rate=1e-4,
        batch_size=16
    )
    model = SanTOKGPT(config)
    print("[OK] Model created\n")
    
    # Training texts
    print("Loading training texts...")
    base_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a programming language used for web development and data science.",
        "Machine learning is a subset of artificial intelligence that enables computers to learn.",
        "Natural language processing enables computers to understand and generate human language.",
        "Deep learning uses neural networks with multiple layers to learn complex patterns.",
        "SanTOK is a tokenization system with custom embeddings and semantic processing.",
        "Language models can generate text by predicting the next token in a sequence.",
        "Transformers use attention mechanisms to process sequences of tokens efficiently.",
        "GPT models are trained on large text corpora to learn language patterns and structure.",
        "Neural networks learn by adjusting weights through backpropagation and gradient descent.",
        "Artificial intelligence aims to create systems that can perform tasks requiring human intelligence.",
        "Computer science is the study of algorithms, data structures, and computational systems.",
        "Programming involves writing code to solve problems and create software applications.",
        "Data structures organize information in ways that enable efficient access and modification.",
        "Algorithms are step-by-step procedures for solving computational problems.",
    ]
    
    # Expand training data
    texts = base_texts * 200
    
    print(f"[OK] Loaded {len(texts)} training texts")
    print(f"    Base sentences: {len(base_texts)}")
    print(f"    Total training examples: {len(texts)}\n")
    
    # Train with 50 EPOCHS (REAL training!)
    print("=" * 70)
    print("Starting REAL Training - 50 EPOCHS")
    print("=" * 70)
    print()
    print("This will:")
    print("  [OK] Compute loss")
    print("  [OK] Compute gradients")
    print("  [OK] Update weights")
    print("  [OK] Train for 50 epochs (REAL training!)")
    print()
    
    model.train(texts, epochs=50, use_trainer=True)
    
    # Save the REAL trained model
    print("=" * 70)
    print("Saving REAL Trained Model")
    print("=" * 70)
    print()
    
    model_path = os.path.join(os.path.dirname(__file__), "santok_gpt_trained.pkl")
    model.save(model_path)
    
    print()
    print("=" * 70)
    print("YOUR REAL MODEL IS SAVED!")
    print("=" * 70)
    print()
    print(f"Model file: {model_path}")
    print(f"Model size: {os.path.getsize(model_path) / (1024*1024):.2f} MB")
    print(f"Parameters: {model.count_parameters():,}")
    print(f"Epochs trained: 50")
    print()
    print("This is a REAL trained model!")
    print("All weights have been updated through 50 epochs!")
    print("You can load it with: python LOAD_AND_USE_MODEL.py")
    print()
    
    # Test generation
    print("=" * 70)
    print("Testing Generation")
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
    print("[OK] REAL Model Training Complete!")
    print("=" * 70)
    print()
    
except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
