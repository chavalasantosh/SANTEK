"""
Use SanTOK Showcase SLM - Interactive Demo
==========================================

Load and use the showcase model for public demonstration.
"""

import sys
import os
import pickle

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from santok_cognitive.slm.santok_gpt import SanTOKLGM

print("\n" + "=" * 70)
print("SanTOK Showcase SLM - Interactive Demo")
print("=" * 70)
print()

# Load model
model_file = "santok_showcase_slm.pkl"

if not os.path.exists(model_file):
    print(f"[ERROR] Model file not found: {model_file}")
    print()
    print("Please train the model first:")
    print("  python SHOWCASE_SLM.py")
    print()
    sys.exit(1)

print(f"Loading model from {model_file}...")
with open(model_file, 'rb') as f:
    model = pickle.load(f)

file_size_mb = os.path.getsize(model_file) / (1024 * 1024)
print(f"[OK] Model loaded: {file_size_mb:.2f} MB")
print()

# Show model info
print("Model Information:")
print(f"  Vocabulary size: {len(model.tokenizer.vocab)}")
print(f"  Model parameters: ~{model.count_parameters():,}")
print()

# Demo prompts
print("=" * 70)
print("Predefined Demo Prompts")
print("=" * 70)
print()

demo_prompts = [
    "SanTOK is",
    "SanTOK tokenization",
    "SanTOK Cognitive provides",
    "What is SanTOK?",
    "SanTOK uses",
]

for prompt in demo_prompts:
    generated = model.generate(
        prompt, 
        max_length=60, 
        temperature=0.7, 
        repetition_penalty=1.2
    )
    print(f"Prompt: '{prompt}'")
    print(f"Generated: {generated}")
    print()

# Interactive mode
print("=" * 70)
print("Interactive Mode")
print("=" * 70)
print()
print("Enter prompts to generate text (or 'quit' to exit):")
print()

while True:
    try:
        prompt = input("You: ").strip()
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            print("\n[OK] Goodbye!")
            break
        
        if not prompt:
            continue
        
        generated = model.generate(
            prompt,
            max_length=80,
            temperature=0.7,
            repetition_penalty=1.2
        )
        
        print(f"SanTOK: {generated}")
        print()
        
    except KeyboardInterrupt:
        print("\n\n[OK] Goodbye!")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        print()
