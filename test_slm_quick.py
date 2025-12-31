#!/usr/bin/env python
"""Quick SLM test"""

from santok_slm import SanTOKSLM

slm = SanTOKSLM()
print("SLM created")

slm.load_facts([
    "Python is a programming language",
    "Python was created by Guido van Rossum",
    "Python is used for web development"
])
print("Facts loaded")

stats = slm.get_stats()
print(f"\nNeural Model:")
print(f"  Parameters: {stats['neural_model']['parameters']:,}")
print(f"  Layers: {stats['neural_model']['n_layers']}")
print(f"  Heads: {stats['neural_model']['n_heads']}")
print(f"  Vocabulary: {stats['neural_model']['vocab_size']}")

print("\nGenerating...")
result = slm.generate("What is Python?", max_length=20)
print(f"Result: {result}")
