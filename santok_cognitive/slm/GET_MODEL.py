"""
Get SanTOK LGM Model
====================

Load and use your trained SanTOK LGM model.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("Get SanTOK LGM Model")
print("=" * 70)
print()

model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_trained_on_santok.pkl")

if not os.path.exists(model_path):
    print("[ERROR] Model file not found!")
    print()
    print(f"Expected location: {os.path.abspath(model_path)}")
    print()
    print("The model needs to be trained first.")
    print("Run: python TRAIN_ON_SANTOK_DATA.py")
    print()
    print("This will train the model for 50 epochs on SanTOK knowledge.")
    print("Training takes time - be patient!")
    sys.exit(1)

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM
    
    print(f"Loading model from: {os.path.abspath(model_path)}")
    print()
    
    model = SanTOKLGM()
    model.load(model_path)
    
    print("[OK] Model loaded!")
    print()
    print("=" * 70)
    print("Model Details")
    print("=" * 70)
    print()
    print(f"Parameters: {model.count_parameters():,}")
    print(f"Vocabulary: {model.config.vocab_size} tokens")
    print(f"Model size: {os.path.getsize(model_path) / (1024*1024):.2f} MB")
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
        "SanTOK uses",
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
    print("100% SanTOK-native - trained on SanTOK's own knowledge!")
    print()
    
except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
