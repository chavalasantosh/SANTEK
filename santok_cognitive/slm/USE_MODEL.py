"""
Use Your SanTOK LGM Model - Interactive
=======================================

Simple script to use your trained SanTOK LGM model.
Just run it and start generating text!
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

print("\n" + "=" * 70)
print("SanTOK LGM - Interactive Model Usage")
print("=" * 70)
print()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_trained_on_santok.pkl")

if not os.path.exists(model_path):
    print("[ERROR] Model file not found!")
    print(f"Expected: {os.path.abspath(model_path)}")
    print()
    print("Train the model first:")
    print("  python TRAIN_QUICK_MODEL.py")
    sys.exit(1)

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM
    
    print("Loading model...")
    model = SanTOKLGM()
    model.load(model_path)
    
    print("[OK] Model loaded!")
    print()
    print("=" * 70)
    print("Model Info")
    print("=" * 70)
    print(f"Parameters: {model.count_parameters():,}")
    print(f"Vocabulary: {model.config.vocab_size} tokens")
    print(f"Model size: {os.path.getsize(model_path) / (1024*1024):.2f} MB")
    print()
    
    print("=" * 70)
    print("Ready to Generate!")
    print("=" * 70)
    print()
    print("Enter prompts to generate text.")
    print("Type 'quit' or 'exit' to stop.")
    print("Type 'examples' to see example prompts.")
    print()
    
    while True:
        try:
            prompt = input("Your prompt: ").strip()
            
            if not prompt:
                continue
            
            if prompt.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break
            
            if prompt.lower() == 'examples':
                print("\nExample prompts:")
                print("  - SanTOK is")
                print("  - SanTOK tokenization")
                print("  - SanTOK Cognitive")
                print("  - SanTOK uses")
                print("  - SanTOK embeddings")
                print()
                continue
            
            # Generate
            print("\nGenerating...")
            try:
                result = model.generate(prompt, max_tokens=50, temperature=0.8)
                print(f"\nGenerated text:")
                print(f"  {result}")
                print()
            except Exception as e:
                print(f"Error: {e}\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")

except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
