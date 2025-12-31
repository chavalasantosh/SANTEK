# SanTOK 60K Vocabulary Language Model Training

## 🎯 Goal

Build a **complete language model** (like GPT-2) using **ONLY SanTOK**:
- ✅ 60K vocabulary from SanTOK tokens
- ✅ SanTOK embeddings (feature-based or semantic)
- ✅ SanTOK tokenization
- ✅ Transformer architecture (pure NumPy)
- ❌ NO external models
- ❌ NO pretrained algorithms
- ❌ NO external tokenizers

## 📋 Complete Pipeline

### Step 1: Download Datasets

```bash
python -m src.training.dataset_downloader
```

Downloads free datasets:
- **Wikipedia** (1GB) - General knowledge
- **OpenWebText** - Internet text (GPT-2 dataset)
- **CC-News** - Clean news articles
- **Custom data** - Your domain-specific text

### Step 2: Build 60K Vocabulary

```bash
python -m src.training.vocabulary_builder
```

Builds vocabulary from SanTOK tokens:
- Tokenizes all text with SanTOK
- Counts token frequencies
- Selects top 60K most frequent tokens
- Creates token-to-ID mapping

### Step 3: Train Language Model

```bash
python examples/train_santok_60k_vocab.py
```

Trains GPT-2 style model:
- Uses SanTOK vocabulary
- Uses SanTOK embeddings
- Transformer architecture (12 layers, 12 heads)
- Trains on your data

## 🚀 Quick Start

```python
from src.training import (
    SanTOKDatasetDownloader,
    SanTOKVocabularyBuilder,
    SanTOKLanguageModel,
    SanTOKLanguageModelTrainer
)

# 1. Download datasets
downloader = SanTOKDatasetDownloader()
wikipedia = downloader.download_wikipedia(size_limit_gb=1.0)
combined = downloader.combine_datasets()

# 2. Build vocabulary
vocab_builder = SanTOKVocabularyBuilder(vocab_size=60000)
vocab_builder.build_vocabulary(combined)
vocab_builder.save(Path("models/santok_60k_vocab.pkl"))

# 3. Train model
model = SanTOKLanguageModel(
    vocab_size=60000,
    embedding_dim=768,
    num_layers=12,
    num_heads=12
)

trainer = SanTOKLanguageModelTrainer(model, vocab_builder)
trainer.train(combined, epochs=10)
```

## 📊 Architecture

```
Input Text
    ↓
SanTOK Tokenization (word, char, grammar, etc.)
    ↓
60K Vocabulary (token → ID mapping)
    ↓
SanTOK Embeddings (feature-based or semantic)
    ↓
Transformer Layers (12 layers, 12 heads)
    ↓
Output Projection
    ↓
Next Token Prediction
```

## 🎓 What Makes This Different?

### Traditional Approach:
- Uses BPE/WordPiece tokenization (external)
- Uses pretrained embeddings (BERT, GPT-2)
- Uses external vocabulary

### SanTOK Approach:
- ✅ Uses SanTOK tokenization (your own)
- ✅ Uses SanTOK embeddings (your own)
- ✅ Uses SanTOK vocabulary (your own)
- ✅ 100% end-to-end SanTOK

## 📁 Files

- `dataset_downloader.py` - Download free datasets
- `vocabulary_builder.py` - Build 60K vocab from SanTOK tokens
- `language_model_trainer.py` - Train GPT-2 style model
- `train_santok_60k_vocab.py` - Complete pipeline

## 🔧 Requirements

```bash
pip install numpy tqdm requests
```

Optional (for faster processing):
```bash
pip install scipy
```

## 📈 Expected Results

After training:
- **Vocabulary**: 60,000 SanTOK tokens
- **Model size**: ~500MB (12 layers, 768 dim)
- **Training time**: 4-8 hours (on CPU, 1GB data)
- **Generation**: Can generate text like GPT-2

## 🎯 Next Steps

1. **Download datasets** (Wikipedia, OpenWebText, CC-News)
2. **Build vocabulary** (60K tokens from SanTOK)
3. **Train model** (10-20 epochs)
4. **Generate text** (use trained model)

## 💡 Tips

- Start with **1GB Wikipedia** to test
- Use **feature_based** embeddings (faster)
- Train for **10-20 epochs** for good results
- Add **your own domain data** for better performance

---

**This is YOUR model. Built with YOUR tokenizer. Trained on YOUR data.**

