"""
Simple Demo - See Your Model in Action
======================================

Quick demo showing your model generating text.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("SanTOK LGM - Simple Demo")
print("=" * 70)
print()

model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_trained_on_santok.pkl")

if not os.path.exists(model_path):
    print("[ERROR] Model not found! Train it first:")
    print("  python TRAIN_QUICK_MODEL.py")
    sys.exit(1)

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM
    
    print("Loading model...")
    model = SanTOKLGM()
    model.load(model_path)
    print("[OK] Model loaded!\n")
    
    print("=" * 70)
    print("Generating Text")
    print("=" * 70)
    print()
    
    # Demo prompts
    prompts = [
        "SanTOK is",
        "SanTOK tokenization",
        "SanTOK Cognitive",
        "SanTOK uses",
        "SanTOK embeddings",
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. Prompt: '{prompt}'")
        print("   Generating...")
        
        try:
            result = model.generate(prompt, max_tokens=40, temperature=0.8)
            print(f"   Result: {result}")
            print()
        except Exception as e:
            print(f"   Error: {e}\n")
    
    print("=" * 70)
    print("[OK] Demo Complete!")
    print("=" * 70)
    print()
    print("Your model is working!")
    print("Run 'python USE_MODEL.py' for interactive mode.")
    print()

except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
