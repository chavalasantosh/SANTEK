# SanTOK Integration Module

## Overview

This module solves the **critical vocabulary compatibility issue** between SanTOK and pretrained transformer models.

**The Problem:** SanTOK generates its own token IDs (UIDs, frontend digits, backend numbers) that don't match pretrained model vocabularies. Feeding SanTOK IDs directly to a pretrained model's embedding layer produces incorrect results.

**The Solution:** This module provides vocabulary adapters that map SanTOK token strings to standard model vocabulary IDs.

## Quick Start

```python
from src.core.core_tokenizer import run_once
from src.integration.vocabulary_adapter import quick_convert_santok_to_model_ids

# 1. Tokenize with SanTOK
text = "Hello world! SanTOK is amazing."
santok_result = run_once(text, seed=42, embedding_bit=False)

# 2. Extract tokens
tokens = [rec["text"] for rec in santok_result["word"]["records"]]

# 3. Convert to model vocabulary IDs
model_ids = quick_convert_santok_to_model_ids(tokens, model_name="bert-base-uncased")

# Now use model_ids with any BERT model!
```

## Installation

```bash
# Required for vocabulary adapter
pip install transformers

# Optional: For model inference
pip install torch  # or tensorflow
```

## Usage

### Basic Usage: Quick Conversion

```python
from src.integration.vocabulary_adapter import quick_convert_santok_to_model_ids

santok_tokens = ["hello", "world", "!"]
model_ids = quick_convert_santok_to_model_ids(santok_tokens, model_name="bert-base-uncased")
```

### Advanced Usage: Full Converter

```python
from src.core.core_tokenizer import run_once
from src.integration.vocabulary_adapter import SanTOKToModelConverter

# Tokenize with SanTOK
santok_result = run_once("Hello world!", seed=42, embedding_bit=False)

# Convert to model format
converter = SanTOKToModelConverter(model_name="bert-base-uncased")
result = converter.convert_santok_result(santok_result, tokenizer_type="word")

# Access results
print(result["model_input_ids"])      # Model vocabulary IDs
print(result["santok_tokens"])        # Original SanTOK tokens
print(result["santok_frontend_digits"])  # SanTOK metadata preserved
```

### Using with Pretrained Models

```python
from src.integration.vocabulary_adapter import SanTOKToModelConverter
from transformers import AutoModel

# 1. Tokenize and convert
converter = SanTOKToModelConverter(model_name="bert-base-uncased")
model_inputs = converter.prepare_for_inference(
    santok_result,
    tokenizer_type="word",
    return_tensors="pt"
)

# 2. Load model and run inference
model = AutoModel.from_pretrained("bert-base-uncased")
outputs = model(**model_inputs)
```

## API Reference

### `VocabularyAdapter`

Maps SanTOK tokens to model vocabulary IDs.

```python
adapter = VocabularyAdapter(model_name="bert-base-uncased")
result = adapter.map_santok_tokens_to_model_ids(santok_tokens)
```

**Methods:**
- `map_santok_tokens_to_model_ids(tokens)`: Map tokens to model vocabulary IDs
- `get_model_embedding_layer_info()`: Get embedding layer metadata

### `SanTOKToModelConverter`

High-level converter for SanTOK results.

```python
converter = SanTOKToModelConverter(model_name="bert-base-uncased")
result = converter.convert_santok_result(santok_result, tokenizer_type="word")
model_inputs = converter.prepare_for_inference(santok_result, tokenizer_type="word")
```

**Methods:**
- `convert_santok_result(santok_result, tokenizer_type)`: Convert SanTOK result to model format
- `prepare_for_inference(santok_result, tokenizer_type, return_tensors)`: Prepare tensors for model inference

### `quick_convert_santok_to_model_ids()`

Quick conversion function.

```python
model_ids = quick_convert_santok_to_model_ids(tokens, model_name="bert-base-uncased")
```

## Supported Models

Works with any HuggingFace model:

- **BERT**: `bert-base-uncased`, `bert-large-uncased`
- **GPT**: `gpt2`, `gpt2-medium`, `gpt2-large`
- **T5**: `t5-small`, `t5-base`, `t5-large`
- **RoBERTa**: `roberta-base`, `roberta-large`
- **DistilBERT**: `distilbert-base-uncased`
- **And 100+ more models...**

## Important Notes

⚠️ **Subword Tokenization**: If the model uses subword tokenization (BPE, WordPiece), a single SanTOK token may map to multiple model tokens.

⚠️ **Token Alignment**: The mapping between SanTOK tokens and model tokens may not be 1:1. Check the `token_mapping` field in results.

✅ **Metadata Preserved**: SanTOK's frontend digits, backend numbers, and other metadata are preserved in conversion results.

## Examples

See `examples/integration_with_transformers.py` for complete examples including:
- Basic mapping
- Full conversion with metadata
- Model inference
- Multiple models
- Different tokenization strategies

## Documentation

For detailed explanation of the vocabulary compatibility issue, see:
- `docs/VOCABULARY_COMPATIBILITY_ISSUE.md` - Complete guide

## License

Same as SanTOK project.

