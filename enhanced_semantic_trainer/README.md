# Enhanced SanTOK Semantic Trainer

God-tier semantic embedding system that leverages ALL unique SanTOK features.

## Features

1. **Multi-Stream Hierarchical Learning** - Learn semantics at char, subword, word simultaneously
2. **Deterministic UID Semantic Graph** - Persistent semantic relationships based on UIDs
3. **Content-ID Clustering** - Deterministic semantic grouping using content_id
4. **Mathematical Property Integration** - Use frontend/backend/global_id as semantic signals
5. **Temporal/Sequential Semantics** - Position-dependent embeddings, semantic flow modeling
6. **Cross-Stream Alignment** - Align semantics between different granularities
7. **Source-Aware Multi-Space** - Different semantic spaces for different sources

## Usage

```python
from enhanced_semantic_trainer import EnhancedSanTOKSemanticTrainer
from src.core.core_tokenizer import TextTokenizer

# Tokenize corpus
tokenizer = TextTokenizer()
streams = tokenizer.build(your_text)

# Train enhanced embeddings
trainer = EnhancedSanTOKSemanticTrainer(
    embedding_dim=768,
    window_size=5,
    epochs=10,
    use_multi_stream=True,
    use_temporal=True,
    use_content_id_clustering=True,
    use_math_properties=True,
    use_cross_stream_alignment=True,
    use_deterministic_graph=True,
    use_source_aware=True
)

trainer.train(streams)
trainer.save("enhanced_model.pkl")

# Get embeddings
embedding = trainer.get_embedding(uid=12345)
```

## What Makes This Unique

- **Deterministic**: Same token = same UID = same embedding (always)
- **Multi-granularity**: Learns at all levels simultaneously
- **Temporal aware**: Understands semantic flow over sequences
- **Mathematically rich**: Incorporates token mathematical properties
- **Persistent graph**: Semantic relationships survive across runs
