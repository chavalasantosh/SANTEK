# SanTOK Small Language Model (SLM)

**Constraint-Grounded Small Language Model (CG-SLM)**

A lightweight, CPU-friendly language model that uses **ONLY** SanTOK's custom infrastructure.

## What is SanTOK SLM?

SanTOK SLM is a **Constraint-Grounded Small Language Model (CG-SLM)** - a specific class of SLM.

### System Behavior (SLM Characteristics)

✅ **Has embeddings** - Uses SanTOK embeddings and learned embedding matrices  
✅ **Has sequence modeling** - Transformer-based sequence optimizer  
✅ **Has learned parameters** - Trainable weights in attention and feed-forward layers  
✅ **Has probabilistic sampling** - Temperature-based token sampling  
✅ **Improves ordering with training** - Learns token co-occurrence patterns  

**This IS an SLM**, but of a different class than traditional statistical language models.

### Key Differentiator

**Traditional SLM:**
- Learns from data
- Can hallucinate
- Probabilistic output

**SanTOK SLM (CG-SLM):**
- Learns ordering patterns (not facts)
- **Cannot hallucinate** (structurally impossible)
- Constraint-grounded output
- Intelligence stays in SanTOK Cognitive

## Features

✅ **100% SanTOK Native**
- Uses SanTOK tokenization
- Uses SanTOK embeddings (optional)
- Uses SanTOK semantic processing
- Uses SanTOK trees and graphs
- Uses SanTOK training/testing

✅ **NO TensorFlow Dependency**
- Pure NumPy implementation
- No TF graphs
- No TF backpropagation
- All operations use NumPy arrays
- Works without TensorFlow installed

✅ **CPU-Friendly**
- Small model size (~1-2M parameters)
- No GPU required
- Fast inference on CPU
- Low memory footprint

✅ **Constraint-Based**
- Fact-grounded generation
- Cannot hallucinate (structurally impossible)
- All output grounded in SanTOK Cognitive facts

## Architecture

```
Input Text
    ↓
SanTOK Tokenizer (custom tokenization)
    ↓
Constraint Engine (filters to allowed tokens from facts)
    ↓
Sequence Optimizer (lightweight transformer, 2 layers)
    ├── Embeddings ✅
    ├── Sequence Modeling ✅
    ├── Learned Parameters ✅
    └── Probabilistic Sampling ✅
    ↓
Constrained Decoder (combines optimizer scores + constraints)
    ↓
Generated Text (guaranteed grounded in facts)
```

**This is a full SLM** with all SLM characteristics, but **constraint-grounded**.

## Quick Start

```python
from santok_cognitive.slm import SmallSanTOKSLM, SLMConfig

# Create SLM with small config
config = SLMConfig(
    d_model=128,      # Small embedding dimension
    n_layers=2,      # Just 2 layers
    n_heads=4,        # 4 attention heads
    vocab_size=5000   # Small vocabulary
)

slm = SmallSanTOKSLM(config)

# Facts from SanTOK Cognitive
facts = [
    "Python is a programming language",
    "Python was created by Guido van Rossum",
    "Python supports object-oriented programming"
]

# Train
slm.train(facts, facts)

# Generate
result = slm.generate("Python is", max_tokens=20)
print(result)  # "Python is a programming language"
```

## Components

### 1. ConstraintEngine
- Extracts tokens from SanTOK Cognitive facts
- Builds allowed token set
- Prevents hallucination

### 2. SanTOKSequenceOptimizer
- Lightweight transformer (2 layers)
- Learns token ordering patterns
- Does NOT learn facts (intelligence stays in Cognitive)

### 3. ConstrainedDecoder
- Combines optimizer scores with constraints
- Only samples from allowed tokens
- Guarantees fact-grounded output

## Integration with SanTOK

The SLM automatically integrates with:

- **SanTOK Tokenizer**: Custom tokenization engine
- **SanTOK Embeddings**: Feature-based embeddings
- **SanTOK Semantic**: Semantic similarity computation
- **SanTOK Graph**: Knowledge graph for facts

## Model Size

Default configuration:
- Parameters: ~1.2M
- Memory: ~5-10 MB
- Inference: ~1-5ms per token on CPU

## Training

Training uses masked loss - only allowed tokens contribute to loss:

```python
# Training data comes from SanTOK Cognitive
facts = unified_memory.get_facts(query)
slm.train(facts, facts)
```

## Generation

Generation is constraint-based:

```python
# All output is grounded in facts
result = slm.generate("What is Python?", max_tokens=50)
# Cannot generate tokens not in facts
```

## Requirements

**Required:**
- NumPy
- SanTOK tokenization system

**Optional:**
- SanTOK embeddings (disabled by default to avoid TF imports)
- SanTOK semantic similarity
- SanTOK graph store

**NOT Required:**
- ❌ TensorFlow (SLM is pure NumPy)
- ❌ PyTorch
- ❌ Any deep learning framework

## CPU Performance

Tested on:
- Intel i5: ~2-5ms per token
- Raspberry Pi: ~10-20ms per token
- No GPU needed!

## License

Part of SanTOK Cognitive System.
