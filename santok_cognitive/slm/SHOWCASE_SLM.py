"""
SanTOK Showcase SLM - Lightweight Demo Model
===========================================

Optimized for:
- Low RAM (uses ~2-4 GB)
- Low CPU (trains in 10-30 minutes)
- Low storage (model ~5-10 MB)
- Showcase-ready (produces coherent SanTOK text)

This is your PUBLIC DEMO model - perfect for showcasing SanTOK!
"""

import sys
import os
import pickle
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

try:
    from santok_cognitive.slm.santok_gpt import SanTOKLGM, SanTOKLGMConfig
    from santok_cognitive.slm.santok_gpt_trainer_real import SanTOKLGMTrainer
    from santok_cognitive.slm.EXPAND_TRAINING_DATA import expand_santok_knowledge_base
    from santok_cognitive.slm.VOCAB_EXPANSION import add_general_english_to_texts
except ImportError:
    # Fallback for direct execution
    from santok_gpt import SanTOKLGM, SanTOKLGMConfig
    from santok_gpt_trainer_real import SanTOKLGMTrainer
    from EXPAND_TRAINING_DATA import expand_santok_knowledge_base
    from VOCAB_EXPANSION import add_general_english_to_texts

print("\n" + "=" * 70)
print("SanTOK Showcase SLM - Lightweight Demo Model")
print("=" * 70)
print()
print("Optimized for low-resource systems:")
print("  - RAM: ~2-4 GB")
print("  - CPU: 10-30 minutes training")
print("  - Storage: ~5-10 MB model file")
print("  - Perfect for public demonstration!")
print()

# ============================================================================
# STEP 1: Create MINIMAL model config (lightweight!)
# ============================================================================

config = SanTOKLGMConfig(
    vocab_size=3000,      # Small vocab (was 8000) - saves memory
    d_model=128,          # Small model (was 256) - 4x less memory
    n_layers=3,          # Few layers (was 6) - faster training
    n_heads=4,           # Few heads (was 8) - less compute
    d_ff=512,            # Small FF (was 1024) - less memory
    max_seq_len=256,     # Shorter sequences (was 512) - faster
    learning_rate=2e-4,   # Slightly higher LR for faster convergence
    batch_size=8         # Small batches (was 16) - less memory
)

print("[OK] Model config created (lightweight)")
print(f"    Vocab: {config.vocab_size}")
print(f"    Model dim: {config.d_model}")
print(f"    Layers: {config.n_layers}")
print(f"    Heads: {config.n_heads}")
print(f"    Estimated RAM: ~2-3 GB")
print()

# ============================================================================
# STEP 2: Load SanTOK knowledge (NO external downloads!)
# ============================================================================

print("Loading SanTOK knowledge base...")
print("(Using only SanTOK's own data - no external downloads!)")
print()

santok_knowledge = [
    # Core SanTOK Concepts
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
    
    # Tokenization Features
    "SanTOK tokenization creates TokenRecord objects with uid, frontend, backend_huge, and content_id.",
    "SanTOK frontend digits are calculated using weighted sum, digital root, and hash values.",
    "SanTOK backend numbers are composed from neighbor tokens and embedding bits.",
    "SanTOK supports universal file tokenization for text, images, videos, audio, and binary files.",
    "SanTOK tokenization is fully reversible - original files can be reconstructed from tokens.",
    
    # Cognitive System
    "SanTOK Cognitive is a deterministic reasoning substrate for LLM-based systems.",
    "SanTOK Cognitive provides structured knowledge through graphs and trees.",
    "SanTOK Cognitive uses symbolic reasoning with 20+ inference rules.",
    "SanTOK Cognitive enforces constraints to prevent hallucination in LLMs.",
    "SanTOK Cognitive provides full explainability with reasoning traces.",
    
    # Architecture
    "SanTOK has four core systems: tokenization, embeddings, semantic processing, and training.",
    "SanTOK tokenization system uses 9 methods with xorshift64 UIDs.",
    "SanTOK embedding system extracts features from TokenRecord without pretrained models.",
    "SanTOK semantic system uses self-supervised co-occurrence learning like GloVe.",
    "SanTOK training system implements pure NumPy transformer architecture.",
    
    # Philosophy
    "SanTOK is a complete self-contained NLP system that doesn't depend on external AI models.",
    "SanTOK doesn't use OpenAI, Hugging Face, or any external AI models for core functionality.",
    "SanTOK Cognitive provides System 2 reasoning to complement System 1 LLM capabilities.",
    "SanTOK Cognitive makes LLMs speakers, not thinkers, by providing structured knowledge.",
    "SanTOK is designed to be safe - new modules don't modify existing working code.",
]

print(f"[OK] Loaded {len(santok_knowledge)} base facts")
print()

# ============================================================================
# STEP 3: Expand facts (lightweight expansion)
# ============================================================================

print("Expanding facts into variants (10 per fact for lightweight training)...")
expanded_facts = expand_santok_knowledge_base(santok_knowledge, variants_per_fact=10)
print(f"[OK] Expanded to {len(expanded_facts)} training sentences")
print()

# ============================================================================
# STEP 4: Add minimal grammar (lightweight)
# ============================================================================

print("Adding general English for grammar (25% grammar, 75% SanTOK)...")
print("(Lightweight ratio for faster training)")
training_texts = add_general_english_to_texts(expanded_facts, ratio=0.25)
print(f"[OK] Total training sentences: {len(training_texts)}")
print()

# ============================================================================
# STEP 5: Create model
# ============================================================================

print("Creating SanTOK LGM model...")
model = SanTOKLGM(config)
print("[OK] Model created")
print()

# ============================================================================
# STEP 6: Train (lightweight training - fewer epochs)
# ============================================================================

print("=" * 70)
print("Training Showcase Model (Lightweight)")
print("=" * 70)
print()
print("Training settings:")
print("  - Epochs: 20 (lightweight, was 50)")
print("  - Batch size: 8 (small batches)")
print("  - Estimated time: 10-30 minutes")
print()

# Shuffle for better learning
random.shuffle(training_texts)

# Train with lightweight trainer
trainer = SanTOKLGMTrainer(model, learning_rate=config.learning_rate)
trainer.train(training_texts, epochs=20, batch_size=config.batch_size)

print()
print("=" * 70)
print("[OK] Training Complete!")
print("=" * 70)
print()

# ============================================================================
# STEP 7: Save model
# ============================================================================

model_file = "santok_showcase_slm.pkl"
print(f"Saving model to {model_file}...")
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

file_size_mb = os.path.getsize(model_file) / (1024 * 1024)
print(f"[OK] Model saved: {file_size_mb:.2f} MB")
print()

# ============================================================================
# STEP 8: Test generation
# ============================================================================

print("=" * 70)
print("Testing Generation (Showcase Examples)")
print("=" * 70)
print()

test_prompts = [
    "SanTOK is",
    "SanTOK tokenization",
    "SanTOK Cognitive",
    "What is SanTOK?",
]

for prompt in test_prompts:
    generated = model.generate(prompt, max_length=50, temperature=0.7, repetition_penalty=1.2)
    print(f"Prompt: '{prompt}'")
    print(f"Generated: {generated}")
    print()

print("=" * 70)
print("[OK] Showcase Model Ready!")
print("=" * 70)
print()
print("Your showcase model is ready to demonstrate SanTOK!")
print(f"Model file: {os.path.abspath(model_file)}")
print(f"Model size: {file_size_mb:.2f} MB")
print()
print("To use this model:")
print("  python USE_SHOWCASE_MODEL.py")
print()
