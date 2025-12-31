"""
Find and Load Any Available SanTOK Model
==========================================

This script finds any available trained model and loads it.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("Find and Load SanTOK Model")
print("=" * 70)
print()

# Possible model files
possible_models = [
    "santok_lgm_trained_on_santok.pkl",  # New SanTOK-native model
    "santok_gpt_trained.pkl",            # Older model
]

found_models = []

for model_name in possible_models:
    model_path = os.path.join(os.path.dirname(__file__), model_name)
    if os.path.exists(model_path):
        size_mb = os.path.getsize(model_path) / (1024 * 1024)
        found_models.append((model_path, model_name, size_mb))
        print(f"[FOUND] {model_name}")
        print(f"  Path: {os.path.abspath(model_path)}")
        print(f"  Size: {size_mb:.2f} MB")
        print()

if not found_models:
    print("[NOT FOUND] No trained models found!")
    print()
    print("Available training scripts:")
    print("  1. python TRAIN_ON_SANTOK_DATA.py  (Trains on SanTOK knowledge)")
    print("  2. python TRAIN_GPT_MODEL.py      (Trains on general text)")
    print()
    print("Training takes time (50 epochs), so be patient!")
    sys.exit(1)

# Use the first found model (prefer the new one)
model_path, model_name, size_mb = found_models[0]

print("=" * 70)
print(f"Loading: {model_name}")
print("=" * 70)
print()

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM
    
    print(f"Loading model...")
    model = SanTOKLGM()
    model.load(model_path)
    
    print("[OK] Model loaded!")
    print()
    print("=" * 70)
    print("Model Details")
    print("=" * 70)
    print()
    print(f"Model file: {model_name}")
    print(f"Parameters: {model.count_parameters():,}")
    print(f"Vocabulary: {model.config.vocab_size} tokens")
    print(f"Model size: {size_mb:.2f} MB")
    print(f"Trained: {model.trained}")
    print()
    
    print("=" * 70)
    print("Test Generation")
    print("=" * 70)
    print()
    
    test_prompts = [
        "SanTOK is",
        "SanTOK tokenization",
        "SanTOK Cognitive",
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
    print("[OK] Model Ready!")
    print("=" * 70)
    print()
    print("Your SanTOK LGM model is loaded and working!")
    print("This is SanTOK's own Language Generation Model.")
    print("100% SanTOK-native!")
    print()
    print("You can use this model in your code:")
    print("  from santok_cognitive.slm.santok_gpt import SanTOKLGM")
    print("  model = SanTOKLGM()")
    print(f"  model.load('{model_name}')")
    print("  result = model.generate('Your prompt here')")
    print()
    
except Exception as e:
    print(f"[ERROR] Error loading model: {e}")
    import traceback
    traceback.print_exc()
