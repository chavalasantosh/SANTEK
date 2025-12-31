"""
Check SanTOK LGM Model Status
=============================

Check if the trained model exists and show its details.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("SanTOK LGM Model Status Check")
print("=" * 70)
print()

model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_trained_on_santok.pkl")
model_path_abs = os.path.abspath(model_path)

print(f"Looking for model at:")
print(f"  {model_path_abs}")
print()

if os.path.exists(model_path):
    size_mb = os.path.getsize(model_path) / (1024 * 1024)
    print("[OK] Model file EXISTS!")
    print()
    print(f"Model file: {model_path_abs}")
    print(f"Size: {size_mb:.2f} MB")
    print()
    
    # Try to load it
    try:
        from santok_cognitive.slm.santok_gpt import SanTOKLGM
        
        print("Loading model...")
        model = SanTOKLGM()
        model.load(model_path)
        
        print("[OK] Model loaded successfully!")
        print()
        print(f"Parameters: {model.count_parameters():,}")
        print(f"Vocabulary: {model.config.vocab_size} tokens")
        print(f"Trained: {model.trained}")
        print()
        print("Model is ready to use!")
        print()
        
        # Quick test
        print("Quick generation test:")
        try:
            result = model.generate("SanTOK is", max_tokens=20, temperature=0.8)
            print(f"  Prompt: 'SanTOK is'")
            print(f"  Generated: {result}")
            print()
            print("[OK] Model is working!")
        except Exception as e:
            print(f"  [ERROR] Generation failed: {e}")
        
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        import traceback
        traceback.print_exc()
else:
    print("[NOT FOUND] Model file does not exist yet.")
    print()
    print("The model is still training or training hasn't started.")
    print("Run: python TRAIN_ON_SANTOK_DATA.py")
    print()
    print("Training takes time (50 epochs), so be patient!")

print("=" * 70)
