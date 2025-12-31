# SANTEK = Structured Artificial Intelligence Technology Kernel
### SanTOK - Advanced Text Tokenization & Cognitive Processing Framework

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/chavalasantosh/SanTOK)
[![zread](https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM5ODQgNS4zMTM1NiAxNC4zOTg0IDQuOTYwMVYyLjI0MDFDMTQuMzk4NCAxLjg4NjY0IDE0LjExMTkgMS42MDAxIDEzLjc1ODQgMS42MDAxWiIgZmlsbD0iI2ZmZiIvPgo8cGF0aCBkPSJNNCAxMkwxMiA0TDQgMTJaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00IDEyTDEyIDQiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K&logoColor=ffffff)](https://zread.ai/chavalasantosh/SANTEK)

**SanTOK** is a comprehensive, production-ready text processing and cognitive reasoning framework that goes far beyond simple tokenization. It provides a complete toolkit for text analysis, semantic understanding, model training, vector storage, API deployment, and deterministic reasoning.

---

## 📋 Table of Contents

- [Quick Start (5 Minutes)](#quick-start-5-minutes)
- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Model Learning & Development Process](#model-learning--development-process---complete-workflow)
- [How SanTOK Components Help Your Model](#how-santok-components-help-your-model---practical-benefits)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Components](#core-components)
- [Usage Examples](#usage-examples)
- [Advanced Examples & Use Cases](#advanced-examples--use-cases)
- [API Documentation](#api-documentation)
- [CLI Usage](#cli-usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Comparison with Alternatives](#comparison-with-alternatives)
- [Known Limitations](#known-limitations)
- [Best Practices & Recommendations](#best-practices--recommendations)
- [Roadmap & Future Plans](#roadmap--future-plans)
- [Version History](#version-history)
- [Migration Guide](#migration-guide)
- [Quick Reference / Cheat Sheet](#quick-reference--cheat-sheet)
- [Industry Use Cases & Applications](#industry-use-cases--applications)
- [FAQ](#frequently-asked-questions-faq)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Additional Resources](#additional-resources)
- [Support & Troubleshooting](#support--troubleshooting)

---

## ⚡ Quick Start (5 Minutes)

**Get SanTOK running in 5 minutes:**

```bash
# 1. Install
pip install -r requirements.txt

# 2. Basic tokenization
python -c "from santok import TextTokenizationEngine; engine = TextTokenizationEngine(); print(engine.tokenize('Hello World', 'word'))"

# 3. Start API server
python run.py

# 4. Test API
curl http://localhost:8000/api/v1/health
```

**Or use the CLI:**
```bash
python santok_cli.py tokenize "Hello World" --method word
```

**For detailed setup, see [Installation](#installation) section.**

---

## 🎯 Overview

SanTOK is a multi-layered framework consisting of three main components:

1. **SanTOK Core** - Advanced text tokenization engine with multiple methods, mathematical analysis, and statistical features
2. **SanTOK Cognitive** - Deterministic reasoning substrate for LLM-based systems with knowledge graphs and symbolic reasoning
3. **SanTOK Complete** - Comprehensive production system with embeddings, vector stores, training, and API servers

### What Makes SanTOK Unique?

- **Multiple Tokenization Methods**: 9+ tokenization strategies (word, character, subword, grammar-based, byte-level, etc.)
- **Deterministic Processing**: Same input always produces the same output with reproducible UIDs
- **Mathematical Analysis**: Advanced algorithms using digital roots, weighted sums, and 9-centric mathematics
- **Semantic Embeddings**: Multiple embedding strategies (feature-based, hash-based, semantic, hybrid)
- **Vector Database Integration**: Support for ChromaDB, FAISS, and Weaviate
- **Cognitive Reasoning**: Knowledge graphs, symbolic reasoning, and constraint enforcement
- **Production-Ready APIs**: FastAPI-based servers with WebSocket support
- **Training Capabilities**: Custom semantic model training on your data

---

## ✨ Key Features

### Core Tokenization
- ✅ **9+ Tokenization Methods**: Space, word, character, grammar, subword (BPE, frequency, syllable), byte-level
- ✅ **Mathematical Properties**: Frontend digits, backend numbers, global IDs, digital roots
- ✅ **Deterministic UIDs**: Xorshift64* based unique identifiers
- ✅ **Statistical Features**: Length factors, balance indices, entropy calculations
- ✅ **Preprocessing Options**: Case normalization, punctuation removal, repetition collapsing

### Semantic Processing
- ✅ **Multiple Embedding Strategies**: Feature-based, hash-based, semantic, hybrid
- ✅ **Semantic Training**: Train custom embeddings on your corpus
- ✅ **Enhanced Trainer**: Multi-stream hierarchical learning with temporal awareness
- ✅ **Vector Stores**: ChromaDB, FAISS, Weaviate integration
- ✅ **Inference Pipeline**: Production-ready embedding inference

### Cognitive Reasoning (SanTOK Cognitive)
- ✅ **Knowledge Graphs**: 15+ relation types (IS_A, PART_OF, CAUSES, USES, etc.)
- ✅ **Symbolic Reasoning**: 20+ inference rules (transitivity, inheritance, symmetry)
- ✅ **Knowledge Trees**: Hierarchical organization and taxonomies
- ✅ **Unified Memory**: Persistent memory system with graph linking
- ✅ **Constraint Enforcement**: LLM output validation against verified facts
- ✅ **Full Explainability**: Complete reasoning traces for every answer

### API & Deployment
- ✅ **FastAPI Servers**: Production-ready RESTful APIs
- ✅ **WebSocket Support**: Real-time tokenization and streaming
- ✅ **Interactive Documentation**: Auto-generated API docs at `/docs`
- ✅ **Job Management**: Async job processing with status tracking
- ✅ **Authentication**: JWT-based security
- ✅ **Cross-Platform**: Windows, Linux, macOS support

### Training & Models
- ✅ **Vocabulary Building**: Custom vocabulary construction
- ✅ **Language Model Training**: Train language models on your data
- ✅ **Small Language Models (SLM)**: Lightweight transformer-based models
- ✅ **Dataset Management**: Download and process training datasets

---

## 🏗️ Architecture

SanTOK follows a modular architecture with clear separation of concerns. Below is a detailed breakdown of each component's architecture.

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    SanTOK Framework                          │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ SanTOK Core  │  │ SanTOK       │  │ SanTOK       │      │
│  │              │  │ Cognitive    │  │ Complete     │      │
│  │ Tokenization │  │ Reasoning    │  │ Production   │      │
│  │ Engine       │  │ Substrate    │  │ System       │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         │                  │                  │             │
│         └──────────────────┼──────────────────┘             │
│                            │                                 │
│         ┌──────────────────▼──────────────────┐             │
│         │      API Servers & CLI Tools         │             │
│         └──────────────────────────────────────┘             │
│                            │                                 │
│         ┌──────────────────▼──────────────────┐             │
│         │   Vector Stores & Integrations       │             │
│         └──────────────────────────────────────┘             │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 Clean Architecture - Component Deep Dives

This section provides a clean, detailed view of each major component's architecture, showing how they work internally and how they integrate with the rest of the system.

---

## 🔤 Tokenization Architecture - Clean Face

### Overview

SanTOK's tokenization system is the foundation of all text processing. It provides 9 different tokenization methods, each producing deterministic, mathematically-rich token representations.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Tokenization Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Input Layer                             │    │
│  │  - Raw text string                                   │    │
│  │  - Optional: source tag, language hint               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Preprocessing Pipeline                        │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Normalize    │→ │ Remove       │                │    │
│  │  │ Case         │  │ Punctuation  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Normalize    │→ │ Detect       │                │    │
│  │  │ Whitespace   │  │ Language     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      Parallel Tokenization (9 Methods)              │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐           │    │
│  │  │  Space   │ │  Word    │ │  Char    │           │    │
│  │  │Tokenizer │ │Tokenizer │ │Tokenizer │           │    │
│  │  └──────────┘ └──────────┘ └──────────┘           │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐           │    │
│  │  │ Grammar  │ │ Subword  │ │  Byte    │           │    │
│  │  │Tokenizer │ │Tokenizer │ │Tokenizer │           │    │
│  │  └──────────┘ └──────────┘ └──────────┘           │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐           │    │
│  │  │   BPE    │ │ Syllable │ │Frequency │           │    │
│  │  │Tokenizer │ │Tokenizer │ │Tokenizer │           │    │
│  │  └──────────┘ └──────────┘ └──────────┘           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      Mathematical Enrichment Layer                   │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ UID          │→ │ Frontend     │                │    │
│  │  │ Generation   │  │ Digit Calc   │                │    │
│  │  │(Xorshift64*) │  │(9-centric)   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Backend      │→ │ Global ID    │                │    │
│  │  │ Number       │  │ Assignment   │                │    │
│  │  │ Composition  │  │              │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Neighbor     │→ │ Content ID   │                │    │
│  │  │ UID Linking  │  │ Generation   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      Statistical Analysis                             │    │
│  │  - Length Factor (token count % 10)                  │    │
│  │  - Balance Index (mean of frontend digits)           │    │
│  │  - Entropy Index (variance of frontend digits)       │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      TokenStream Output                               │    │
│  │  - TokenRecord objects with all properties            │    │
│  │  - Organized by tokenization method                   │    │
│  │  - Ready for embedding generation                    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Token Processing Flow

```
Input: "Hello World"
    ↓
[Preprocessing]
    normalize_case() → "hello world"
    normalize_whitespace() → "hello world"
    detect_language() → "en"
    ↓
[Tokenization - Word Method]
    tokenize_word() → ["Hello", "World"]
    ↓
[UID Assignment]
    assign_uids(seed=42) → 
        "Hello" → UID: 12345678901234567890
        "World" → UID: 98765432109876543210
    ↓
[Mathematical Properties]
    Frontend Digits:
        "Hello" → 5 (9-centric calculation)
        "World" → 6
    Backend Numbers:
        "Hello" → 12345 (composite calculation)
        "World" → 67890
    Global IDs:
        "Hello" → 1001
        "World" → 1002
    ↓
[Neighbor Linking]
    "Hello".prev_uid = None
    "Hello".next_uid = 98765432109876543210
    "World".prev_uid = 12345678901234567890
    "World".next_uid = None
    ↓
[TokenRecord Creation]
    TokenRecord(
        text="Hello",
        uid=12345678901234567890,
        index=0,
        frontend_digit=5,
        backend_number=12345,
        global_id=1001,
        prev_uid=None,
        next_uid=98765432109876543210,
        content_id=hash("Hello")
    )
    ↓
[TokenStream]
    TokenStream(
        name="word",
        tokens=[TokenRecord("Hello"), TokenRecord("World")]
    )
```

### TokenRecord Structure

```python
TokenRecord:
    text: str                    # Original token text
    uid: int                     # Unique identifier (64-bit)
    index: int                   # Position in sequence
    frontend_digit: int          # 9-centric digit (1-9)
    backend_number: int          # Composite number
    global_id: int               # Global sequence ID
    content_id: int              # Content-based hash
    prev_uid: Optional[int]      # Previous token UID
    next_uid: Optional[int]       # Next token UID
    stream_type: str             # Tokenization method
    metadata: dict               # Additional properties
```

### Key Features

- **Deterministic**: Same input + seed = same output
- **Parallel Processing**: All 9 methods run simultaneously
- **Mathematical Richness**: Every token has 5+ mathematical properties
- **Multi-language**: Automatic language detection
- **Source Tracking**: Optional source tags for provenance

---

## 🧮 Embeddings Architecture - Clean Face

### Overview

SanTOK's embedding system converts tokenized text into dense vector representations suitable for machine learning, similarity search, and semantic analysis.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Embeddings Architecture                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  TokenRecord Input                                            │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Strategy Router                              │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐           │    │
│  │  │ Feature  │ │ Semantic │ │   Hash   │           │    │
│  │  │  Based   │ │ (Trained)│ │  Based   │           │    │
│  │  └──────────┘ └──────────┘ └──────────┘           │    │
│  │  ┌──────────┐                                      │    │
│  │  │  Hybrid  │                                      │    │
│  │  │(Combined)│                                      │    │
│  │  └──────────┘                                      │    │
│  └──────────────┬──────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      Feature Extraction (All Strategies)            │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ UID Features │  │ Text Features│                │    │
│  │  │ - 64-bit → 8 │  │ - Length     │                │    │
│  │  │   bytes      │  │ - Char freq  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Math Features│  │ Stream Features│               │    │
│  │  │ - Frontend   │  │ - Type (one-hot)│              │    │
│  │  │ - Backend    │  │ - Position     │              │    │
│  │  │ - Global ID  │  │                │              │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────┬──────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      Strategy-Specific Processing                    │    │
│  │                                                       │    │
│  │  [Feature-Based]                                     │    │
│  │    Features → Concatenate → Project → Normalize     │    │
│  │                                                       │    │
│  │  [Semantic]                                          │    │
│  │    UID → Lookup in trained model → Embedding         │    │
│  │                                                       │    │
│  │  [Hash-Based]                                        │    │
│  │    Text+UID → Hash → Vector → Normalize             │    │
│  │                                                       │    │
│  │  [Hybrid]                                            │    │
│  │    Text Embedding + Feature Embedding → Weighted    │    │
│  │                                                       │    │
│  └──────────────┬──────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      Dimension Projection                            │    │
│  │  - Project to target dimension (default: 768)        │    │
│  │  - L2 normalization                                   │    │
│  │  - Type conversion (float32)                          │    │
│  └──────────────┬──────────────────────────────────────┘    │
│                 ↓                                           │
│  Embedding Vector (numpy.ndarray, shape: (embedding_dim,)) │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Embedding Strategies Deep Dive

#### 1. Feature-Based Strategy

```
TokenRecord
    ↓
Extract Features:
    - UID bytes: [0.12, 0.34, 0.56, ...] (8 floats)
    - Frontend digit: [0.56] (1 float, normalized)
    - Backend number: [0.78] (1 float, normalized)
    - Global ID: [0.90] (1 float, normalized)
    - Text length: [0.05] (1 float, normalized)
    - Character frequencies: [0.1, 0.2, ...] (26 floats)
    - Stream type: [0, 1, 0, ...] (9 floats, one-hot)
    ↓
Concatenate → Feature Vector (47 floats)
    ↓
Linear Projection Matrix (47 × 768)
    ↓
Embedding Vector (768 floats)
    ↓
L2 Normalize
    ↓
Final Embedding
```

#### 2. Semantic Strategy

```
TokenRecord
    ↓
Extract UID: 12345678901234567890
    ↓
Lookup in Trained Model:
    vocab[uid] → index: 42
    ↓
Retrieve Embedding:
    embeddings[42] → [0.1, 0.2, ..., 0.9] (768 floats)
    ↓
Final Embedding (already normalized from training)
```

#### 3. Hash-Based Strategy

```
TokenRecord
    ↓
Combine: text + str(uid)
    ↓
Hash Function (SHA256)
    ↓
Convert to Vector:
    hash_bytes → [0-255] → normalize to [0-1]
    ↓
Repeat/Interpolate to 768 dimensions
    ↓
L2 Normalize
    ↓
Final Embedding
```

#### 4. Hybrid Strategy

```
TokenRecord
    ↓
    ├─→ Text Embedding (optional, from sentence-transformers)
    │   └─→ [0.1, 0.2, ..., 0.9] (768 floats)
    │
    └─→ Feature Embedding (always)
        └─→ [0.2, 0.3, ..., 0.8] (768 floats)
    ↓
Weighted Combination:
    embedding = α × text_emb + (1-α) × feature_emb
    (default: α = 0.5)
    ↓
L2 Normalize
    ↓
Final Embedding
```

### Batch Processing

```
List[TokenRecord]
    ↓
[Parallel Processing]
    Split into chunks
    Process chunks in parallel (multiprocessing)
    ↓
[Feature Extraction]
    Extract features for all tokens
    ↓
[Vector Generation]
    Generate embeddings for all tokens
    ↓
[Stacking]
    Stack into matrix: (N, embedding_dim)
    ↓
Output: numpy.ndarray
```

---

## 🧠 Semantic Architecture - Clean Face

### Overview

SanTOK's semantic system learns meaningful representations from token co-occurrence patterns, context relationships, and mathematical properties without requiring pre-trained models.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Semantic System Architecture                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Training Corpus                                             │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Tokenization Phase                            │    │
│  │  - TextTokenizer.build()                             │    │
│  │  - Multiple token streams                            │    │
│  │  - TokenRecord creation                              │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Vocabulary Building                           │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Count        │→ │ Filter       │                │    │
│  │  │ Frequencies  │  │ (min_count)  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Sort by      │→ │ Create       │                │    │
│  │  │ Frequency    │  │ UID→Index    │                │    │
│  │  └──────────────┘  │ Mapping      │                │    │
│  │                    └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Co-occurrence Matrix Construction            │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Build        │→ │ Context      │                │    │
│  │  │ Context      │  │ Windows      │                │    │
│  │  │ Windows      │  │ (size=5)     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Count        │→ │ Create       │                │    │
│  │  │ Co-occurrence│  │ Sparse       │                │    │
│  │  │ Pairs        │  │ Matrix       │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Embedding Initialization                     │    │
│  │  - Random initialization (normal distribution)       │    │
│  │  - Token embeddings: (vocab_size, embedding_dim)     │    │
│  │  - Context embeddings: (vocab_size, embedding_dim)  │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Training Loop (Epochs)                       │    │
│  │  For each epoch:                                     │    │
│  │    ┌─────────────────────────────────────┐          │    │
│  │    │ Sample Training Pairs                │          │    │
│  │    │ - Positive: co-occurring tokens      │          │    │
│  │    │ - Negative: random tokens            │          │    │
│  │    └──────────────┬──────────────────────┘          │    │
│  │                   ↓                                  │    │
│  │    ┌─────────────────────────────────────┐          │    │
│  │    │ Forward Pass                         │          │    │
│  │    │ - Dot product: token_emb · ctx_emb   │          │    │
│  │    │ - Apply sigmoid                      │          │    │
│  │    │ - Compute loss (binary cross-entropy)│          │    │
│  │    └──────────────┬──────────────────────┘          │    │
│  │                   ↓                                  │    │
│  │    ┌─────────────────────────────────────┐          │    │
│  │    │ Backward Pass                        │          │    │
│  │    │ - Compute gradients                  │          │    │
│  │    │ - Update embeddings (SGD)            │          │    │
│  │    └──────────────────────────────────────┘          │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Model Saving                                 │    │
│  │  - Save token embeddings                             │    │
│  │  - Save vocabulary mapping                           │    │
│  │  - Save metadata (dim, vocab_size, etc.)             │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Enhanced Semantic Training (Multi-Stream)

```
Multiple Token Streams
    ├─ char stream: [c, h, e, l, l, o, ...]
    ├─ subword stream: [hel, lo, wor, ld, ...]
    └─ word stream: [hello, world, ...]
        ↓
[Multi-Stream Learning]
    Learn embeddings at all granularities simultaneously
    Cross-stream alignment:
        - Align char → subword → word
        - Hierarchical semantic relationships
    ↓
[Temporal Awareness]
    Position-dependent embeddings:
        - Early tokens: different semantics
        - Middle tokens: context-aware
        - Late tokens: summary semantics
    ↓
[Content-ID Clustering]
    Group tokens by content_id:
        - Deterministic semantic clusters
        - Similar content → similar embeddings
    ↓
[Mathematical Property Integration]
    Incorporate frontend/backend/global_id:
        - Mathematical relationships → semantic signals
        - UID-based semantic graph
    ↓
Enhanced Multi-Granularity Embeddings
```

### Semantic Relationships Captured

1. **Co-occurrence**: Tokens appearing together
2. **Context**: Neighbor relationships
3. **Content Similarity**: Same content_id → similar meaning
4. **Temporal**: Position-dependent semantics
5. **Hierarchical**: Char → Subword → Word relationships
6. **Mathematical**: UID-based relationships

---

## 🧠 Model Learning & Development Process - Complete Workflow

### How Models Learn in SanTOK

SanTOK models learn through **self-supervised learning** using SanTOK's unique mathematical properties. The learning process is transparent, deterministic, and explainable.

---

### 📚 Phase 1: Vocabulary Building (Foundation)

**Purpose**: Create a deterministic vocabulary from your text corpus using SanTOK tokenization.

**Step-by-Step Process**:

```
1. Text Corpus Input
   └─ Raw text files (any size)
       ↓
2. SanTOK Tokenization
   └─ Tokenize using SanTOK (word/char/subword)
   └─ Extract UIDs, frontend digits, backend numbers
   └─ Build TokenRecord objects
       ↓
3. Token Counting & Frequency Analysis
   └─ Count occurrences of each unique token
   └─ Track token metadata (UID, frontend, backend, content_id)
   └─ Filter by minimum frequency threshold
       ↓
4. Vocabulary Construction
   └─ Select top N tokens (default: 60,000)
   └─ Assign sequential IDs to tokens
   └─ Create token_to_id and id_to_token mappings
   └─ Store special tokens (<PAD>, <UNK>, <BOS>, <EOS>, <MASK>)
       ↓
5. Vocabulary Persistence
   └─ Save vocabulary to disk (pickle + JSON)
   └─ Ready for model training
```

**What the Model Learns at This Stage**:
- ✅ Token frequency distributions
- ✅ Token relationships (through UIDs)
- ✅ Mathematical properties (frontend/backend numbers)
- ✅ Content similarity (content_id clustering)

**Example Output**:
```
Building SanTOK Vocabulary (60K)
============================================================
[Pass 1] Tokenizing text and counting vocabulary tokens...
  ✓ Found 1,234,567 unique tokens
  Total token occurrences: 45,678,901
  After filtering (min_freq=2): 987,654 tokens

[Pass 2] Creating 60K vocabulary from token frequencies...
  ✓ Vocabulary built!
  Total vocabulary size: 60,000
  Special tokens: 5
  Regular tokens: 59,995
```

---

### 🎯 Phase 2: Semantic Embedding Training (Understanding)

**Purpose**: Train embeddings that capture semantic relationships between tokens.

**Step-by-Step Learning Process**:

```
1. Token Stream Preparation
   └─ Load tokenized data with TokenRecords
   └─ Extract UIDs, neighbors (prev_uid, next_uid)
   └─ Group by stream type (char, subword, word)
       ↓
2. Vocabulary Building for Embeddings
   └─ Create UID-based vocabulary
   └─ Filter by minimum count
   └─ Initialize random embeddings (vocab_size × embedding_dim)
       ↓
3. Co-occurrence Matrix Construction
   └─ Build context windows (default: ±5 tokens)
   └─ Track which tokens appear together
   └─ Use SanTOK's neighbor structure:
       • prev_uid → immediate predecessor
       • next_uid → immediate successor
       • content_id → semantic similarity
       • Same stream → contextual relationships
   └─ Create sparse/dense co-occurrence matrix
       ↓
4. Training Loop (Epochs)
   For each epoch:
   ├─ Positive Sampling
   │  └─ Sample co-occurring token pairs
   │  └─ Update embeddings to increase similarity
   │  └─ Use gradient descent:
   │     • Compute dot product (similarity)
   │     • Apply sigmoid activation
   │     • Calculate loss (cross-entropy)
   │     • Update embeddings: emb += lr * gradient
   │
   ├─ Negative Sampling
   │  └─ Sample random non-co-occurring pairs
   │  └─ Update embeddings to decrease similarity
   │  └─ 5 negative samples per positive
   │
   └─ Embedding Normalization
      └─ L2 normalize embeddings every 2 epochs
      └─ Maintain unit vectors
       ↓
5. Model Convergence
   └─ Loss decreases over epochs
   └─ Embeddings capture semantic relationships
   └─ Similar tokens have similar embeddings
```

**What the Model Learns**:
- ✅ **Semantic Similarity**: Tokens with similar meanings cluster together
- ✅ **Contextual Relationships**: Tokens that appear together get closer embeddings
- ✅ **Hierarchical Structure**: Multi-stream learning captures different granularities
- ✅ **Temporal Patterns**: Position-dependent semantics
- ✅ **Content Clustering**: Tokens with similar content_id cluster together

**Learning Metrics**:
```python
Epoch 1/10: Loss = 2.3456  # High loss - random embeddings
Epoch 2/10: Loss = 1.8923  # Learning patterns
Epoch 3/10: Loss = 1.4567  # Improving
Epoch 4/10: Loss = 1.1234  # Good progress
...
Epoch 10/10: Loss = 0.5678  # Converged - model learned!
```

**Visual Learning Progress**:
```
Initial State (Random):
  "cat"    → [0.12, -0.45, 0.78, ...]  (random)
  "dog"    → [-0.23, 0.67, -0.12, ...]  (random)
  "car"    → [0.34, -0.56, 0.89, ...]  (random)
  
After Training:
  "cat"    → [0.45, 0.23, 0.12, ...]  (learned)
  "dog"    → [0.42, 0.25, 0.15, ...]  (similar to cat!)
  "car"    → [-0.12, 0.78, -0.34, ...]  (different from cat/dog)
  
Similarity Scores:
  cat-dog:  0.87  (high - learned they're similar!)
  cat-car:  0.12  (low - learned they're different)
```

---

### 🚀 Phase 3: Language Model Training (Generation)

**Purpose**: Train a GPT-2 style language model to predict next tokens.

**Step-by-Step Learning Process**:

```
1. Data Preparation
   └─ Encode text to token IDs using vocabulary
   └─ Create sequences of fixed length (default: 512)
   └─ Split into input/target pairs:
      Input:  [token_1, token_2, ..., token_n]
      Target: [token_2, token_3, ..., token_n+1]
       ↓
2. Model Architecture Initialization
   └─ Token embeddings (vocab_size × embedding_dim)
   └─ Position embeddings (max_seq_length × embedding_dim)
   └─ Transformer layers (12 layers, 12 heads each):
      • Self-attention (Q, K, V projections)
      • Feed-forward networks
      • Layer normalization
   └─ Output projection (embedding_dim × vocab_size)
       ↓
3. Training Loop (Epochs)
   For each epoch:
   ├─ Batch Creation
   │  └─ Shuffle training sequences
   │  └─ Create batches (default: 32 sequences)
   │
   ├─ Forward Pass
   │  └─ Embed tokens: token_emb + pos_emb
   │  └─ Pass through transformer layers:
   │     • Multi-head self-attention
   │     • Feed-forward networks
   │     • Residual connections
   │     • Layer normalization
   │  └─ Generate logits (vocab_size probabilities)
   │
   ├─ Loss Calculation
   │  └─ Cross-entropy loss:
   │     loss = -log(prob[target_token])
   │  └─ Average over all positions in sequence
   │
   └─ Weight Updates
      └─ Compute gradients (backpropagation)
      └─ Update all weights:
         • Embedding weights
         • Attention weights (Q, K, V, O)
         • Feed-forward weights
         • Layer norm parameters
         • Output projection
       ↓
4. Model Checkpointing
   └─ Save model every N epochs
   └─ Store all weights and hyperparameters
   └─ Enable resuming training
       ↓
5. Convergence & Validation
   └─ Loss decreases: 6.0 → 2.0 → 1.5 → 1.2
   └─ Perplexity decreases (measure of uncertainty)
   └─ Model learns language patterns
```

**What the Model Learns**:
- ✅ **Next Token Prediction**: Learns to predict likely next tokens
- ✅ **Language Patterns**: Grammar, syntax, semantics
- ✅ **Context Understanding**: Uses previous tokens to predict next
- ✅ **Long-range Dependencies**: Attention mechanism captures relationships
- ✅ **Domain Knowledge**: Learns from training corpus

**Learning Progress Example**:
```
Epoch 1/10:
  Loss: 6.2345  (High - model is guessing randomly)
  Perplexity: 510.2  (Very uncertain)
  Sample: "The cat sat on the [random_word]"

Epoch 5/10:
  Loss: 2.1234  (Learning patterns)
  Perplexity: 8.4  (More confident)
  Sample: "The cat sat on the mat"  (Better!)

Epoch 10/10:
  Loss: 1.4567  (Converged)
  Perplexity: 4.3  (Confident predictions)
  Sample: "The cat sat on the mat and purred"  (Coherent!)
```

---

### 🧪 Phase 4: Testing & Validation (Quality Assurance)

**Purpose**: Verify the model learned correctly and is ready for use.

**Testing Process**:

```
1. Reconstruction Testing
   └─ Test: Tokenize → Reconstruct
   └─ Verify: Original text == Reconstructed text
   └─ Metric: 100% accuracy required
       ↓
2. Embedding Quality Testing
   └─ Test: Similar tokens have similar embeddings
   └─ Verify: Cosine similarity > 0.7 for related tokens
   └─ Metric: Semantic alignment score
       ↓
3. Language Model Testing
   ├─ Perplexity Testing
   │  └─ Measure model's uncertainty
   │  └─ Lower = better (model is confident)
   │
   ├─ Generation Quality
   │  └─ Generate text from prompts
   │  └─ Check: Coherence, grammar, relevance
   │
   └─ Next Token Prediction Accuracy
      └─ Test on held-out validation set
      └─ Measure: Top-1, Top-5, Top-10 accuracy
       ↓
4. Performance Testing
   └─ Speed: Tokens/second
   └─ Memory: RAM usage
   └─ Accuracy: Reconstruction rate
       ↓
5. Model Readiness Checklist
   ✅ Loss converged (< 2.0 for LM, < 1.0 for embeddings)
   ✅ Perplexity reasonable (< 10 for good models)
   ✅ Reconstruction accuracy = 100%
   ✅ Embedding similarity makes sense
   ✅ Generation quality acceptable
   ✅ Performance meets requirements
```

**Test Results Example**:
```
=== Model Testing Results ===

1. Reconstruction Test:
   ✓ Accuracy: 100.0% (Perfect!)
   ✓ All tokens correctly reconstructed

2. Embedding Quality:
   ✓ cat-dog similarity: 0.87 (High - correct!)
   ✓ cat-car similarity: 0.12 (Low - correct!)
   ✓ Semantic alignment: 0.82 (Good!)

3. Language Model:
   ✓ Perplexity: 4.3 (Excellent!)
   ✓ Top-1 accuracy: 45.2%
   ✓ Top-5 accuracy: 78.9%
   ✓ Top-10 accuracy: 89.3%

4. Performance:
   ✓ Speed: 1,234 tokens/second
   ✓ Memory: 2.3 GB
   ✓ Latency: 0.8ms per token

✅ MODEL READY FOR DEPLOYMENT!
```

---

### 📊 Model Learning Indicators

**How to Know Your Model is Learning**:

1. **Loss Decreasing**:
   ```
   Epoch 1: Loss = 6.23  ❌ (Random)
   Epoch 3: Loss = 3.45  ⚠️  (Learning)
   Epoch 5: Loss = 2.12  ✅ (Good progress)
   Epoch 10: Loss = 1.45 ✅ (Converged!)
   ```

2. **Perplexity Decreasing**:
   ```
   Epoch 1: Perplexity = 510.2  ❌ (Very uncertain)
   Epoch 5: Perplexity = 8.4    ✅ (Confident)
   Epoch 10: Perplexity = 4.3    ✅ (Very confident!)
   ```

3. **Embedding Similarity Makes Sense**:
   ```
   cat-dog: 0.87  ✅ (High - they're similar!)
   cat-car: 0.12  ✅ (Low - they're different!)
   python-code: 0.82  ✅ (High - related!)
   ```

4. **Generation Quality Improving**:
   ```
   Epoch 1: "The cat sat on the [random_word]"
   Epoch 5: "The cat sat on the mat"
   Epoch 10: "The cat sat on the mat and purred contentedly"
   ```

5. **Reconstruction Accuracy**:
   ```
   Always: 100% ✅ (SanTOK guarantees perfect reconstruction)
   ```

---

### 🎯 Model Readiness Checklist

**Your model is ready when**:

- ✅ **Loss converged**: Loss < 2.0 (language model) or < 1.0 (embeddings)
- ✅ **Perplexity reasonable**: < 10 for good models, < 5 for excellent
- ✅ **Reconstruction perfect**: 100% accuracy (always true for SanTOK)
- ✅ **Embedding quality**: Similarity scores make semantic sense
- ✅ **Generation coherent**: Generated text is grammatically correct
- ✅ **Performance acceptable**: Meets speed/memory requirements
- ✅ **Validation passed**: All tests pass

**Model NOT ready if**:
- ❌ Loss = 0.0000 (trivial memorization - dataset too small)
- ❌ Loss not decreasing (learning rate too high/low)
- ❌ Perplexity > 100 (model is guessing randomly)
- ❌ Generation is gibberish
- ❌ Embeddings don't capture semantics

---

### 🔬 Advanced Training Features

**Enhanced Semantic Trainer** (Multi-Stream Learning):

```
Multiple Token Streams
    ├─ char stream (character-level)
    ├─ subword stream (subword-level)
    └─ word stream (word-level)
        ↓
[Multi-Stream Learning]
    ├─ Learn at all granularities simultaneously
    ├─ Cross-stream alignment
    ├─ Hierarchical semantics
    └─ Unified embeddings
        ↓
Enhanced Embeddings
    └─ Capture semantics at multiple levels
    └─ Better generalization
    └─ Richer representations
```

**Key Learning Mechanisms**:

1. **Co-occurrence Learning**: Tokens appearing together get similar embeddings
2. **Negative Sampling**: Random tokens get pushed apart
3. **Gradient Descent**: Iteratively improve embeddings
4. **Normalization**: Maintain unit vectors for stability
5. **Multi-Stream Alignment**: Align semantics across granularities
6. **Temporal Patterns**: Learn position-dependent semantics
7. **Content Clustering**: Group tokens by content_id

---

### 🔄 Complete Training Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK Model Development Workflow                │
└─────────────────────────────────────────────────────────────┘

PHASE 1: Data Preparation
──────────────────────────
Raw Text Corpus
    ↓
[SanTOK Tokenization]
    ├─ Extract tokens
    ├─ Generate UIDs
    ├─ Calculate features
    └─ Create TokenRecords
    ↓
Tokenized Dataset
    ↓

PHASE 2: Vocabulary Building
─────────────────────────────
Tokenized Dataset
    ↓
[Vocabulary Builder]
    ├─ Count token frequencies
    ├─ Filter by min_frequency
    ├─ Select top 60K tokens
    ├─ Assign token IDs
    └─ Save vocabulary
    ↓
Vocabulary File (60K tokens)
    ↓

PHASE 3A: Semantic Embedding Training
───────────────────────────────────────
Tokenized Dataset + Vocabulary
    ↓
[Semantic Trainer]
    ├─ Build co-occurrence matrix
    │  └─ Use prev_uid, next_uid
    │  └─ Context windows
    │  └─ Content_id similarity
    ├─ Initialize random embeddings
    ├─ Training Loop (10 epochs):
    │  ├─ Positive sampling
    │  ├─ Negative sampling
    │  ├─ Gradient updates
    │  └─ Embedding normalization
    └─ Save trained embeddings
    ↓
Trained Embeddings Model
    ↓

PHASE 3B: Language Model Training
───────────────────────────────────
Tokenized Dataset + Vocabulary
    ↓
[Language Model Trainer]
    ├─ Encode to token IDs
    ├─ Create sequences
    ├─ Initialize transformer model
    ├─ Training Loop (10 epochs):
    │  ├─ Forward pass
    │  ├─ Loss calculation
    │  ├─ Backpropagation
    │  └─ Weight updates
    └─ Save trained model
    ↓
Trained Language Model
    ↓

PHASE 4: Testing & Validation
──────────────────────────────
Trained Models
    ↓
[Testing Suite]
    ├─ Reconstruction test
    ├─ Embedding quality test
    ├─ Generation quality test
    ├─ Performance benchmarks
    └─ Validation metrics
    ↓
Test Results Report
    ↓

PHASE 5: Model Deployment
─────────────────────────
Validated Models
    ↓
[Deployment]
    ├─ Load models
    ├─ Initialize inference pipeline
    ├─ API server (optional)
    └─ Production ready!
    ↓
🚀 DEPLOYED MODEL
```

---

## 🎯 How SanTOK Components Help Your Model - Practical Benefits

This section showcases **exactly how each SanTOK component contributes** to making your models better, faster, and more reliable.

---

### 🔤 How SanTOK Tokenization Helps Your Model

**What SanTOK Tokenization Provides**:
- ✅ Deterministic UIDs (same token = same UID always)
- ✅ Mathematical properties (frontend digits, backend numbers)
- ✅ Multiple granularities (char, subword, word)
- ✅ Perfect reversibility (100% reconstruction)
- ✅ Statistical features (entropy, balance, variance)

**How It Helps Your Model**:

#### 1. **Deterministic Foundation**
```
Without SanTOK:
  "cat" → random ID (different each time)
  Model confusion: Same word, different IDs

With SanTOK:
  "cat" → UID: 12345 (always the same)
  Model benefit: Consistent representation = better learning
```

**Impact**: Models learn faster because tokens have stable identities. No confusion from changing IDs.

#### 2. **Mathematical Relationships**
```
SanTOK provides:
  - Frontend digit (1-9): Semantic category
  - Backend number: Positional encoding
  - Global ID: Full context signature

Model uses these for:
  - Better feature engineering
  - Mathematical relationships between tokens
  - Deterministic clustering
```

**Impact**: Models can leverage mathematical properties for better understanding, not just raw text.

#### 3. **Multiple Granularities**
```
SanTOK provides 3 streams simultaneously:
  - Character level: "c", "a", "t"
  - Subword level: "cat"
  - Word level: "cat"

Model benefits:
  - Learn at all levels simultaneously
  - Better handling of rare words
  - Richer representations
```

**Impact**: Models understand text at multiple levels, improving generalization.

#### 4. **Perfect Reversibility**
```
SanTOK guarantee:
  Tokenize → Reconstruct = 100% accuracy

Model benefit:
  - No information loss
  - Can verify correctness
  - Trustworthy pipeline
```

**Impact**: Models built on SanTOK are reliable and verifiable.

**Real Example**:
```python
# Without SanTOK: Standard tokenizer
text = "Hello world"
tokens = ["Hello", "world"]  # Lost capitalization, punctuation info

# With SanTOK: Rich tokenization
text = "Hello world"
tokens = [
    TokenRecord(text="Hello", uid=12345, frontend=5, backend=678, ...),
    TokenRecord(text="world", uid=23456, frontend=6, backend=789, ...)
]
# Model gets: text + UID + mathematical properties + neighbors
```

**Result**: Model has **10x more information** per token, leading to better learning.

---

### 🧮 How SanTOK Embeddings Help Your Model

**What SanTOK Embeddings Provide**:
- ✅ Feature-based embeddings (from SanTOK properties)
- ✅ Semantic embeddings (self-trained, no external models)
- ✅ Hash-based embeddings (fast, deterministic)
- ✅ Hybrid embeddings (combines multiple strategies)

**How It Helps Your Model**:

#### 1. **No External Dependencies**
```
Without SanTOK:
  Model needs: BERT, Word2Vec, Sentence Transformers
  Problems: Large models, slow, requires internet

With SanTOK:
  Model gets: Self-trained embeddings from your data
  Benefits: Fast, lightweight, works offline
```

**Impact**: Models can be trained and deployed anywhere, no external dependencies.

#### 2. **Domain-Specific Learning**
```
SanTOK embeddings learn from YOUR data:
  - Medical text → medical embeddings
  - Code → code embeddings
  - Your domain → your embeddings

Standard embeddings:
  - Generic (trained on Wikipedia)
  - May not fit your domain
```

**Impact**: Models perform better on domain-specific tasks because embeddings match the domain.

#### 3. **Mathematical Property Integration**
```
SanTOK embeddings include:
  - UID relationships
  - Frontend/backend numbers
  - Content_id clustering
  - Neighbor relationships

Standard embeddings:
  - Only text similarity
  - No mathematical structure
```

**Impact**: Models can use mathematical relationships for better reasoning.

#### 4. **Multiple Embedding Strategies**
```
SanTOK provides 4 strategies:
  1. Feature-based: Fast, deterministic
  2. Semantic: Learned from data
  3. Hash-based: Ultra-fast, no training
  4. Hybrid: Best of all worlds

Model can choose based on:
  - Speed requirements
  - Accuracy needs
  - Resource constraints
```

**Impact**: Models can optimize for speed or accuracy as needed.

**Real Example**:
```python
# Standard embedding: Generic, slow
embedding = sentence_transformer.encode("cat")
# Time: 50ms, Size: 384 dim, Generic semantics

# SanTOK embedding: Domain-specific, fast
embedding = santok_embedding.generate("cat")
# Time: 2ms, Size: 768 dim, Your domain semantics
# Includes: UID relationships, mathematical properties
```

**Result**: Models get **faster, more accurate, domain-specific embeddings**.

---

### 🧠 How SanTOK Semantics Help Your Model

**What SanTOK Semantics Provide**:
- ✅ Self-supervised semantic learning
- ✅ Co-occurrence patterns
- ✅ Context windows
- ✅ Content-based clustering
- ✅ Multi-stream alignment

**How It Helps Your Model**:

#### 1. **Learns from Your Data**
```
SanTOK semantics:
  - Analyzes YOUR text corpus
  - Learns relationships in YOUR domain
  - Captures YOUR terminology

Standard semantics:
  - Pre-trained on generic data
  - May not understand your domain
```

**Impact**: Models understand your specific domain better.

#### 2. **Captures Contextual Relationships**
```
SanTOK learns:
  - Which tokens appear together
  - Context windows (neighbors)
  - Sequential patterns
  - Temporal relationships

Model uses for:
  - Better next-token prediction
  - Understanding context
  - Capturing dependencies
```

**Impact**: Models understand context and relationships, not just individual tokens.

#### 3. **Multi-Stream Semantic Alignment**
```
SanTOK provides:
  - Character-level semantics
  - Subword-level semantics
  - Word-level semantics
  - Cross-stream alignment

Model benefits:
  - Understands at all granularities
  - Better handling of rare words
  - Richer semantic understanding
```

**Impact**: Models have deeper semantic understanding across multiple levels.

#### 4. **Deterministic Semantic Graph**
```
SanTOK creates:
  - Persistent semantic relationships
  - UID-based semantic graph
  - Content_id clusters
  - Temporal patterns

Model uses for:
  - Consistent semantic understanding
  - Better generalization
  - Explainable semantics
```

**Impact**: Models have consistent, explainable semantic understanding.

**Real Example**:
```python
# Standard semantics: Generic
"Python" → generic programming language embedding

# SanTOK semantics: Domain-aware
"Python" → embedding that includes:
  - Co-occurrence with "code", "programming", "language"
  - Content_id cluster (programming concepts)
  - Temporal patterns (appears with "develop", "script")
  - Multi-stream alignment (char/subword/word levels)
```

**Result**: Models have **richer, domain-specific semantic understanding**.

---

### 💾 How SanTOK Vectors Help Your Model

**What SanTOK Vectors Provide**:
- ✅ Unified vector store interface
- ✅ Multiple backends (ChromaDB, FAISS, Weaviate)
- ✅ Efficient similarity search
- ✅ Metadata management
- ✅ Batch operations

**How It Helps Your Model**:

#### 1. **Fast Similarity Search**
```
SanTOK vectors:
  - Optimized similarity search
  - Sub-millisecond queries
  - Scales to millions of vectors

Standard approach:
  - Linear search (slow)
  - No optimization
  - Doesn't scale
```

**Impact**: Models can quickly find similar examples for few-shot learning, retrieval, etc.

#### 2. **Multiple Storage Backends**
```
SanTOK supports:
  - ChromaDB: Persistent, disk-based
  - FAISS: Fast, in-memory
  - Weaviate: Cloud-native, scalable

Model can choose:
  - Development: FAISS (fast)
  - Production: Weaviate (scalable)
  - Local: ChromaDB (simple)
```

**Impact**: Models can use the best storage for their use case.

#### 3. **Metadata Integration**
```
SanTOK vectors store:
  - Embeddings
  - Token metadata (UID, frontend, backend)
  - Source information
  - Timestamps
  - Custom tags

Model uses for:
  - Filtered searches
  - Source tracking
  - Temporal queries
```

**Impact**: Models can do sophisticated queries beyond simple similarity.

#### 4. **Batch Operations**
```
SanTOK vectors:
  - Batch insert (thousands at once)
  - Batch search (multiple queries)
  - Efficient updates

Standard approach:
  - One-by-one operations
  - Slow for large datasets
```

**Impact**: Models can efficiently work with large datasets.

**Real Example**:
```python
# Standard approach: Slow linear search
similar = find_similar(embedding)  # O(n) - scans all vectors

# SanTOK vectors: Fast indexed search
similar = vector_store.search(embedding, top_k=10)  # O(log n) - indexed
# Returns: Similar vectors + metadata + source info
```

**Result**: Models get **10-100x faster similarity search** with rich metadata.

---

### 🌳 How SanTOK Trees, Graphs & Reasoning Help Your Model

**What SanTOK Trees, Graphs & Reasoning Provide**:
- ✅ Knowledge graphs (nodes, edges, relations)
- ✅ Hierarchical trees (concepts, documents)
- ✅ Symbolic reasoning (20+ inference rules)
- ✅ Contradiction detection
- ✅ Confidence propagation

**How It Helps Your Model**:

#### 1. **Structured Knowledge**
```
SanTOK provides:
  - Knowledge graph: Relationships between concepts
  - Trees: Hierarchical organization
  - Reasoning: Logical inference

Model uses for:
  - Understanding relationships
  - Hierarchical concepts
  - Logical reasoning
```

**Impact**: Models can reason about structured knowledge, not just text.

#### 2. **Explainable Reasoning**
```
SanTOK reasoning:
  - Shows inference steps
  - Explains conclusions
  - Tracks confidence

Standard models:
  - Black box predictions
  - No explanation
  - Unclear reasoning
```

**Impact**: Models can explain their reasoning, crucial for trust and debugging.

#### 3. **Contradiction Detection**
```
SanTOK detects:
  - Conflicting information
  - Logical inconsistencies
  - Confidence conflicts

Model uses for:
  - Validating outputs
  - Preventing hallucinations
  - Ensuring consistency
```

**Impact**: Models can catch and prevent errors before they happen.

#### 4. **20+ Inference Rules**
```
SanTOK provides:
  - Transitivity: A→B, B→C → A→C
  - Inheritance: IS_A relationships
  - Symmetry: Bidirectional relations
  - And 17+ more rules

Model uses for:
  - Logical inference
  - Knowledge expansion
  - Relationship discovery
```

**Impact**: Models can make logical inferences, expanding knowledge automatically.

**Real Example**:
```python
# Standard model: Text-only
Question: "Is Python a programming language?"
Answer: "Yes" (but can't explain why)

# SanTOK reasoning: Structured knowledge
Question: "Is Python a programming language?"
Reasoning:
  1. Python IS_A programming language (fact)
  2. Therefore: Yes
  3. Confidence: 1.0 (certain)
  4. Explanation: Direct IS_A relationship
```

**Result**: Models can **reason logically and explain their answers**.

---

### 🧠 How SanTOK Cognitive Helps Your Model

**What SanTOK Cognitive Provides**:
- ✅ Deterministic reasoning substrate
- ✅ Knowledge representation
- ✅ Symbolic inference
- ✅ Constraint enforcement
- ✅ Full explainability

**How It Helps Your Model**:

#### 1. **System 2 for AI**
```
SanTOK Cognitive = System 2 (deliberate, correct)
LLMs = System 1 (fast, intuitive, error-prone)

Combined:
  - LLM generates fast responses
  - SanTOK validates and corrects
  - Best of both worlds
```

**Impact**: Models get the speed of LLMs with the correctness of symbolic reasoning.

#### 2. **Hallucination Prevention**
```
SanTOK Cognitive:
  - Validates against knowledge graph
  - Checks for contradictions
  - Enforces constraints

Standard models:
  - Can hallucinate
  - No validation
  - Unreliable outputs
```

**Impact**: Models produce reliable, validated outputs.

#### 3. **Constraint Enforcement**
```
SanTOK Cognitive:
  - Enforces domain constraints
  - Validates against rules
  - Prevents invalid outputs

Model uses for:
  - Safe generation
  - Compliance
  - Quality assurance
```

**Impact**: Models stay within safe, valid boundaries.

#### 4. **Full Explainability**
```
SanTOK Cognitive:
  - Shows reasoning trace
  - Explains every step
  - Provides confidence scores

Standard models:
  - Black box
  - No explanation
  - Unclear reasoning
```

**Impact**: Models are trustworthy and debuggable.

**Real Example**:
```python
# Standard LLM: Can hallucinate
Question: "What is the capital of France?"
Answer: "Paris" (correct, but can't explain)

# SanTOK Cognitive: Validated and explained
Question: "What is the capital of France?"
Answer: "Paris"
Reasoning:
  - France HAS_CAPITAL Paris (fact in knowledge graph)
  - Confidence: 1.0
  - Source: Knowledge graph node #12345
  - Validation: ✓ No contradictions found
```

**Result**: Models are **reliable, explainable, and validated**.

---

### 🤖 How SanTOK SLM (Small Language Model) Helps Your Model

**What SanTOK SLM Provides**:
- ✅ 100% SanTOK-native (no external AI)
- ✅ Constraint-grounded generation
- ✅ No hallucination
- ✅ Full explainability
- ✅ Lightweight and fast

**How It Helps Your Model**:

#### 1. **No External Dependencies**
```
SanTOK SLM:
  - Uses only SanTOK components
  - No BERT, GPT, or other models
  - Pure SanTOK tokenization + embeddings

Standard SLMs:
  - Require external models
  - Large dependencies
  - Complex setup
```

**Impact**: Models are self-contained and easy to deploy.

#### 2. **Constraint-Grounded Generation**
```
SanTOK SLM:
  - Generates within constraints
  - Validates against knowledge graph
  - Prevents invalid outputs

Standard SLMs:
  - Can generate anything
  - No validation
  - Unreliable
```

**Impact**: Models generate safe, valid outputs.

#### 3. **No Hallucination**
```
SanTOK SLM:
  - Only generates from learned knowledge
  - Validates against facts
  - No made-up information

Standard SLMs:
  - Can hallucinate
  - Make up facts
  - Unreliable
```

**Impact**: Models are trustworthy and factual.

#### 4. **Lightweight and Fast**
```
SanTOK SLM:
  - Small model size
  - Fast inference
  - Low memory usage

Standard SLMs:
  - Large models
  - Slow inference
  - High memory
```

**Impact**: Models can run on edge devices, mobile, etc.

**Real Example**:
```python
# Standard SLM: Large, slow, can hallucinate
model = load_pretrained_slm()  # 500MB, slow, unreliable

# SanTOK SLM: Small, fast, reliable
model = SanTOKSLMModel()  # 50MB, fast, validated
# Generates: Constraint-grounded, explainable, no hallucination
```

**Result**: Models are **lightweight, fast, and reliable**.

---

### 🧠 How SanTOK Memory Helps Your Model

**What SanTOK Memory Provides**:
- ✅ Unified memory system
- ✅ Vector + Graph + Tree storage
- ✅ Cross-store linking
- ✅ Temporal tracking
- ✅ Source awareness

**How It Helps Your Model**:

#### 1. **Unified Knowledge Storage**
```
SanTOK Memory:
  - Vector store: Similarity search
  - Graph store: Relationships
  - Tree store: Hierarchies
  - All linked together

Standard approach:
  - Separate stores
  - No integration
  - Fragmented knowledge
```

**Impact**: Models have unified, integrated knowledge.

#### 2. **Multi-Modal Retrieval**
```
SanTOK Memory:
  - Search by similarity (vector)
  - Search by relationship (graph)
  - Search by hierarchy (tree)
  - Combined searches

Standard approach:
  - Single search type
  - Limited retrieval
```

**Impact**: Models can retrieve knowledge in multiple ways.

#### 3. **Temporal Awareness**
```
SanTOK Memory:
  - Tracks when knowledge was added
  - Temporal relationships
  - Freshness scoring

Model uses for:
  - Recent information priority
  - Temporal reasoning
  - Knowledge evolution
```

**Impact**: Models understand time and can prioritize recent information.

#### 4. **Source Tracking**
```
SanTOK Memory:
  - Tracks source of each fact
  - Source-aware queries
  - Source-based filtering

Model uses for:
  - Attribution
  - Source verification
  - Quality control
```

**Impact**: Models can cite sources and verify information.

**Real Example**:
```python
# Standard memory: Single store
memory = vector_store  # Only similarity search

# SanTOK Memory: Unified system
memory = UnifiedMemory()
memory.add("Python is a language", source="wikipedia")
# Stored in: Vector store + Graph store + Tree store
# Linked together, with source tracking
```

**Result**: Models have **unified, multi-modal, source-aware memory**.

---

### 🔍 How SanTOK Interpretation Helps Your Model

**What SanTOK Interpretation Provides**:
- ✅ Real-time data interpretation
- ✅ Semantic relationship discovery
- ✅ Concept exploration
- ✅ Knowledge discovery
- ✅ Weaviate integration

**How It Helps Your Model**:

#### 1. **Real-Time Understanding**
```
SanTOK Interpretation:
  - Interprets data as it arrives
  - Finds semantic relationships
  - Discovers concepts

Standard approach:
  - Batch processing
  - No real-time understanding
```

**Impact**: Models can understand and interpret data in real-time.

#### 2. **Semantic Relationship Discovery**
```
SanTOK Interpretation:
  - Finds related concepts
  - Discovers relationships
  - Builds knowledge graph

Model uses for:
  - Understanding context
  - Relationship discovery
  - Knowledge expansion
```

**Impact**: Models can discover and understand relationships automatically.

#### 3. **Concept Exploration**
```
SanTOK Interpretation:
  - Explores concepts deeply
  - Multi-level exploration
  - Hierarchical understanding

Model uses for:
  - Deep understanding
  - Concept hierarchies
  - Knowledge navigation
```

**Impact**: Models can explore and understand concepts at multiple levels.

#### 4. **Knowledge Discovery**
```
SanTOK Interpretation:
  - Discovers new knowledge
  - Finds patterns
  - Builds understanding

Standard approach:
  - Static knowledge
  - No discovery
```

**Impact**: Models can discover new knowledge from data.

**Real Example**:
```python
# Standard approach: Static processing
data = "Machine learning uses neural networks"
result = process(data)  # Basic processing

# SanTOK Interpretation: Dynamic understanding
data = "Machine learning uses neural networks"
result = interpreter.interpret(data)
# Discovers:
#   - "machine learning" IS_A "AI technique"
#   - "neural networks" USES "machine learning"
#   - Related concepts: "deep learning", "training"
#   - Builds knowledge graph automatically
```

**Result**: Models can **discover and understand knowledge dynamically**.

---

### 🎯 Combined Impact: How All Components Work Together

**The Complete SanTOK Advantage**:

```
┌─────────────────────────────────────────────────────────────┐
│         How SanTOK Components Help Your Model                │
└─────────────────────────────────────────────────────────────┘

1. Tokenization
   └─ Provides: Deterministic foundation, mathematical properties
   └─ Helps Model: Stable learning, rich features

2. Embeddings
   └─ Provides: Domain-specific, fast embeddings
   └─ Helps Model: Better representations, no external deps

3. Semantics
   └─ Provides: Self-learned semantic understanding
   └─ Helps Model: Domain-aware, contextual understanding

4. Vectors
   └─ Provides: Fast similarity search, multiple backends
   └─ Helps Model: Efficient retrieval, scalable storage

5. Trees & Graphs
   └─ Provides: Structured knowledge, reasoning
   └─ Helps Model: Logical inference, explainability

6. Cognitive
   └─ Provides: Validation, constraint enforcement
   └─ Helps Model: Reliable outputs, no hallucination

7. SLM
   └─ Provides: Lightweight, constraint-grounded generation
   └─ Helps Model: Fast, reliable text generation

8. Memory
   └─ Provides: Unified, multi-modal knowledge storage
   └─ Helps Model: Integrated knowledge, source tracking

9. Interpretation
   └─ Provides: Real-time understanding, knowledge discovery
   └─ Helps Model: Dynamic learning, relationship discovery

COMBINED RESULT:
✅ Faster training (deterministic, rich features)
✅ Better accuracy (domain-specific, validated)
✅ More reliable (no hallucination, constraints)
✅ Fully explainable (reasoning traces, sources)
✅ Production-ready (scalable, efficient)
✅ Self-contained (no external dependencies)
```

---

## 🎓 Training & Testing Architecture - Clean Face

### Overview

SanTOK provides comprehensive training and testing systems for semantic models, language models, and performance evaluation.

### Training Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Training System Architecture                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Data Preparation                              │    │
│  │  - Corpus loading                                     │    │
│  │  - Text preprocessing                                 │    │
│  │  - Dataset splitting (train/val/test)                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Tokenization                                 │    │
│  │  - TextTokenizer.build()                             │    │
│  │  - Multiple streams                                 │    │
│  │  - TokenRecord creation                             │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Training Type Selection                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Semantic     │  │ Language     │                │    │
│  │  │ Embedding    │  │ Model        │                │    │
│  │  │ Training     │  │ Training     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Enhanced     │  │ Vocabulary   │                │    │
│  │  │ Semantic     │  │ Building     │                │    │
│  │  │ Training     │  │              │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Training Execution                           │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ For each epoch:                      │           │    │
│  │  │  1. Sample batch                     │           │    │
│  │  │  2. Forward pass                     │           │    │
│  │  │  3. Compute loss                      │           │    │
│  │  │  4. Backward pass                     │           │    │
│  │  │  5. Update parameters                │           │    │
│  │  │  6. Validation (if applicable)       │           │    │
│  │  └──────────────────────────────────────┘           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Model Evaluation                              │    │
│  │  - Loss curves                                        │    │
│  │  - Embedding quality metrics                          │    │
│  │  - Similarity evaluation                              │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Model Persistence                             │    │
│  │  - Save embeddings                                   │    │
│  │  - Save vocabulary                                   │    │
│  │  - Save metadata                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Testing Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Testing System Architecture                  │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Test Categories                               │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Unit Tests   │  │ Integration  │                │    │
│  │  │ - Functions  │  │ Tests        │                │    │
│  │  │ - Classes    │  │ - Pipelines  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Performance │  │ Accuracy     │                │    │
│  │  │ Tests        │  │ Tests        │                │    │
│  │  │ - Speed      │  │ - Correctness│                │    │
│  │  │ - Memory     │  │ - Quality    │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Test Execution                               │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ 1. Tokenization Tests                │           │    │
│  │  │    - All 9 methods                   │           │    │
│  │  │    - Determinism                     │           │    │
│  │  │    - Mathematical properties          │           │    │
│  │  └──────────────────────────────────────┘           │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ 2. Embedding Tests                   │           │    │
│  │  │    - All 4 strategies                │           │    │
│  │  │    - Dimension correctness           │           │    │
│  │  │    - Normalization                   │           │    │
│  │  └──────────────────────────────────────┘           │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ 3. Training Tests                    │           │    │
│  │  │    - Vocabulary building             │           │    │
│  │  │    - Training convergence           │           │    │
│  │  │    - Model saving/loading            │           │    │
│  │  └──────────────────────────────────────┘           │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ 4. Performance Benchmarks            │           │    │
│  │  │    - Speed measurements              │           │    │
│  │  │    - Memory usage                    │           │    │
│  │  │    - Scalability                     │           │    │
│  │  └──────────────────────────────────────┘           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Test Reporting                               │    │
│  │  - Pass/Fail status                                 │    │
│  │  - Performance metrics                              │    │
│  │  - Coverage reports                                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Training Workflow

```
1. Data Collection
    ↓
2. Preprocessing
    ↓
3. Tokenization
    ↓
4. Vocabulary Building
    ↓
5. Co-occurrence Matrix
    ↓
6. Model Initialization
    ↓
7. Training Loop
    ├─ Epoch 1 → Loss: 0.5
    ├─ Epoch 2 → Loss: 0.4
    ├─ Epoch 3 → Loss: 0.3
    └─ ...
    ↓
8. Validation
    ↓
9. Model Saving
    ↓
10. Evaluation
```

---

## 🌳 Trees, Graphs & Reasoning Architecture - Clean Face

### Overview

SanTOK Cognitive provides a complete knowledge representation and reasoning system using trees, graphs, and symbolic inference.

### Knowledge Trees Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Knowledge Trees Architecture                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Tree Structure                              │    │
│  │                                                       │    │
│  │              Root Node                               │    │
│  │              (depth=0)                               │    │
│  │                 │                                     │    │
│  │        ┌────────┼────────┐                           │    │
│  │        │        │        │                           │    │
│  │    Child 1   Child 2   Child 3                      │    │
│  │   (depth=1)  (depth=1)  (depth=1)                    │    │
│  │        │        │        │                           │    │
│  │    ┌───┴───┐    │    ┌───┴───┐                       │    │
│  │    │       │    │    │       │                       │    │
│  │  Leaf 1  Leaf 2│  Leaf 3  Leaf 4                    │    │
│  │                │                                     │    │
│  │            Leaf 5                                    │    │
│  │                                                       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  TreeNode Properties:                                        │
│    - node_id: Unique identifier                             │
│    - content: Text/label                                    │
│    - parent_id: Parent node reference                      │
│    - children_ids: List of child node IDs                  │
│    - depth: Hierarchical depth                             │
│    - metadata: Additional properties                       │
│    - embedding_ref: Link to vector store                   │
│    - graph_node_ref: Link to graph store                   │
│                                                               │
│  Operations:                                                 │
│    - add_node(): Add new node                              │
│    - remove_node(): Remove node (recursive)                │
│    - get_path(): Get path from root to node                │
│    - traverse_dfs(): Depth-first traversal                │
│    - traverse_bfs(): Breadth-first traversal              │
│    - get_subtree(): Extract subtree                       │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Knowledge Graph Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Knowledge Graph Architecture                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Graph Structure                              │    │
│  │                                                       │    │
│  │  Node A ──IS_A──→ Node B                             │    │
│  │    │                │                                 │    │
│  │    │                │                                 │    │
│  │ PART_OF         USES                                 │    │
│  │    │                │                                 │    │
│  │    ↓                ↓                                 │    │
│  │  Node C ──CAUSES──→ Node D                            │    │
│  │    │                │                                 │    │
│  │    │                │                                 │    │
│  │ LOCATED_IN      RELATED_TO                            │    │
│  │    │                │                                 │    │
│  │    └───────────────┘                                  │    │
│  │                                                       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  GraphNode Properties:                                       │
│    - id: Unique integer ID                                  │
│    - label: Human-readable label                           │
│    - properties: Dictionary of properties                  │
│    - edges: List of outgoing edges                         │
│                                                               │
│  GraphEdge Properties:                                       │
│    - source_id: Source node ID                             │
│    - target_id: Target node ID                             │
│    - relation: RelationType (15+ types)                    │
│    - confidence: Confidence score (0-1)                    │
│    - metadata: Additional properties                       │
│                                                               │
│  Relation Types (15+):                                       │
│    - IS_A, PART_OF, CAUSES, USES                           │
│    - LOCATED_IN, RELATED_TO, PRECEDES                      │
│    - OPPOSITE_OF, SIMILAR_TO, CONTAINS                     │
│    - ... (and more)                                        │
│                                                               │
│  Operations:                                                 │
│    - add_node(): Add new node                              │
│    - add_edge(): Add relation                              │
│    - get_neighbors(): Get connected nodes                  │
│    - find_path(): Find path between nodes                 │
│    - query(): Complex graph queries                        │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Reasoning Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Reasoning Architecture                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Query: "What is machine learning?"                         │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Query Parser                                 │    │
│  │  - Parse natural language                            │    │
│  │  - Extract key concepts                              │    │
│  │  - Build structured query                            │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Knowledge Retrieval                          │    │
│  │  - Search in GraphStore                              │    │
│  │  - Search in TreeStore                               │    │
│  │  - Search in UnifiedMemory                           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Inference Engine                              │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ Apply Inference Rules (20+)          │           │    │
│  │  │  - Transitivity: A→B, B→C → A→C     │           │    │
│  │  │  - Inheritance: IS_A relationships   │           │    │
│  │  │  - Symmetry: A↔B                     │           │    │
│  │  │  - Inverse: A→B → B←A                │           │    │
│  │  │  - ... (16+ more rules)              │           │    │
│  │  └──────────────┬──────────────────────┘           │    │
│  │                 ↓                                   │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ Rule Chaining                        │           │    │
│  │  │  - Chain multiple rules              │           │    │
│  │  │  - Propagate confidence              │           │    │
│  │  │  - Track reasoning path              │           │    │
│  │  └──────────────┬──────────────────────┘           │    │
│  │                 ↓                                   │    │
│  │  ┌─────────────────────────────────────┐           │    │
│  │  │ Generate Inferred Facts              │           │    │
│  │  │  - New relationships                 │           │    │
│  │  │  - Confidence scores                 │           │    │
│  │  │  - Reasoning traces                  │           │    │
│  │  └──────────────────────────────────────┘           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Path Finding                                 │    │
│  │  - Find reasoning paths                              │    │
│  │  - Calculate path confidence                         │    │
│  │  - Rank paths by relevance                           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Contradiction Detection                      │    │
│  │  - Check for conflicting facts                       │    │
│  │  - Flag contradictions                               │    │
│  │  - Resolve conflicts (if possible)                   │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Explanation Generation                        │    │
│  │  - Build reasoning trace                             │    │
│  │  - Format explanation                                │    │
│  │  - Include confidence scores                         │    │
│  │  - Link to source facts                              │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  Answer with Full Reasoning Trace                          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Unified Memory Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         Unified Memory Architecture                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         MemoryObject                                 │    │
│  │  - content: Text/fact                                │    │
│  │  - type: "fact", "concept", "rule", etc.            │    │
│  │  - metadata: Additional properties                  │    │
│  │  - graph_node_ref: Link to graph                    │    │
│  │  - tree_node_ref: Link to tree                       │    │
│  │  - embedding_ref: Link to vector store               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Auto-Linking                                 │    │
│  │  When auto_link_graph=True:                         │    │
│  │    - Extract entities from content                   │    │
│  │    - Create graph nodes                              │    │
│  │    - Create relations (IS_A, PART_OF, etc.)         │    │
│  │    - Link memory object to graph                     │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Storage Integration                           │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ GraphStore   │  │ TreeStore    │                │    │
│  │  │ (Relations)  │  │ (Hierarchy)  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐                                   │    │
│  │  │ VectorStore  │                                   │    │
│  │  │ (Embeddings) │                                   │    │
│  │  └──────────────┘                                   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Reasoning Flow Example

```
Query: "What is Python?"
    ↓
[Query Parser]
    Extract: "Python" (entity)
    Query type: DEFINITION
    ↓
[Knowledge Retrieval]
    Find in GraphStore:
        Node: "Python" (id=1)
        Edge: Python --IS_A--> Programming Language
    Find in Memory:
        MemoryObject: "Python is a programming language"
    ↓
[Inference Engine]
    Apply rules:
        - IS_A transitivity
        - Inheritance
    Generate inferred facts:
        Python IS_A Programming Language
        Programming Language IS_A Software Tool
        → Python IS_A Software Tool (inferred)
    ↓
[Path Finding]
    Find paths:
        Path 1: Python → Programming Language (confidence: 1.0)
        Path 2: Python → Programming Language → Software Tool (confidence: 0.9)
    ↓
[Explanation Generation]
    Build trace:
        Facts used: 2
        Rules applied: transitive_is_a
        Path: Python → Programming Language
        Confidence: 95%
    ↓
Answer: "Python is a type of programming language."
Explanation: [Full reasoning trace]
```

---

## 🌐 API Server Architecture - Clean Face

### Overview

SanTOK provides production-ready API servers built on FastAPI, supporting REST endpoints, WebSocket connections, file uploads, and async job processing.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK API Server Architecture                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Client Layer                             │    │
│  │  - HTTP Clients (REST)                               │    │
│  │  - WebSocket Clients                                 │    │
│  │  - File Upload Clients                               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              FastAPI Application                      │    │
│  │  - FastAPI app instance                              │    │
│  │  - Route registration                                │    │
│  │  - Middleware stack                                  │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Middleware Layer                         │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ CORS         │→ │ Authentication│                │    │
│  │  │ Handler      │  │ (JWT)         │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Request      │→ │ Error        │                │    │
│  │  │ Validation   │  │ Handling     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Route Handlers                           │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ /api/v1/     │  │ /api/v1/     │                │    │
│  │  │ tokenize     │  │ embed        │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ /api/v1/     │  │ /api/v1/     │                │    │
│  │  │ train        │  │ search       │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ /api/v1/     │  │ /ws          │                │    │
│  │  │ upload       │  │ (WebSocket)  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Business Logic Layer                      │    │
│  │  - TextTokenizer                                      │    │
│  │  - EmbeddingGenerator                                 │    │
│  │  - VectorStore                                        │    │
│  │  - JobManager (async)                                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Response Layer                           │    │
│  │  - JSON responses                                    │    │
│  │  - Streaming responses                               │    │
│  │  - WebSocket messages                                │    │
│  │  - File downloads                                    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Request Flow

```
HTTP Request
    ↓
[FastAPI Router]
    Parse route → Select handler
    ↓
[CORS Middleware]
    Add CORS headers
    ↓
[Authentication Middleware]
    Validate JWT token (if required)
    ↓
[Request Validation]
    Validate request body (Pydantic)
    ↓
[Route Handler]
    Execute business logic:
        - Tokenize text
        - Generate embeddings
        - Search vectors
        - etc.
    ↓
[Response Serialization]
    Convert to JSON
    ↓
[Response Middleware]
    Add headers, status codes
    ↓
HTTP Response
```

### WebSocket Flow

```
WebSocket Connection
    ↓
[Connection Handler]
    Accept connection
    ↓
[Message Loop]
    While connected:
        Receive message
            ↓
        [Message Router]
            Route to handler:
                - tokenize
                - train
                - stream
            ↓
        [Processing]
            Execute operation
            ↓
        [Streaming Response]
            Send progress updates
            ↓
        Send final result
    ↓
[Connection Close]
    Cleanup resources
```

### Job Management Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         Async Job Management                                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  POST /api/v1/jobs                                           │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Job Creation                                  │    │
│  │  - Generate job_id                                   │    │
│  │  - Create job record                                 │    │
│  │  - Status: PENDING                                   │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Background Task                              │    │
│  │  - Execute in thread pool                            │    │
│  │  - Update status: RUNNING                            │    │
│  │  - Process request                                   │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Status Updates                                │    │
│  │  - Update progress                                   │    │
│  │  - Store intermediate results                        │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Job Completion                                │    │
│  │  - Status: COMPLETED or FAILED                       │    │
│  │  - Store final results                               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  GET /api/v1/jobs/{job_id}                                 │
│      ↓                                                       │
│  Return job status and results                              │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### API Endpoint Categories

**Core Endpoints:**
- `POST /api/v1/tokenize` - Tokenize text
- `POST /api/v1/embed` - Generate embeddings
- `POST /api/v1/analyze` - Comprehensive analysis

**Training Endpoints:**
- `POST /api/v1/train` - Train semantic model
- `GET /api/v1/training/jobs` - List training jobs
- `GET /api/v1/training/jobs/{id}` - Get job status

**File Operations:**
- `POST /api/v1/upload` - Upload file
- `POST /api/v1/tokenize/file` - Tokenize file
- `GET /api/v1/download/{id}` - Download results

**Search & Retrieval:**
- `POST /api/v1/search` - Vector search
- `GET /api/v1/health` - Health check
- `GET /api/v1/info` - System information

**WebSocket:**
- `WS /ws` - Real-time tokenization
- `WS /ws/train` - Training progress
- `WS /ws/execute` - Code execution

---

## 💾 Vector Store Architecture - Clean Face

### Overview

SanTOK provides a unified interface to multiple vector database backends, allowing seamless switching between ChromaDB, FAISS, and Weaviate.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Vector Store Architecture                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Unified Interface                        │    │
│  │  SanTOKVectorStore (Abstract Base Class)             │    │
│  │  - add_tokens()                                      │    │
│  │  - search()                                          │    │
│  │  - get_token_embedding()                             │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Backend Selection                        │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ ChromaDB     │  │ FAISS        │                │    │
│  │  │ VectorStore  │  │ VectorStore   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Weaviate     │  │ In-Memory    │                │    │
│  │  │ VectorStore  │  │ VectorStore  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Backend-Specific Implementation          │    │
│  │  Each backend implements:                             │    │
│  │  - Storage mechanism                                  │    │
│  │  - Index structure                                    │    │
│  │  - Search algorithm                                   │    │
│  │  - Metadata handling                                  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### ChromaDB Backend

```
ChromaVectorStore
    ↓
[Initialization]
    Create PersistentClient
    Get or create collection
    ↓
[Add Tokens]
    Convert embeddings to list
    Extract metadata from TokenRecords
    Add to collection with IDs
    ↓
[Search]
    Query collection with embedding
    Use similarity search
    Return top_k results with metadata
    ↓
[Retrieve]
    Get by ID from collection
    Return embedding vector
```

### FAISS Backend

```
FAISSVectorStore
    ↓
[Initialization]
    Create IndexFlatL2 (L2 distance)
    Initialize token mapping
    ↓
[Add Tokens]
    Add embeddings to FAISS index
    Store TokenRecord mapping
    ↓
[Search]
    Query FAISS index
    Get top_k indices
    Map indices to TokenRecords
    Return results with distances
    ↓
[Retrieve]
    Get embedding from index
    Return vector
```

### Weaviate Backend

```
WeaviateVectorStore
    ↓
[Initialization]
    Connect to Weaviate cluster
    Create or get class (collection)
    Define schema
    ↓
[Add Tokens]
    Create objects with:
        - Vector (embedding)
        - Properties (metadata)
    Batch insert
    ↓
[Search]
    Use GraphQL query
    Vector similarity search
    Filter by metadata (optional)
    Return results
    ↓
[Retrieve]
    Get object by ID
    Extract vector and metadata
    Return embedding
```

### Vector Store Comparison

| Feature | ChromaDB | FAISS | Weaviate |
|---------|----------|-------|----------|
| **Speed** | Fast | Very Fast | Fast |
| **Memory** | Medium | Low | Medium |
| **Persistence** | Built-in | Manual | Cloud |
| **Metadata** | Good | Limited | Excellent |
| **Scalability** | Medium | High | Very High |
| **Use Case** | Development | Production | Enterprise |

---

## 🤖 Small Language Models (SLM) Architecture - Clean Face

### Overview

SanTOK includes a complete Small Language Model implementation that uses only SanTOK components - no external AI frameworks.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK SLM Architecture                             │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Input Layer                             │    │
│  │  - Text prompt                                      │    │
│  │  - Context (optional)                               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Tokenization                            │    │
│  │  - SanTOK TextTokenizer                             │    │
│  │  - Convert text to TokenRecords                     │    │
│  │  - Extract UIDs                                      │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Embedding Layer                         │    │
│  │  - SanTOK EmbeddingGenerator                        │    │
│  │  - Convert tokens to embeddings                     │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Model Architecture                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Transformer  │→ │ Attention    │                │    │
│  │  │ Encoder      │  │ Mechanism    │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Positional   │→ │ Feed-Forward │                │    │
│  │  │ Encoding     │  │ Network      │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Constraint Engine                        │    │
│  │  - Knowledge graph constraints                       │    │
│  │  - Fact validation                                  │    │
│  │  - No hallucination guarantee                        │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Decoder                                  │    │
│  │  - Constrained decoding                              │    │
│  │  - Token generation                                  │    │
│  │  - Sequence optimization                             │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Output                                  │    │
│  │  - Generated text                                   │    │
│  │  - Confidence scores                                │    │
│  │  - Reasoning trace                                  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Training Flow

```
Training Facts
    ↓
[Knowledge Integration]
    Add facts to UnifiedMemory
    Build knowledge graph
    ↓
[Tokenization]
    Tokenize all facts
    Build vocabulary
    ↓
[Embedding Training]
    Train semantic embeddings
    Learn token relationships
    ↓
[Model Training]
    Train transformer layers
    Learn sequence patterns
    ↓
[Constraint Learning]
    Learn graph constraints
    Build constraint rules
    ↓
Trained Model
```

### Generation Flow

```
Input Prompt
    ↓
[Tokenization]
    Tokenize prompt
    ↓
[Embedding]
    Convert to embeddings
    ↓
[Encoding]
    Pass through encoder
    Generate context
    ↓
[Constraint Checking]
    Query knowledge graph
    Get valid tokens
    ↓
[Decoding]
    Generate tokens one by one
    Apply constraints
    Optimize sequence
    ↓
[Output]
    Generated text
    Confidence scores
```

### Constraint-Grounded (CG-SLM) Features

- **No Hallucination**: Only generates facts from knowledge graph
- **Fact Validation**: Every token checked against constraints
- **Reasoning Trace**: Full explanation of generation
- **Confidence Scores**: Reliability for each token

---

## 💻 CLI Architecture - Clean Face

### Overview

SanTOK provides comprehensive command-line interfaces for all operations, from tokenization to training to system management.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK CLI Architecture                            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Command: python santok_cli.py <command> [options]          │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Argument Parser                          │    │
│  │  - Parse command-line arguments                      │    │
│  │  - Validate inputs                                   │    │
│  │  - Set defaults                                      │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Command Router                           │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ tokenize     │  │ train        │                │    │
│  │  │ - Text       │  │ - Model      │                │    │
│  │  │ - File       │  │ - Corpus     │                │    │
│  │  │ - URL        │  │ - Enhanced   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ embed        │  │ test         │                │    │
│  │  │ - Generate   │  │ - Quick      │                │    │
│  │  │ - Strategy   │  │ - Full       │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐                                   │    │
│  │  │ info         │                                   │    │
│  │  │ - System     │                                   │    │
│  │  │ - Features   │                                   │    │
│  │  └──────────────┘                                   │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Execution Layer                          │    │
│  │  - Initialize components                             │    │
│  │  - Execute operation                                 │    │
│  │  - Handle errors                                     │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Output Formatting                        │    │
│  │  - JSON output                                       │    │
│  │  - Pretty print                                      │    │
│  │  - File output                                       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### CLI Command Structure

```
santok_cli.py
    ├─ tokenize
    │   ├─ --text <text>
    │   ├─ --file <path>
    │   ├─ --url <url>
    │   ├─ --method <method>
    │   ├─ --output <path>
    │   └─ --format <json|txt>
    │
    ├─ train
    │   ├─ --file <corpus>
    │   ├─ --model-path <path>
    │   ├─ --embedding-dim <dim>
    │   ├─ --epochs <n>
    │   └─ --enhanced
    │
    ├─ embed
    │   ├─ --text <text>
    │   ├─ --model-path <path>
    │   ├─ --strategy <strategy>
    │   └─ --output <path>
    │
    ├─ test
    │   └─ --quick
    │
    └─ info
```

---

## 🔗 Integration Architecture - Clean Face

### Overview

SanTOK provides integration modules to connect with external systems, adapt vocabularies, and bridge between different components.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Integration Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Integration Modules                      │    │
│  │                                                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Vocabulary   │  │ Source Map   │                │    │
│  │  │ Adapter      │  │ Integration │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Convert    │  │ - Track      │                │    │
│  │  │   between    │  │   sources    │                │    │
│  │  │   systems    │  │ - Map tokens │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Cognitive    │  │ Vector       │                │    │
│  │  │ Pipeline     │  │ Bridge       │                │    │
│  │  │              │  │              │                │    │
│  │  │ - End-to-end │  │ - Connect    │                │    │
│  │  │   processing │  │   to stores  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Token        │  │ Embedding    │                │    │
│  │  │ Bridge       │  │ Bridge       │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Link       │  │ - Convert    │                │    │
│  │  │   systems    │  │   formats    │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Integration Flow

```
External System
    ↓
[Integration Module]
    - Receive input
    - Convert format
    - Validate
    ↓
[SanTOK Processing]
    - Tokenize
    - Generate embeddings
    - Process
    ↓
[Output Conversion]
    - Convert to external format
    - Add metadata
    ↓
External System
```

---

## ⚡ Performance & Optimization Architecture - Clean Face

### Overview

SanTOK includes comprehensive performance optimization features including parallel processing, caching, and efficient algorithms.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Performance Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Performance Strategies                   │    │
│  │                                                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Parallel     │  │ Caching      │                │    │
│  │  │ Processing   │  │ System       │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Threading  │  │ - Result     │                │    │
│  │  │ - Multiproc  │  │   caching    │                │    │
│  │  │ - Auto-detect│  │ - Embedding  │                │    │
│  │  └──────────────┘  │   cache      │                │    │
│  │  ┌──────────────┐  └──────────────┘                │    │
│  │  │ Memory       │  ┌──────────────┐                │    │
│  │  │ Optimization │  │ Algorithm   │                │    │
│  │  │              │  │ Efficiency  │                │    │
│  │  │ - Streaming  │  │              │                │    │
│  │  │ - Chunking   │  │ - Sparse     │                │    │
│  │  │ - Lazy eval  │  │   matrices   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Parallel Processing Flow

```
Input Text (Large)
    ↓
[Size Detection]
    Check text length
    ↓
[Threshold Check]
    If > 50KB:
        → Use parallel processing
    Else:
        → Use sequential processing
    ↓
[Chunking]
    Split text into chunks (50KB each)
    ↓
[Parallel Execution]
    ┌─────────────┬─────────────┬─────────────┐
    │  Chunk 1    │  Chunk 2    │  Chunk 3    │
    │  (Thread 1) │  (Thread 2) │  (Thread 3) │
    └──────┬──────┴──────┬──────┴──────┬──────┘
           │            │            │
           └────────────┼────────────┘
                        ↓
            [Result Aggregation]
                Merge all results
                Maintain order
                ↓
            Final TokenStream
```

### Performance Optimization Strategies

**1. Automatic Parallel Processing:**
- Detects text size automatically
- Uses threading for I/O-bound tasks
- Uses multiprocessing for CPU-bound tasks
- Optimal worker count based on CPU cores

**2. Memory Optimization:**
- Streaming processing for large files
- Chunked processing to avoid memory overflow
- Lazy evaluation where possible
- Efficient data structures

**3. Caching:**
- Tokenization result caching
- Embedding caching
- Vocabulary caching
- Model caching

**4. Algorithm Efficiency:**
- Sparse matrices for large vocabularies
- Efficient hash-based lookups
- Optimized mathematical operations
- Vectorized operations (NumPy)

### Performance Benchmarks

```
Text Size    | Sequential | Threaded | Multiprocess | Speedup
-------------|------------|----------|--------------|--------
1 KB         | 0.001s     | 0.002s   | 0.005s       | 0.5x
10 KB        | 0.01s      | 0.008s   | 0.012s       | 1.25x
100 KB       | 0.1s       | 0.05s    | 0.04s        | 2.5x
1 MB         | 1.0s       | 0.3s     | 0.2s         | 5x
10 MB        | 10s        | 2s       | 1.5s         | 6.7x
```

---

## 🛡️ Error Handling & Validation Architecture - Clean Face

### Overview

SanTOK implements comprehensive error handling and validation to ensure robust operation and prevent failures.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Error Handling Architecture                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Input/Request                                                │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Input Validation Layer                  │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Type         │→ │ Value        │                │    │
│  │  │ Validation   │  │ Validation   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Range        │→ │ Format       │                │    │
│  │  │ Validation   │  │ Validation   │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Processing Layer                        │    │
│  │  - Try-catch blocks                                 │    │
│  │  - Graceful degradation                             │    │
│  │  - Fallback mechanisms                              │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Error Classification                    │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Validation   │  │ Processing   │                │    │
│  │  │ Errors       │  │ Errors       │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ System       │  │ External     │                │    │
│  │  │ Errors       │  │ Errors       │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Error Response                          │    │
│  │  - User-friendly messages                           │    │
│  │  - Detailed logs (server-side)                      │    │
│  │  - Error codes                                      │    │
│  │  - Recovery suggestions                             │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Validation Layers

**1. Input Validation:**
```python
validate_text_input(text)      # Type and format check
validate_port(port)             # Range validation
validate_file_path(path)        # Path validation
validate_tokenization_method()  # Method validation
```

**2. Processing Validation:**
- Token count limits
- Memory usage checks
- Timeout handling
- Resource availability

**3. Output Validation:**
- Result format validation
- Data integrity checks
- Consistency verification

### Error Handling Strategy

```
Error Occurs
    ↓
[Error Classification]
    - ValidationError
    - ProcessingError
    - SystemError
    - ExternalError
    ↓
[Error Context]
    - Capture stack trace
    - Log context
    - Identify recovery options
    ↓
[Error Response]
    Production:
        - Generic user message
        - Detailed server logs
    Development:
        - Detailed error message
        - Stack trace
        - Debug information
    ↓
[Recovery Attempt]
    - Fallback methods
    - Retry logic
    - Graceful degradation
```

### Security Considerations

- **Information Disclosure Prevention**: Detailed errors only in development
- **Input Sanitization**: All inputs validated and sanitized
- **Resource Limits**: Prevent DoS attacks
- **Authentication**: JWT-based security
- **CORS Configuration**: Configurable origins

---

## 🔄 Complete Data Flow Architecture - Clean Face

### Overview

This section shows the complete end-to-end data flow through the entire SanTOK system.

### End-to-End Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│         Complete SanTOK Data Flow                            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [1] Input Sources                                   │    │
│  │  - Text string                                       │    │
│  │  - File upload                                       │    │
│  │  - URL fetch                                         │    │
│  │  - API request                                       │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [2] Preprocessing                                    │    │
│  │  - Text normalization                                │    │
│  │  - Language detection                                │    │
│  │  - Encoding detection                                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [3] Tokenization (9 methods in parallel)            │    │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐              │    │
│  │  │Space │ │Word  │ │Char  │ │Gram  │              │    │
│  │  └──────┘ └──────┘ └──────┘ └──────┘              │    │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐              │    │
│  │  │Subw  │ │BPE   │ │Syll  │ │Freq  │              │    │
│  │  └──────┘ └──────┘ └──────┘ └──────┘              │    │
│  │  ┌──────┐                                          │    │
│  │  │Byte  │                                          │    │
│  │  └──────┘                                          │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [4] Mathematical Enrichment                         │    │
│  │  - UID assignment                                    │    │
│  │  - Frontend digits                                   │    │
│  │  - Backend numbers                                   │    │
│  │  - Global IDs                                        │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [5] Branch Point                                    │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Embedding    │  │ Cognitive    │                │    │
│  │  │ Path         │  │ Reasoning    │                │    │
│  │  │              │  │ Path         │                │    │
│  │  └──────┬───────┘  └──────┬───────┘                │    │
│  │         │                 │                         │    │
│  │         ↓                 ↓                         │    │
│  │  [5a] Embedding    [5b] Knowledge                  │    │
│  │  Generation        Graph Building                  │    │
│  │         │                 │                         │    │
│  │         ↓                 ↓                         │    │
│  │  [5c] Vector Store  [5d] Reasoning                 │    │
│  │         │                 │                         │    │
│  │         └────────┬────────┘                         │    │
│  │                  ↓                                  │    │
│  │         [6] Integration                            │    │
│  └─────────────────────────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [7] Output Generation                                │    │
│  │  - Formatted results                                  │    │
│  │  - Metadata                                           │    │
│  │  - Explanations                                       │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [8] Response Delivery                                │    │
│  │  - JSON response                                      │    │
│  │  - File download                                      │    │
│  │  - WebSocket stream                                   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Detailed Processing Pipeline

```
1. INPUT
   Text: "Hello World"
   Source: API/File/URL
   ↓
2. PREPROCESSING
   normalize_case() → "hello world"
   normalize_whitespace() → "hello world"
   detect_language() → "en"
   ↓
3. TOKENIZATION (Parallel)
   Space: ["hello", "world"]
   Word: ["hello", "world"]
   Char: ["h", "e", "l", ...]
   Grammar: ["hello", ",", "world"]
   Subword: ["hel", "lo", "wor", "ld"]
   ... (9 methods)
   ↓
4. MATHEMATICAL ANALYSIS
   For each token:
     - Generate UID (Xorshift64*)
     - Calculate frontend digit (9-centric)
     - Compose backend number
     - Assign global ID
     - Link neighbors
   ↓
5. EMBEDDING GENERATION
   Strategy: feature_based/semantic/hash/hybrid
   Extract features → Generate vector (768-dim)
   ↓
6. STORAGE/REASONING
   Option A: Vector Store
     - Add to ChromaDB/FAISS/Weaviate
     - Index for search
   Option B: Cognitive Reasoning
     - Add to knowledge graph
     - Build relations
     - Enable reasoning
   ↓
7. OUTPUT FORMATTING
   {
     "tokens": [...],
     "embeddings": [...],
     "metadata": {...},
     "reasoning": {...}
   }
   ↓
8. RESPONSE
   JSON/File/Stream
```

---

## 🚀 Deployment Architecture - Clean Face

### Overview

SanTOK supports multiple deployment scenarios from local development to cloud production.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Deployment Architecture                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Deployment Options                       │    │
│  │                                                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Local        │  │ Cloud        │                │    │
│  │  │ Development  │  │ Production   │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Python     │  │ - Railway    │                │    │
│  │  │   script     │  │ - Heroku     │                │    │
│  │  │ - CLI        │  │ - AWS        │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Docker       │  │ Kubernetes   │                │    │
│  │  │ Container    │  │ Cluster      │                │    │
│  │  │              │  │              │                │    │
│  │  │ - docker-compose│ - Auto-scaling│                │    │
│  │  │ - Dockerfile │  │ - Load bal.  │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Deployment Scenarios

**1. Local Development:**
```
python run.py
    ↓
[Development Server]
    - Hot reload
    - Debug mode
    - Local storage
    - Port: 8000
```

**2. Production (Railway/Heroku):**
```
Procfile: web: python start.py
    ↓
[Platform Detection]
    - Auto-detect Python
    - Set PORT from env
    - Configure logging
    ↓
[Production Server]
    - Optimized settings
    - Error handling
    - Logging
    - Health checks
```

**3. Docker Deployment:**
```
docker-compose up
    ↓
[Docker Container]
    - Isolated environment
    - Volume mounts
    - Network config
    - Environment variables
```

**4. Kubernetes:**
```
kubectl apply -f k8s/
    ↓
[K8s Cluster]
    - Pods
    - Services
    - Ingress
    - Auto-scaling
```

### Environment Configuration

```
Development:
    - DEBUG=True
    - LOG_LEVEL=DEBUG
    - CORS_ORIGINS=*
    - PORT=8000

Production:
    - DEBUG=False
    - LOG_LEVEL=INFO
    - CORS_ORIGINS=https://yourdomain.com
    - PORT=${PORT}
    - WEAVIATE_URL=${WEAVIATE_URL}
    - WEAVIATE_API_KEY=${WEAVIATE_API_KEY}
```

---

## 🔐 Security Architecture - Clean Face

### Overview

SanTOK implements multiple security layers to protect the system and user data.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Security Architecture                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Security Layers                         │    │
│  │                                                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Input        │→ │ Authentication│                │    │
│  │  │ Validation   │  │ (JWT)        │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Sanitization │→ │ Authorization│                │    │
│  │  │              │  │ (Roles)      │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Rate         │→ │ Error        │                │    │
│  │  │ Limiting     │  │ Masking      │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Security Features

**1. Authentication:**
- JWT-based token authentication
- Token expiration
- Secure token storage
- Refresh tokens

**2. Input Validation:**
- Type checking
- Range validation
- Format validation
- Sanitization

**3. Resource Protection:**
- Rate limiting
- File size limits
- Memory limits
- Timeout protection

**4. Error Security:**
- No information disclosure in production
- Detailed errors only in development
- Secure logging
- Error masking

**5. CORS Configuration:**
- Configurable origins
- Production restrictions
- Development flexibility

---

## 📊 Monitoring & Logging Architecture - Clean Face

### Overview

SanTOK includes comprehensive monitoring and logging for observability and debugging.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Monitoring Architecture                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Logging System                          │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Application  │  │ Error        │                │    │
│  │  │ Logs         │  │ Logs         │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Performance  │  │ Access       │                │    │
│  │  │ Logs         │  │ Logs         │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Metrics Collection                       │    │
│  │  - Request count                                     │    │
│  │  - Response times                                    │    │
│  │  - Error rates                                       │    │
│  │  - Resource usage                                    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Logging Levels

- **DEBUG**: Detailed debugging information
- **INFO**: General informational messages
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical errors

### Health Check Endpoints

- `GET /api/v1/health` - Basic health check
- `GET /api/v1/info` - System information
- `GET /api/v1/metrics` - Performance metrics

---

## 🗜️ Compression Architecture - Clean Face

### Overview

SanTOK includes text compression algorithms based on mathematical properties and 9-centric numerology.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Compression Architecture                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Input Text                                                   │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Compression Strategies                        │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Numerology   │  │ Weighted     │                │    │
│  │  │ Based        │  │ Sum Based    │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Digital Root │  │ Backend      │                │    │
│  │  │ Folding      │  │ Number       │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Compression Process                           │    │
│  │  1. Calculate numerology values                       │    │
│  │  2. Compute weighted character sums                   │    │
│  │  3. Apply digital root folding                        │    │
│  │  4. Generate compressed representation               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  Compressed Output                                           │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Compression Algorithms

**1. Numerology-Based Compression:**
```
Text: "Hello"
    ↓
[Character Numerology]
    H → 8 (position in alphabet % 9 + 1)
    e → 5
    l → 3
    l → 3
    o → 6
    ↓
[Sum Calculation]
    Total: 8 + 5 + 3 + 3 + 6 = 25
    ↓
[Digital Root]
    dr(25) = 1 + ((25-1) mod 9) = 7
    ↓
Compressed: 7
```

**2. Weighted Sum Compression:**
```
Text: "Hello"
    ↓
[Weighted Sum]
    H: ord('H') × 1 = 72 × 1 = 72
    e: ord('e') × 2 = 101 × 2 = 202
    l: ord('l') × 3 = 108 × 3 = 324
    l: ord('l') × 4 = 108 × 4 = 432
    o: ord('o') × 5 = 111 × 5 = 555
    ↓
Total: 72 + 202 + 324 + 432 + 555 = 1585
    ↓
[Digital Root]
    dr(1585) = 1 + ((1585-1) mod 9) = 1
    ↓
Compressed: 1
```

---

## 🗺️ Source Map Integration Architecture - Clean Face

### Overview

SanTOK's source map integration tracks the provenance of tokens and embeddings, enabling source-aware processing and multi-source merging.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Source Map Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Source Map Structure                          │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Source       │  │ Algorithm    │                │    │
│  │  │ Metadata     │  │ Mapping      │                │    │
│  │  │              │  │              │                │    │
│  │  │ - source_id  │  │ - algorithm  │                │    │
│  │  │ - source_tag │  │   → tokens   │                │    │
│  │  │ - timestamp  │  │ - tokens →   │                │    │
│  │  │ - metadata   │  │   source     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Source-Aware Tokenization                     │    │
│  │  - Tag tokens with source                            │    │
│  │  - Track algorithm used                              │    │
│  │  - Maintain provenance                               │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Source-Aware Embedding Generation             │    │
│  │  - Embeddings linked to source                       │    │
│  │  - Source metadata in embeddings                     │    │
│  │  - Multi-source merging                              │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Source Map Flow

```
Input Text + Source Tag
    ↓
[Source Map Lookup]
    Get source metadata:
        - source_id
        - source_tag (e.g., "wikipedia", "arxiv")
        - algorithm_id
    ↓
[Tokenization with Source]
    Tokenize text
    Tag each token with:
        - source_id
        - source_tag
        - algorithm_id
    ↓
[Embedding Generation with Source]
    Generate embeddings
    Link embeddings to source
    Add source metadata
    ↓
[Source-Aware Storage]
    Store with source tags
    Enable source-based queries
    ↓
[Multi-Source Merging]
    Merge embeddings from multiple sources
    Combine metadata
    Weighted combination
```

---

## 🧩 Data Interpretation Architecture - Clean Face

### Overview

SanTOK's data interpretation system uses embeddings and vector stores to provide real-time insights and interpretations of data.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Data Interpretation Architecture            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Input Text: "Sales dropped 20% last month"                   │
│      ↓                                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Token Extraction                              │    │
│  │  - Tokenize input                                     │    │
│  │  - Extract key tokens                                │    │
│  │  - Identify important terms                          │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Embedding Generation                          │    │
│  │  - Generate embeddings for tokens                    │    │
│  │  - Create query embedding                           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Vector Search                                 │    │
│  │  - Search in Weaviate/ChromaDB/FAISS                │    │
│  │  - Find related concepts                            │    │
│  │  - Retrieve top-k results                           │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Interpretation Generation                     │    │
│  │  - Analyze relationships                             │    │
│  │  - Generate insights                                │    │
│  │  - Provide recommendations                          │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  Output: "Analyze customer behavior and marketing changes"   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Interpretation Flow

```
Input: "Sales dropped 20% last month"
    ↓
[Token Extraction]
    Key tokens: ["Sales", "dropped", "20%", "last", "month"]
    ↓
[Embedding Generation]
    Generate embeddings for each token
    Create combined query embedding
    ↓
[Vector Search]
    Search in knowledge base:
        - Find "Sales" related concepts
        - Find "dropped" related concepts
        - Find "20%" related concepts
    ↓
[Concept Retrieval]
    Related concepts:
        - "customer behavior"
        - "marketing changes"
        - "trend analysis"
        - "improvement strategies"
    ↓
[Interpretation Generation]
    Combine concepts:
        "Analyze customer behavior and 
         marketing changes to find the cause."
    ↓
Output with confidence scores
```

---

## 🎯 Custom Algorithms Architecture - Clean Face

### Overview

SanTOK includes several custom algorithms for ranking, scoring, similarity, and graph operations.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Custom Algorithms Architecture              │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Algorithm Categories                          │    │
│  │                                                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Ranking      │  │ Scoring      │                │    │
│  │  │ Algorithms   │  │ Algorithms   │                │    │
│  │  │              │  │              │                │    │
│  │  │ - SanTOK     │  │ - 9-Scorer   │                │    │
│  │  │   Ranker     │  │ - Confidence │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Similarity   │  │ Graph        │                │    │
│  │  │ Algorithms   │  │ Algorithms   │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Semantic   │  │ - Graph      │                │    │
│  │  │   Similarity │  │   Walker     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Pattern      │  │ Query        │                │    │
│  │  │ Matching     │  │ Parsing      │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Pattern    │  │ - NL → Query │                │    │
│  │  │   Matcher    │  │   Parser     │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### SanTOK Ranker Architecture

```
Query + Candidates
    ↓
[Component Score Calculation]
    ┌──────────────┬──────────────┬──────────────┬──────────────┐
    │ Relevance    │ Connectivity │ Hierarchy    │ Freshness    │
    │              │              │              │              │
    │ - Token      │ - Graph      │ - Tree       │ - Temporal   │
    │   overlap    │   centrality │   depth      │   decay      │
    │ - Position   │ - Relation   │ - Sibling    │ - Access     │
    │   boost      │   strength   │   penalty    │   frequency  │
    │ - Digital    │ - Path       │ - Parent     │ - Mod time   │
    │   root       │   distance   │   inheritance│              │
    └──────────────┴──────────────┴──────────────┴──────────────┘
    ↓
[Weighted Combination]
    score = α·Relevance + β·Connectivity + γ·Hierarchy + δ·Freshness
    (default: α=0.4, β=0.3, γ=0.2, δ=0.1)
    ↓
[9-Centric Folding]
    Apply digital root transformation
    ↓
Ranked Results
```

### 9-Scorer Architecture

```
Input Value
    ↓
[9-Centric Calculation]
    Apply digital root: dr(n) = 1 + ((n-1) mod 9)
    ↓
[Score Normalization]
    Map to [0, 1] range
    ↓
[Confidence Score]
    Final score (0-1)
```

### Semantic Similarity Architecture

```
Token A + Token B
    ↓
[Feature Extraction]
    Extract features from both tokens
    ↓
[Similarity Calculation]
    - Character overlap
    - UID distance
    - Frontend digit similarity
    - Backend number proximity
    ↓
[Combined Similarity]
    Weighted combination of features
    ↓
Similarity Score (0-1)
```

### Graph Walker Architecture

```
Start Node
    ↓
[Energy-Based Traversal]
    - Calculate node energy
    - Follow high-energy paths
    - Avoid low-energy nodes
    ↓
[Path Exploration]
    - BFS/DFS traversal
    - Depth limits
    - Energy thresholds
    ↓
[Path Ranking]
    Rank paths by:
        - Total energy
        - Path length
        - Relation strength
    ↓
Top-K Paths
```

### Pattern Matcher Architecture

```
Input Text
    ↓
[Pattern Library]
    ┌──────────────┬──────────────┬──────────────┬──────────────┐
    │ Lexical      │ Structural   │ Copula       │ Possessive   │
    │ Patterns     │ Patterns     │ Patterns     │ Patterns     │
    │              │              │              │              │
    │ - IS_A       │ - Position   │ - "X is Y"   │ - "X's Y"    │
    │ - PART_OF    │ - Distance   │ - "X are Y"  │ - "Y of X"   │
    │ - HAS_PART   │ - Context    │              │              │
    │ - CAUSES     │              │              │              │
    │ - USES       │              │              │              │
    └──────────────┴──────────────┴──────────────┴──────────────┘
    ↓
[Pattern Matching]
    - Apply regex patterns
    - Extract subject/object
    - Identify relation type
    - Calculate confidence
    ↓
[9-Centric Scoring]
    Apply digital root to confidence
    ↓
[Relation Extraction]
    Output: (subject, relation, object, confidence)
```

**Pattern Types:**
- **Lexical Patterns**: Word-based regex patterns (e.g., "X is Y" → IS_A)
- **Structural Patterns**: Position-based extraction
- **Copula Patterns**: "X is Y", "X are Y" → IS_A relation
- **Possessive Patterns**: "X's Y", "Y of X" → PART_OF/HAS_PART
- **Causal Patterns**: "X causes Y", "because of X" → CAUSES
- **Temporal Patterns**: "X before Y", "after X" → TEMPORAL

**Example:**
```python
matcher = SanTOKPatternMatcher()
text = "Python is a programming language. It uses dynamic typing."
matches = matcher.extract(text)
# Output: [
#   (Python, IS_A, programming language, 0.9),
#   (Python, USES, dynamic typing, 0.8)
# ]
```

### Query Parser Architecture

```
Natural Language Query
    ↓
[Query Type Detection]
    ┌──────────────┬──────────────┬──────────────┬──────────────┐
    │ Definition   │ Relation     │ List         │ Boolean      │
    │ "What is X?" │ "How X→Y?"   │ "Parts of X" │ "Is X a Y?"  │
    └──────────────┴──────────────┴──────────────┴──────────────┘
    ┌──────────────┬──────────────┬──────────────┐
    │ Comparison   │ Process      │ Count        │
    │ "X vs Y?"    │ "How X works"│ "How many X?"│
    └──────────────┴──────────────┴──────────────┘
    ↓
[Entity Extraction]
    - Extract subject
    - Extract object (if relation query)
    - Extract modifiers (negation, quantifiers)
    ↓
[Query Structure]
    {
        "type": "definition|relation|list|...",
        "subject": "extracted entity",
        "object": "extracted entity (optional)",
        "negated": false,
        "quantifier": null,
        "confidence": 0.95
    }
    ↓
[Structured Query]
    Ready for execution against knowledge base
```

**Supported Query Types:**
- **Definition**: "What is X?", "Define X", "Tell me about X"
- **Relation**: "How is X related to Y?", "What's the relationship between X and Y?"
- **List**: "What are the parts of X?", "List all X", "What does X contain?"
- **Boolean**: "Is X a Y?", "Does X have Y?"
- **Comparison**: "What's the difference between X and Y?", "Compare X and Y"
- **Process**: "How does X work?", "Explain how X operates"
- **Count**: "How many X?", "Count the number of Y"
- **Cause**: "Why does X happen?", "What causes Y?"

**Example:**
```python
parser = SanTOKQueryParser()
query = parser.parse("What is machine learning?")
# Output:
#   type: DEFINITION
#   subject: "machine learning"
#   confidence: 0.95
```

### Semantic Similarity Architecture (Detailed)

```
Text A + Text B
    ↓
[Tokenization]
    Tokenize both texts
    ↓
[Multi-Component Analysis]
    ┌─────────────────────────────────────────────────────────┐
    │ Component 1: Lexical Similarity                        │
    │   - Jaccard coefficient (token overlap)                │
    │   - Dice coefficient                                    │
    │   - Common tokens identification                        │
    └─────────────────────────────────────────────────────────┘
    ┌─────────────────────────────────────────────────────────┐
    │ Component 2: N-gram Similarity                          │
    │   - Character n-gram extraction (default: trigrams)     │
    │   - N-gram overlap calculation                          │
    │   - Position-aware matching                             │
    └─────────────────────────────────────────────────────────┘
    ┌─────────────────────────────────────────────────────────┐
    │ Component 3: Position-Weighted Similarity              │
    │   - Token position matching                             │
    │   - Order preservation scoring                          │
    │   - Distance-based weighting                            │
    └─────────────────────────────────────────────────────────┘
    ┌─────────────────────────────────────────────────────────┐
    │ Component 4: Graph-Based Similarity (Optional)          │
    │   - Path distance in knowledge graph                    │
    │   - Relation strength                                   │
    │   - Common neighbors                                    │
    └─────────────────────────────────────────────────────────┘
    ↓
[Weighted Combination]
    score = α·Lexical + β·Ngram + γ·Position + δ·Graph
    (default: α=0.35, β=0.25, γ=0.20, δ=0.20)
    ↓
[9-Centric Harmonization]
    Apply digital root transformation
    Normalize to [0, 1] range
    ↓
SimilarityResult
    - Combined score (0-1)
    - Digital root (1-9)
    - Component breakdown
    - Common tokens/ngrams
```

**Similarity Formula:**
```
sim(a, b) = α·Jaccard(a, b) + β·Ngram(a, b) + γ·Position(a, b) + δ·Graph(a, b)

Where:
- Jaccard(a, b) = |A ∩ B| / |A ∪ B|
- Ngram(a, b) = |N-grams(a) ∩ N-grams(b)| / |N-grams(a) ∪ N-grams(b)|
- Position(a, b) = Weighted position alignment score
- Graph(a, b) = Path distance / max_path_distance (if graph available)
```

**Example:**
```python
similarity = SanTOKSimilarity(graph=knowledge_graph)
result = similarity.compute("machine learning", "deep learning")
# Output:
#   score: 0.67
#   digital_root: 4
#   lexical_score: 0.60
#   ngram_score: 0.75
#   position_score: 0.55
#   graph_score: 0.70
```

---

## ⚙️ Configuration & Utilities Architecture - Clean Face

### Overview

SanTOK includes comprehensive configuration management and utility systems for system-wide settings and operations.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Configuration Architecture                  │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Configuration Sources                        │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Environment  │  │ Config Files │                │    │
│  │  │ Variables     │  │ (.env, yaml) │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Default      │  │ Runtime      │                │    │
│  │  │ Values       │  │ Overrides    │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Configuration Manager                        │    │
│  │  - Load configurations                              │    │
│  │  - Merge sources                                    │    │
│  │  - Validate settings                                │    │
│  │  - Provide defaults                                 │    │
│  └──────────────────┬──────────────────────────────────┘    │
│                     ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Configuration Categories                     │    │
│  │  - Server settings (port, host, CORS)               │    │
│  │  - Tokenization settings (seed, methods)            │    │
│  │  - Embedding settings (dim, strategy)               │    │
│  │  - Vector store settings (backend, connection)       │    │
│  │  - Logging settings (level, format)                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Configuration Hierarchy

```
1. Runtime Overrides (highest priority)
    - Command-line arguments
    - Function parameters
    ↓
2. Environment Variables
    - PORT, LOG_LEVEL, etc.
    ↓
3. Config Files
    - .env file
    - config.yaml
    ↓
4. Default Values (lowest priority)
    - Built-in defaults
```

### Utility Systems

**1. Validation Utilities:**
- Input type validation
- Range validation
- Format validation
- Path validation

**2. Logging Utilities:**
- Structured logging
- Log levels
- File/console output
- Log rotation

**3. Unique Identifier Utilities:**
- UID generation (Xorshift64*)
- ID management
- Collision detection

**4. Formatting Utilities:**
- Output formatting
- Data serialization
- Pretty printing

---

## 🔄 Memory Management Architecture - Clean Face

### Overview

SanTOK implements efficient memory management for handling large datasets and long-running processes.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│         SanTOK Memory Management Architecture              │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Memory Strategies                             │    │
│  │                                                       │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Streaming    │  │ Chunking     │                │    │
│  │  │ Processing   │  │ Strategy     │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Process    │  │ - Split into │                │    │
│  │  │   in chunks  │  │   chunks     │                │    │
│  │  │ - Release    │  │ - Process    │                │    │
│  │  │   memory     │  │   separately │                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  │  ┌──────────────┐  ┌──────────────┐                │    │
│  │  │ Caching      │  │ Lazy         │                │    │
│  │  │ Strategy     │  │ Evaluation   │                │    │
│  │  │              │  │              │                │    │
│  │  │ - Result     │  │ - Compute    │                │    │
│  │  │   caching    │  │   on demand  │                │    │
│  │  │ - Embedding  │  │ - Defer      │                │    │
│  │  │   caching    │  │   computation│                │    │
│  │  └──────────────┘  └──────────────┘                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Memory Optimization Techniques

**1. Streaming Processing:**
- Process data in streams
- Release memory after each chunk
- Avoid loading entire dataset

**2. Chunking:**
- Split large texts into chunks
- Process chunks independently
- Aggregate results

**3. Caching:**
- Cache frequently used results
- LRU eviction policy
- Memory-bounded cache

**4. Lazy Evaluation:**
- Compute only when needed
- Defer expensive operations
- Generator-based processing

---

## 📐 Detailed Component Architectures

### 1. SanTOK Core Tokenization Architecture

**Core Tokenization Engine** - The foundation of all text processing.

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK Core Tokenization Engine                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Input Text                                                  │
│      ↓                                                       │
│  ┌─────────────────────────────────────┐                   │
│  │   Preprocessing Layer                │                   │
│  │  - Case normalization                 │                   │
│  │  - Punctuation handling              │                   │
│  │  - Whitespace normalization          │                   │
│  │  - Language detection                │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Tokenization Methods (9 types)    │                   │
│  │  ┌──────┐ ┌──────┐ ┌──────┐       │                   │
│  │  │Space │ │ Word │ │ Char │       │                   │
│  │  └──────┘ └──────┘ └──────┘       │                   │
│  │  ┌──────┐ ┌──────┐ ┌──────┐       │                   │
│  │  │Grammar│ │Subword│ │ Byte │       │                   │
│  │  └──────┘ └──────┘ └──────┘       │                   │
│  │  ┌──────┐ ┌──────┐ ┌──────┐       │                   │
│  │  │BPE   │ │Syllable│ │Freq  │       │                   │
│  │  └──────┘ └──────┘ └──────┘       │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Mathematical Analysis Layer        │                   │
│  │  - UID Generation (Xorshift64*)      │                   │
│  │  - Frontend Digit Calculation        │                   │
│  │  - Backend Number Composition       │                   │
│  │  - Global ID Assignment              │                   │
│  │  - Digital Root Computation          │                   │
│  │  - Neighbor UID Linking              │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Statistical Features              │                   │
│  │  - Length Factor                    │                   │
│  │  - Balance Index                    │                   │
│  │  - Entropy Index                    │                   │
│  │  - Mean & Variance                 │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  TokenStream Objects (with TokenRecord instances)          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Token Processing Pipeline:**

```
Text Input
    ↓
[Preprocessing]
    ├─ normalize_case()
    ├─ remove_punctuation()
    ├─ normalize_whitespace()
    └─ detect_language()
    ↓
[Tokenization] (Parallel execution for 9 methods)
    ├─ tokenize_space()      → Space tokens
    ├─ tokenize_word()       → Word tokens
    ├─ tokenize_char()       → Character tokens
    ├─ tokenize_grammar()    → Grammar tokens
    ├─ tokenize_subword()    → Subword tokens
    ├─ tokenize_subword_bpe() → BPE tokens
    ├─ tokenize_subword_syllable() → Syllable tokens
    ├─ tokenize_subword_frequency() → Frequency tokens
    └─ tokenize_bytes()      → Byte tokens
    ↓
[UID Assignment]
    ├─ assign_uids(seed)     → Xorshift64* based UIDs
    └─ neighbor_uids()        → Link prev/next UIDs
    ↓
[Mathematical Properties]
    ├─ frontend_digit         → 9-centric digit (1-9)
    ├─ backend_number         → Composite number
    ├─ global_id              → Unique global identifier
    └─ content_id             → Content-based ID
    ↓
[TokenStream Creation]
    └─ TokenStream with TokenRecord objects
```

**Key Classes:**
- `TextTokenizer` - Main orchestrator
- `TokenStream` - Container for tokenized results
- `TokenRecord` - Individual token with all properties

---

### 2. SanTOK Cognitive Architecture

**Cognitive Reasoning System** - Deterministic reasoning substrate.

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK Cognitive System                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Knowledge Storage Layer                 │    │
│  │                                                       │    │
│  │  ┌──────────────┐      ┌──────────────┐            │    │
│  │  │  GraphStore   │      │  TreeStore    │            │    │
│  │  │              │      │              │            │    │
│  │  │ - Nodes      │      │ - Root Nodes │            │    │
│  │  │ - Edges      │      │ - Children   │            │    │
│  │  │ - Relations  │      │ - Hierarchy  │            │    │
│  │  │ (15+ types)  │      │ - Taxonomies │            │    │
│  │  └──────┬───────┘      └──────┬───────┘            │    │
│  │         │                      │                     │    │
│  │         └──────────┬──────────┘                     │    │
│  │                    ↓                                 │    │
│  │         ┌──────────────────────┐                    │    │
│  │         │  UnifiedMemory       │                    │    │
│  │         │  - MemoryObjects     │                    │    │
│  │         │  - Graph linking     │                    │    │
│  │         │  - Auto-relations   │                    │    │
│  │         └──────────┬───────────┘                    │    │
│  └────────────────────┼─────────────────────────────────┘    │
│                       ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Reasoning Engine                          │    │
│  │                                                       │    │
│  │  ┌──────────────┐      ┌──────────────┐            │    │
│  │  │ Inference     │      │ Query Engine  │            │    │
│  │  │ Engine        │      │              │            │    │
│  │  │              │      │ - Parsing    │            │    │
│  │  │ - 20+ Rules  │      │ - Execution  │            │    │
│  │  │ - Chaining   │      │ - Results    │            │    │
│  │  │ - Validation │      └──────┬───────┘            │    │
│  │  └──────┬───────┘             │                     │    │
│  │         │                     │                     │    │
│  │         └──────────┬──────────┘                     │    │
│  │                    ↓                                 │    │
│  │         ┌──────────────────────┐                    │    │
│  │         │  PathFinder          │                    │    │
│  │         │  - Graph traversal  │                    │    │
│  │         │  - Path discovery    │                    │    │
│  │         └──────────┬───────────┘                    │    │
│  │                    ↓                                 │    │
│  │         ┌──────────────────────┐                    │    │
│  │         │  Contradiction       │                    │    │
│  │         │  Detector            │                    │    │
│  │         └──────────┬───────────┘                    │    │
│  └────────────────────┼─────────────────────────────────┘    │
│                       ↓                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Explanation Layer                       │    │
│  │  - Reasoning traces                                  │    │
│  │  - Confidence scores                                 │    │
│  │  - Source attribution                                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Knowledge Graph Structure:**

```
GraphNode
    ├─ id: str
    ├─ label: str
    ├─ properties: dict
    └─ edges: List[GraphEdge]

GraphEdge
    ├─ source: str (node id)
    ├─ target: str (node id)
    ├─ relation: RelationType (15+ types)
    │   ├─ IS_A
    │   ├─ PART_OF
    │   ├─ CAUSES
    │   ├─ USES
    │   ├─ LOCATED_IN
    │   └─ ... (10+ more)
    └─ confidence: float (0-1)
```

**Reasoning Flow:**

```
Query Input
    ↓
[Query Parser]
    └─ Parse natural language → Structured query
    ↓
[Query Engine]
    ├─ Find relevant nodes in graph
    ├─ Extract relations
    └─ Build query plan
    ↓
[Inference Engine]
    ├─ Apply inference rules (20+)
    │   ├─ Transitivity
    │   ├─ Inheritance
    │   ├─ Symmetry
    │   ├─ Inverse
    │   └─ ... (16+ more)
    ├─ Rule chaining
    └─ Confidence propagation
    ↓
[Path Finder]
    └─ Find reasoning paths
    ↓
[Contradiction Detector]
    └─ Validate consistency
    ↓
[Explainer]
    ├─ Generate reasoning trace
    ├─ Calculate confidence
    └─ Format explanation
    ↓
Answer with full trace
```

---

### 3. Embedding System Architecture

**Semantic Embedding Generation** - Multiple strategies for vector generation.

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK Embedding System                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  TokenRecord Input                                            │
│      ↓                                                       │
│  ┌─────────────────────────────────────┐                   │
│  │   Strategy Selection                │                   │
│  │  ┌──────────┐  ┌──────────┐       │                   │
│  │  │ Feature  │  │ Semantic │       │                   │
│  │  │ Based    │  │ (Trained)│       │                   │
│  │  └──────────┘  └──────────┘       │                   │
│  │  ┌──────────┐  ┌──────────┐       │                   │
│  │  │ Hash     │  │ Hybrid   │       │                   │
│  │  │ Based    │  │ (Combined)│       │                   │
│  │  └──────────┘  └──────────┘       │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Feature Extraction                │                   │
│  │  - UID (64-bit → 8 bytes)           │                   │
│  │  - Frontend digit (1-9)             │                   │
│  │  - Backend number                   │                   │
│  │  - Global ID                        │                   │
│  │  - Text length                      │                   │
│  │  - Character frequencies            │                   │
│  │  - Stream type (one-hot)            │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Embedding Generation              │                   │
│  │  [Feature-based]                    │                   │
│  │    └─ Direct feature → vector      │                   │
│  │  [Semantic]                         │                   │
│  │    └─ Trained model lookup          │                   │
│  │  [Hash-based]                       │                   │
│  │    └─ Hash → normalized vector     │                   │
│  │  [Hybrid]                           │                   │
│  │    ├─ Text embedding (optional)    │                   │
│  │    └─ Feature embedding            │                   │
│  │    └─ Weighted combination          │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Dimension Projection               │                   │
│  │  - Project to target dimension       │                   │
│  │  - Normalize vector                 │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  Embedding Vector (float32 array)                          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Embedding Strategies:**

```
Feature-Based Strategy:
    TokenRecord
        ↓
    Extract Features:
        - UID bytes (8 floats)
        - Frontend digit (1 float)
        - Backend number (1 float)
        - Global ID (1 float)
        - Text length (1 float)
        - Stream type (9 floats, one-hot)
        - Character stats (N floats)
        ↓
    Concatenate → Feature vector
        ↓
    Project to embedding_dim (768 default)
        ↓
    Normalize
        ↓
    Embedding

Semantic Strategy:
    TokenRecord
        ↓
    Lookup UID in trained model
        ↓
    Retrieve learned embedding
        ↓
    Embedding

Hash-Based Strategy:
    TokenRecord
        ↓
    Hash text + UID
        ↓
    Convert to vector
        ↓
    Normalize
        ↓
    Embedding

Hybrid Strategy:
    TokenRecord
        ↓
    ┌─────────────┬─────────────┐
    │ Text Embed  │ Feature Emb │
    │ (optional)  │ (always)    │
    └──────┬──────┴──────┬──────┘
           │            │
           └─────┬──────┘
                 ↓
         Weighted Combination
                 ↓
         Embedding
```

---

### 4. Training System Architecture

**Semantic Model Training** - Train custom embeddings on your corpus.

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK Training System                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Training Corpus                                             │
│      ↓                                                       │
│  ┌─────────────────────────────────────┐                   │
│  │   Tokenization Phase                  │                   │
│  │  - TextTokenizer.build()             │                   │
│  │  - Multiple streams                   │                   │
│  │  - TokenRecord creation               │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Vocabulary Building                │                   │
│  │  - Collect unique tokens             │                   │
│  │  - Build token → index mapping       │                   │
│  │  - Calculate frequencies             │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Co-occurrence Matrix               │                   │
│  │  - Build context windows             │                   │
│  │  - Count co-occurrences               │                   │
│  │  - Create sparse matrix               │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Training Loop                      │                   │
│  │  For each epoch:                     │                   │
│  │    - Sample training pairs           │                   │
│  │    - Forward pass                    │                   │
│  │    - Calculate loss                  │                   │
│  │    - Backward pass                    │                   │
│  │    - Update embeddings                │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Model Saving                       │                   │
│  │  - Save embeddings                   │                   │
│  │  - Save vocabulary                   │                   │
│  │  - Save metadata                     │                   │
│  └─────────────────────────────────────┘                   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Enhanced Training (Multi-Stream):**

```
Multiple Token Streams
    ├─ char stream
    ├─ subword stream
    └─ word stream
        ↓
[Multi-Stream Learning]
    ├─ Learn at all granularities
    ├─ Cross-stream alignment
    └─ Hierarchical semantics
    ↓
[Temporal Awareness]
    ├─ Position-dependent embeddings
    └─ Sequence modeling
    ↓
[Content-ID Clustering]
    ├─ Deterministic grouping
    └─ Semantic clusters
    ↓
[Mathematical Properties]
    ├─ Frontend/backend integration
    └─ UID-based relationships
    ↓
Enhanced Embeddings
```

---

### 5. API Server Architecture

**FastAPI Server** - Production-ready RESTful API.

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK API Server Architecture                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Request Layer                          │    │
│  │  - HTTP Requests (REST)                            │    │
│  │  - WebSocket Connections                            │    │
│  │  - File Uploads                                     │    │
│  └──────────────┬────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Middleware Layer                       │    │
│  │  - CORS handling                                    │    │
│  │  - Authentication (JWT)                           │    │
│  │  - Request validation                              │    │
│  │  - Error handling                                  │    │
│  └──────────────┬────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Route Handlers                         │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │    │
│  │  │ Tokenize │  │ Embed    │  │ Train    │        │    │
│  │  └──────────┘  └──────────┘  └──────────┘        │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │    │
│  │  │ Upload   │  │ Search   │  │ Jobs     │        │    │
│  │  └──────────┘  └──────────┘  └──────────┘        │    │
│  └──────────────┬────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Processing Layer                       │    │
│  │  - TextTokenizer                                    │    │
│  │  - EmbeddingGenerator                               │    │
│  │  - VectorStore                                       │    │
│  │  - JobManager (async)                               │    │
│  └──────────────┬────────────────────────────────────┘    │
│                 ↓                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Response Layer                          │    │
│  │  - JSON responses                                    │    │
│  │  - Streaming responses                               │    │
│  │  - WebSocket messages                                │    │
│  │  - File downloads                                    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**API Endpoint Structure:**

```
/api/v1/
    ├─ POST /tokenize
    │   └─ Text → Tokens
    ├─ POST /embed
    │   └─ Text → Embeddings
    ├─ POST /train
    │   └─ Corpus → Model
    ├─ POST /upload
    │   └─ File → Processing
    ├─ GET /search
    │   └─ Query → Results
    ├─ GET /jobs/{id}
    │   └─ Job status
    └─ WebSocket /ws
        └─ Real-time streaming
```

---

### 6. Vector Store Architecture

**Vector Database Integration** - Multiple backend support.

```
┌─────────────────────────────────────────────────────────────┐
│              SanTOK Vector Store Architecture               │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Embeddings + Metadata                                       │
│      ↓                                                       │
│  ┌─────────────────────────────────────┐                   │
│  │   Vector Store Interface             │                   │
│  │  (Abstract base)                     │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Backend Selection                  │                   │
│  │  ┌──────────┐  ┌──────────┐         │                   │
│  │  │ ChromaDB │  │  FAISS   │         │                   │
│  │  └──────────┘  └──────────┘         │                   │
│  │  ┌──────────┐  ┌──────────┐         │                   │
│  │  │ Weaviate │  │ In-Memory│         │                   │
│  │  └──────────┘  └──────────┘         │                   │
│  └──────────────┬──────────────────────┘                   │
│                 ↓                                           │
│  ┌─────────────────────────────────────┐                   │
│  │   Storage Operations                  │                   │
│  │  - add(embedding, metadata)           │                   │
│  │  - search(query, top_k)               │                   │
│  │  - get(id)                            │                   │
│  │  - delete(id)                         │                   │
│  └─────────────────────────────────────┘                   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

### 7. Complete Data Flow Architecture

**End-to-End Processing Pipeline:**

```
┌─────────────────────────────────────────────────────────────┐
│              Complete SanTOK Pipeline                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Input: Text/String                                          │
│      ↓                                                       │
│  [1] Preprocessing                                           │
│      ├─ Normalize case                                       │
│      ├─ Clean punctuation                                    │
│      └─ Detect language                                      │
│      ↓                                                       │
│  [2] Tokenization (9 methods in parallel)                   │
│      ├─ Space, Word, Char                                    │
│      ├─ Grammar, Subword                                     │
│      └─ BPE, Syllable, Frequency, Byte                      │
│      ↓                                                       │
│  [3] Mathematical Analysis                                   │
│      ├─ UID assignment (Xorshift64*)                        │
│      ├─ Frontend digit (9-centric)                          │
│      ├─ Backend number                                       │
│      └─ Global ID                                            │
│      ↓                                                       │
│  [4] Embedding Generation                                    │
│      ├─ Feature extraction                                   │
│      ├─ Strategy selection                                   │
│      └─ Vector generation                                    │
│      ↓                                                       │
│  [5] Storage/Reasoning (Optional)                            │
│      ├─ Vector Store (ChromaDB/FAISS/Weaviate)             │
│      └─ Cognitive Reasoning (Knowledge Graph)               │
│      ↓                                                       │
│  Output: Tokens + Embeddings + Metadata                      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

### 8. Component Interaction Diagram

```
┌──────────────┐
│   User/API   │
└──────┬───────┘
       │
       ↓
┌──────────────────┐
│  API Server      │
│  (FastAPI)      │
└──────┬───────────┘
       │
       ├──────────────┐
       │              │
       ↓              ↓
┌──────────────┐  ┌──────────────┐
│ TextTokenizer│  │ EmbeddingGen │
└──────┬───────┘  └──────┬───────┘
       │                 │
       ├─────────┐       │
       │         │       │
       ↓         ↓       ↓
┌──────────┐ ┌──────────┐ ┌──────────┐
│Cognitive │ │ Vector   │ │ Training │
│Reasoning │ │ Store    │ │ System   │
└──────────┘ └──────────┘ └──────────┘
```

---

### Key Design Principles

1. **Modularity**: Each component is independent and can be used separately
2. **Determinism**: Same input always produces same output
3. **Extensibility**: Easy to add new tokenization methods or embedding strategies
4. **Performance**: Parallel processing where possible
5. **Scalability**: Supports large-scale processing
6. **Explainability**: Full traceability of all operations

---

## 🚀 Installation

### Prerequisites

- **Python**: 3.11 or higher
- **pip**: Python package installer
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 2GB free space

### Method 1: Automated Setup (Recommended)

**Linux/Mac:**
```bash
git clone <repository-url>
cd SanTOK-Code-Only
chmod +x setup.sh  # if setup script exists
./setup.sh
```

**Windows:**
```powershell
git clone <repository-url>
cd SanTOK-Code-Only
.\setup.bat  # if setup script exists
```

### Method 2: Manual Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd SanTOK-Code-Only
```

2. **Create virtual environment:**
```bash
python -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Install the package (optional):**
```bash
pip install -e .
```

### Method 3: Docker (If Available)

```bash
docker-compose up
```

### Verify Installation

```bash
python check_system.py
```

Or test in Python:
```python
from santok import TextTokenizationEngine

engine = TextTokenizationEngine()
result = engine.tokenize("Hello World", "whitespace")
print(result['tokens'])  # Should print: ['Hello', 'World']
```

---

## ⚡ Quick Start

### Method 1: Basic Tokenization (Python)

```python
from santok import TextTokenizationEngine

# Create engine
engine = TextTokenizationEngine(
    random_seed=12345,
    normalize_case=True,
    remove_punctuation=False
)

# Tokenize text
text = "Hello World! This is SanTOK."
result = engine.tokenize(text, tokenization_method="whitespace")

print(f"Tokens: {result['tokens']}")
print(f"Frontend Digits: {result['frontend_digits']}")
print(f"Features: {result['features']}")
```

### Method 2: Using Core Tokenizer (Advanced)

```python
from src.core.core_tokenizer import TextTokenizer

# Create tokenizer
tokenizer = TextTokenizer(seed=42, embedding_bit=False)

# Build token streams (multiple methods at once)
streams = tokenizer.build("Hello World! This is SanTOK.")

# Access different tokenization methods
word_tokens = streams["word"].tokens
char_tokens = streams["char"].tokens
subword_tokens = streams["subword"].tokens

# Each token has: text, uid, index, content_id, frontend_digit, backend_number, global_id
for token in word_tokens[:5]:
    print(f"Text: {token.text}, UID: {token.uid}, Frontend: {token.frontend_digit}")
```

### Method 3: Using the CLI

```bash
# Tokenize text
python santok_cli.py tokenize --text "Hello world" --method word

# Tokenize file
python santok_cli.py tokenize --file data.txt --output tokens.json

# Train embeddings
python santok_cli.py train --file corpus.txt --model-path model.pkl

# Generate embeddings
python santok_cli.py embed --text "Hello world" --model-path model.pkl

# Show system information
python santok_cli.py info
```

### Method 4: Start the API Server

```bash
# Option 1: Using run script (recommended)
python run.py

# Option 2: Direct start
python start.py

# Option 3: For Railway/Heroku deployment
python main.py  # Auto-detects app from src.servers.main_server

# Server will be available at http://localhost:8000
# Interactive API docs at http://localhost:8000/docs
# Alternative docs at http://localhost:8000/redoc
```

### Method 5: API Example (REST)

```bash
# Tokenize via API
curl -X POST "http://localhost:8000/api/v1/tokenize" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "method": "word"}'

# Generate embeddings
curl -X POST "http://localhost:8000/api/v1/embed" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "strategy": "feature_based"}'

# Health check
curl http://localhost:8000/api/v1/health
```

### Method 6: WebSocket (Real-time)

```python
import asyncio
import websockets
import json

async def tokenize_websocket():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        # Send tokenize request
        await websocket.send(json.dumps({
            "action": "tokenize",
            "text": "Hello world",
            "method": "word"
        }))
        
        # Receive results
        result = await websocket.recv()
        print(json.loads(result))

asyncio.run(tokenize_websocket())
```

---

## 🧩 Core Components

### 1. Core Tokenization (`santok/` and `src/core/`)

**Main Classes:**
- `TextTokenizationEngine` - Main tokenization engine
- `TextTokenizer` - Core tokenizer with multiple methods
- `BaseTokenizer` - Base class for custom tokenizers
- `ParallelTokenizer` - Parallel processing support

**Tokenization Methods:**
- `space` / `whitespace` - Split by whitespace characters
- `word` - Word-based tokenization (alphabetic characters)
- `char` / `character` - Character-level tokenization
- `grammar` - Grammar-aware tokenization with punctuation handling
- `subword` - Basic subword tokenization
- `subword_bpe` - Byte-Pair Encoding (BPE) subword tokenization
- `subword_frequency` - Frequency-based subword tokenization
- `subword_syllable` - Syllable-based subword tokenization
- `byte` - Byte-level tokenization (ord-based)

**Multi-language Support:**
- Automatic language detection
- Support for CJK (Chinese, Japanese, Korean)
- Arabic, Cyrillic, Hebrew, Thai, Devanagari support
- Language-specific word boundary detection

### 2. Embeddings (`src/embeddings/`)

**Components:**
- `SanTOKEmbeddingGenerator` - Generate embeddings from text
- `SanTOKVectorStore` - Store and search embeddings
- `SanTOKSemanticTrainer` - Train semantic models
- `SanTOKInferencePipeline` - Inference pipeline
- `EnhancedSanTOKSemanticTrainer` - Enhanced training with multi-stream learning

**Embedding Strategies:**
- `feature_based` - Mathematical feature-based embeddings
- `hash_based` - Hash-based embeddings
- `semantic` - Trained semantic embeddings
- `hybrid` - Combination of multiple strategies

### 3. Vector Stores (`src/embeddings/` and `weaviate_codes/`)

**Supported Databases:**
- **ChromaDB** - Lightweight vector database
- **FAISS** - Facebook AI Similarity Search
- **Weaviate** - Cloud-native vector database

### 4. Cognitive Reasoning (`santok_cognitive/`)

**Components:**
- `UnifiedMemory` - Unified memory system
- `SanTOKReasoner` - Symbolic reasoning engine
- `GraphStore` - Knowledge graph storage
- `TreeStore` - Hierarchical tree storage
- `InferenceEngine` - Inference rule engine

**Features:**
- 15+ relation types
- 20+ inference rules
- Contradiction detection
- Confidence propagation
- Full explainability

### 5. API Servers (`src/servers/`)

**Available Servers:**
- `main_server.py` - Full-featured FastAPI server
- `lightweight_server.py` - Lightweight API server
- `simple_server.py` - Simple HTTP server
- `api_server.py` - Alternative API implementation

**Features:**
- RESTful API endpoints
- WebSocket support
- File upload/download
- Job management
- Authentication (JWT)
- Interactive documentation

### 6. Training (`src/training/` and `enhanced_semantic_trainer/`)

**Components:**
- `SanTOKVocabularyBuilder` - Build vocabularies
- `SanTOKLanguageModelTrainer` - Train language models
- `EnhancedSanTOKSemanticTrainer` - Enhanced semantic training
- `DatasetDownloader` - Download training datasets

### 7. Small Language Models (`santok_cognitive/slm/`)

**Components:**
- Transformer-based small language models
- Training scripts
- Model loading and inference
- Vocabulary expansion

### 8. Integration (`src/integration/`)

**Components:**
- `VocabularyAdapter` - Adapt vocabularies between systems
- `SourceMapIntegration` - Source map integration
- `CognitivePipeline` - Integration with cognitive reasoning

### 9. Utilities (`santok/utils/` and `src/utils/`)

**Components:**
- `Config` - Configuration management
- `LoggingConfig` - Logging setup
- `Validation` - Input validation
- `UniqueIdentifier` - UID generation

---

## 📖 Usage Examples

### Example 1: Comprehensive Text Analysis

```python
from santok import TextTokenizationEngine

engine = TextTokenizationEngine()

# Analyze with all methods
text = "SanTOK is an advanced text processing framework."
analysis = engine.analyze_text(text)

# Access results for each method
for method, result in analysis.items():
    print(f"{method}: {len(result['tokens'])} tokens")
    print(f"  Frontend Digits: {result['frontend_digits']}")
    print(f"  Features: {result['features']}")
```

### Example 2: Semantic Embedding Training

```python
from src.core.core_tokenizer import TextTokenizer
from src.embeddings.semantic_trainer import SanTOKSemanticTrainer

# Tokenize corpus
tokenizer = TextTokenizer(seed=42)
streams = tokenizer.build(your_corpus_text)

# Train semantic embeddings
trainer = SanTOKSemanticTrainer(
    embedding_dim=768,
    epochs=10,
    window_size=5
)

# Collect all tokens
all_tokens = []
for stream in streams.values():
    all_tokens.extend(stream.tokens)

# Build vocabulary and train
trainer.build_vocab(all_tokens)
trainer.build_cooccurrence(all_tokens)
trainer.train(all_tokens)

# Save model
trainer.save("model.pkl")

# Get embedding for a token
embedding = trainer.get_embedding(token_uid)
```

### Example 3: Enhanced Semantic Training

```python
from enhanced_semantic_trainer import EnhancedSanTOKSemanticTrainer
from src.core.core_tokenizer import TextTokenizer

# Tokenize
tokenizer = TextTokenizer()
streams = tokenizer.build(your_text)

# Train with enhanced features
trainer = EnhancedSanTOKSemanticTrainer(
    embedding_dim=768,
    epochs=10,
    window_size=5,
    use_multi_stream=True,
    use_temporal=True,
    use_content_id_clustering=True,
    use_math_properties=True
)

trainer.train(streams)
trainer.save("enhanced_model.pkl")
```

### Example 4: Cognitive Reasoning

```python
from santok_cognitive import UnifiedMemory, SanTOKReasoner

# Create memory
memory = UnifiedMemory()

# Add knowledge
memory.add("Python is a programming language", "fact", auto_link_graph=True)
memory.add("Programming languages are used for software development", "fact", auto_link_graph=True)

# Create reasoner
reasoner = SanTOKReasoner(memory)

# Ask question
answer = reasoner.ask("What is Python?")

print(answer.text)
print(answer.explain())  # Full reasoning trace
```

### Example 5: Vector Store Integration

```python
from src.embeddings.embedding_generator import SanTOKEmbeddingGenerator
from src.embeddings.vector_store import SanTOKVectorStore

# Generate embeddings
generator = SanTOKEmbeddingGenerator(strategy="feature_based")
embedding = generator.generate("Hello world")

# Store in vector database
store = SanTOKVectorStore()
doc_id = store.add(embedding, metadata={"text": "Hello world", "id": 1})

# Search
query_embedding = generator.generate("greeting")
results = store.search(query_embedding, top_k=5)

for result in results:
    print(f"Score: {result['score']}, Metadata: {result['metadata']}")
```

### Example 6: API Server Usage

```python
from fastapi import FastAPI
from santok import TextTokenizationEngine

app = FastAPI()
engine = TextTokenizationEngine()

@app.post("/tokenize")
async def tokenize(text: str, method: str = "whitespace"):
    result = engine.tokenize(text, method)
    return result

# Run with: uvicorn main:app --reload
```

---

## 📚 API Documentation

### REST API Endpoints

When the server is running, visit `http://localhost:8000/docs` for interactive Swagger documentation or `http://localhost:8000/redoc` for ReDoc documentation.

**Core Endpoints:**

- `POST /api/v1/tokenize` - Tokenize text with multiple methods
- `POST /api/v1/embed` - Generate embeddings from text
- `POST /api/v1/train` - Train semantic embedding model
- `GET /api/v1/health` - Health check endpoint
- `GET /api/v1/info` - System information
- `POST /api/v1/analyze` - Comprehensive text analysis

**File Operations:**

- `POST /api/v1/upload` - Upload file for processing
- `POST /api/v1/tokenize/file` - Tokenize uploaded file
- `GET /api/v1/download/{file_id}` - Download processed results

**WebSocket:**

- `WebSocket /ws` - Real-time streaming tokenization
- `WebSocket /ws/train` - Real-time training progress

**Job Management:**

- `POST /api/v1/jobs` - Create async job
- `GET /api/v1/jobs/{job_id}` - Get job status
- `GET /api/v1/jobs/{job_id}/result` - Get job result

**Example Requests:**

**Tokenize Text:**
```bash
curl -X POST "http://localhost:8000/api/v1/tokenize" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "method": "word",
    "compute_features": true,
    "seed": 42
  }'
```

**Response:**
```json
{
  "tokens": ["Hello", "world"],
  "frontend_digits": [5, 6],
  "backend_numbers": [123, 456],
  "global_ids": [789, 101],
  "features": {
    "length_factor": 2,
    "balance_index": 5,
    "entropy_index": 0,
    "mean": 5.5,
    "variance": 0.25
  },
  "method": "word",
  "token_count": 2
}
```

**Generate Embeddings:**
```bash
curl -X POST "http://localhost:8000/api/v1/embed" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "strategy": "feature_based",
    "model_path": "model.pkl"
  }'
```

**Upload and Process File:**
```bash
curl -X POST "http://localhost:8000/api/v1/upload" \
  -F "file=@document.txt" \
  -F "method=word"
```

**WebSocket Example:**
```python
import asyncio
import websockets
import json

async def tokenize_stream():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        # Send request
        await websocket.send(json.dumps({
            "action": "tokenize",
            "text": "Hello world",
            "method": "word"
        }))
        
        # Receive streaming results
        while True:
            result = await websocket.recv()
            data = json.loads(result)
            if data.get("done"):
                break
            print(f"Token: {data.get('token')}")

asyncio.run(tokenize_stream())
```

---

## 💻 CLI Usage

### Tokenization Commands

```bash
# Tokenize text
python santok_cli.py tokenize --text "Hello world" --method word

# Tokenize file
python santok_cli.py tokenize --file data.txt --output tokens.json --format json

# Tokenize from URL
python santok_cli.py tokenize --url https://example.com/text.txt
```

### Training Commands

```bash
# Train basic model
python santok_cli.py train --file corpus.txt --model-path model.pkl

# Train with enhanced trainer
python santok_cli.py train --file corpus.txt --model-path model.pkl --enhanced

# Custom training parameters
python santok_cli.py train --file corpus.txt \
  --model-path model.pkl \
  --embedding-dim 768 \
  --epochs 20 \
  --window-size 5
```

### Embedding Commands

```bash
# Generate embeddings
python santok_cli.py embed --text "Hello world" --model-path model.pkl

# Generate with different strategy
python santok_cli.py embed --text "Hello world" \
  --strategy feature_based \
  --output embeddings.npy
```

### Utility Commands

```bash
# Run tests
python santok_cli.py test

# Quick tests
python santok_cli.py test --quick

# Show system information
python santok_cli.py info
```

### Using the santok CLI (if installed)

```bash
# After installation: pip install -e .
santok "Hello world" --method whitespace
santok "Hello world" --analyze --output results.json
```

---

## 🚢 Deployment

### Local Development

```bash
# Start development server
python run.py

# Or use uvicorn directly
uvicorn src.servers.main_server:app --reload --host 0.0.0.0 --port 8000
```

### Production Deployment

**Using Railway:**
```bash
# Railway auto-detects start.py
# Set PORT environment variable
railway up
```

**Using Docker:**
```bash
docker-compose up -d
```

**Using systemd (Linux):**
```bash
# Create service file
sudo nano /etc/systemd/system/santok.service

# Start service
sudo systemctl start santok
sudo systemctl enable santok
```

### Environment Variables

- `PORT` - Server port (default: 8000)
- `LOG_LEVEL` - Logging level (default: INFO)
- `WEAVIATE_URL` - Weaviate server URL (optional)
- `WEAVIATE_API_KEY` - Weaviate API key (optional)

---

## 📁 Project Structure

```
SanTOK-Code-Only/
├── santok/                      # Core tokenization package
│   ├── __init__.py              # Package initialization
│   ├── santok.py                # Main TextTokenizationEngine class
│   ├── cli.py                   # CLI interface (argparse-based)
│   └── utils/                   # Utility modules
│       ├── config.py            # Configuration management
│       ├── logging_config.py    # Logging setup
│       └── validation.py        # Input validation
│
├── santok_cognitive/            # Cognitive reasoning system
│   ├── __init__.py
│   ├── README.md                # Cognitive system documentation
│   ├── ARCHITECTURE.md          # Architecture documentation
│   ├── WHITEPAPER.md            # Technical whitepaper
│   ├── graph/                   # Knowledge graph implementation
│   │   ├── graph_node.py       # Graph node class
│   │   ├── graph_edge.py        # Graph edge class
│   │   ├── graph_store.py       # Graph storage
│   │   └── relation_extractor.py # Relation extraction
│   ├── trees/                   # Hierarchical tree structures
│   │   ├── tree.py              # Tree implementation
│   │   ├── tree_node.py         # Tree node class
│   │   └── tree_store.py        # Tree storage
│   ├── memory/                  # Unified memory system
│   │   ├── unified_memory.py   # Main memory class
│   │   └── memory_object.py    # Memory object representation
│   ├── reasoning/               # Inference and reasoning
│   │   ├── santok_reasoner.py  # Main reasoner
│   │   ├── inference_engine.py # Inference rule engine
│   │   ├── query_engine.py      # Query processing
│   │   ├── path_finder.py       # Path finding algorithms
│   │   ├── contradiction_detector.py # Contradiction detection
│   │   └── explainer.py        # Explanation generation
│   ├── algorithms/              # Custom SanTOK algorithms
│   │   ├── santok_ranker.py    # Hybrid relevance ranking
│   │   ├── nine_scorer.py      # 9-centric confidence scoring
│   │   ├── semantic_similarity.py # Semantic similarity
│   │   ├── graph_walker.py     # Graph traversal algorithms
│   │   └── pattern_matcher.py  # Pattern matching
│   ├── slm/                     # Small Language Models
│   │   ├── santok_slm_model.py # SLM model implementation
│   │   ├── tiny_slm.py          # Tiny transformer model
│   │   ├── slm_trainer.py      # Training scripts
│   │   └── [multiple training scripts]
│   └── integration/             # Integration modules
│       ├── cognitive_pipeline.py # Cognitive processing pipeline
│       ├── vector_bridge.py    # Vector store bridge
│       └── token_bridge.py      # Token bridge
│
├── santok_complete/             # Complete production system
│   ├── core/                    # Core tokenization
│   ├── embeddings/              # Embedding generation
│   ├── training/                # Model training
│   ├── servers/                 # API servers
│   └── vector_stores/           # Vector database integrations
│
├── src/                         # Main source code
│   ├── core/                    # Core tokenization engines
│   │   ├── core_tokenizer.py   # Main tokenizer (9 methods)
│   │   ├── base_tokenizer.py   # Base tokenizer class
│   │   └── parallel_tokenizer.py # Parallel processing
│   ├── embeddings/              # Embedding systems
│   │   ├── embedding_generator.py # Embedding generation
│   │   ├── semantic_trainer.py  # Semantic model training
│   │   ├── vector_store.py      # Vector storage
│   │   ├── weaviate_vector_store.py # Weaviate integration
│   │   └── inference_pipeline.py # Inference pipeline
│   ├── servers/                 # API servers
│   │   ├── main_server.py      # Full-featured FastAPI server
│   │   ├── lightweight_server.py # Lightweight server
│   │   ├── simple_server.py    # Simple HTTP server
│   │   ├── api_server.py       # Alternative API implementation
│   │   ├── job_manager.py       # Async job management
│   │   └── error_handling.py   # Error handling utilities
│   ├── training/                # Training modules
│   │   ├── vocabulary_builder.py # Vocabulary construction
│   │   ├── language_model_trainer.py # Language model training
│   │   └── dataset_downloader.py # Dataset management
│   ├── integration/             # Integration modules
│   │   ├── vocabulary_adapter.py # Vocabulary adaptation
│   │   └── source_map_integration.py # Source map integration
│   ├── compression/             # Compression algorithms
│   │   └── compression_algorithms.py # Text compression
│   ├── interpretation/          # Text interpretation
│   │   └── data_interpreter.py  # Data interpretation
│   ├── performance/             # Performance testing
│   │   ├── test_accuracy.py     # Accuracy tests
│   │   └── comprehensive_performance_test.py # Full benchmarks
│   ├── cli/                     # CLI tools
│   │   └── main.py              # CLI main entry
│   └── utils/                   # Utilities
│       └── unique_identifier.py # UID generation
│
├── backend/                     # Backend-specific code
│   ├── santok/                  # Backend tokenization package
│   ├── src/                     # Backend source (mirror of src/)
│   └── Architecture_Docs/       # Architecture documentation
│
├── enhanced_semantic_trainer/   # Enhanced semantic training
│   ├── enhanced_trainer.py     # Enhanced trainer implementation
│   ├── example_train.py         # Training examples
│   ├── example_use.py          # Usage examples
│   └── examples/                # Additional examples
│
├── examples/                    # Example scripts and demos
│   ├── embedding_example.py    # Embedding examples
│   ├── vector_store examples   # Vector store usage
│   ├── training examples       # Training examples
│   └── integration examples    # Integration examples
│
├── docs/                        # Comprehensive documentation
│   ├── api/                     # API documentation
│   ├── backend/                 # Backend documentation
│   ├── examples/                # Example documentation
│   ├── guides/                   # User guides
│   ├── integration/             # Integration guides
│   └── performance/             # Performance documentation
│
├── weaviate_codes/              # Weaviate integration
│   ├── weaviate_vector_store.py # Weaviate vector store
│   └── README.md                # Weaviate setup guide
│
├── main.py                      # Main entry point (Railway/Heroku)
├── run.py                       # Cross-platform run script
├── start.py                     # Server startup script
├── santok_cli.py                # Main CLI interface
├── check_system.py              # System verification script
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup configuration
├── Procfile                     # Heroku/Railway process file
├── runtime.txt                  # Python version specification
└── README.md                    # This comprehensive documentation
```

---

## 📚 Advanced Examples & Use Cases

### Complete Workflow Examples

SanTOK provides comprehensive example scripts demonstrating various use cases:

#### 1. Basic Tokenization Examples

**File**: `examples/embedding_example.py`
- Basic tokenization and embedding generation
- Token-by-token embedding visualization
- Document-level embeddings
- Vector store integration

**File**: `examples/train_semantic_embeddings.py`
- Training semantic embeddings from scratch
- Vocabulary building
- Model persistence

#### 2. Vector Store Examples

**File**: `examples/comprehensive_vector_store_example.py`
- Unified example combining ALL vector store capabilities
- Weaviate, FAISS, and ChromaDB integration
- Semantic search with filtering
- Concept exploration and clustering
- Context fusion embeddings
- Batch processing for large datasets

**File**: `examples/use_vector_store.py`
- Loading vector stores from disk
- Interactive search mode
- Cluster analysis
- Similarity comparisons

**File**: `examples/search_examples.py`
- Advanced search patterns
- Multi-level concept exploration
- Related concept finding
- Token comparison utilities

#### 3. Large-Scale Processing Examples

**File**: `examples/test_full_workflow_500k.py`
- Complete workflow for 500K+ token datasets
- Batch processing with disk saving
- Resume capability
- Memory-efficient embedding generation
- Wikipedia data integration

#### 4. Cognitive Reasoning Examples

**File**: `santok_cognitive/demo.py`
- Knowledge graph construction
- Tree-based hierarchical organization
- Symbolic reasoning demonstrations
- Inference rule applications
- Full pipeline examples

**File**: `santok_cognitive/showcase.py`
- Advanced cognitive features
- Query answering with explanations
- Contradiction detection
- Confidence propagation

#### 5. Integration Examples

**File**: `examples/integrate_source_map_workflow.py`
- Source map integration
- Metadata tracking
- Railway compute workflows

**File**: `examples/integration_with_transformers.py`
- Integration with external transformer models
- Hybrid embedding strategies
- Model comparison

**File**: `examples/quick_start_integration.py`
- Quick integration guide
- Common integration patterns

#### 6. Small Language Model Examples

**File**: `examples/santok_with_tiny_slm.py`
- SanTOK-native SLM usage
- Constraint-grounded generation
- No external AI dependencies

**File**: `examples/simple_tiny_slm.py`
- Basic SLM implementation
- Training and inference

#### 7. Quality Evaluation Examples

**File**: `examples/eval_embedding_quality.py`
- Embedding quality assessment
- Probe token evaluation
- Semantic alignment testing

**File**: `examples/compare_neighbors.py`
- Comparison between different stores/strategies
- Overlap analysis
- Performance benchmarking

#### 8. Data Interpretation Examples

**File**: `examples/test_data_interpreter.py`
- Real-time data interpretation
- Weaviate-based knowledge discovery
- Semantic relationship extraction

### Use Case Scenarios

#### Scenario 1: Document Processing Pipeline

```python
# 1. Tokenize documents
from src.core.core_tokenizer import TextTokenizer
tokenizer = TextTokenizer(method="word", seed=42)
tokens = tokenizer.tokenize_text("Your document text here...")

# 2. Generate embeddings
from src.embeddings.embedding_generator import SanTOKEmbeddingGenerator
generator = SanTOKEmbeddingGenerator(strategy="hybrid")
embeddings = generator.generate_embeddings(tokens)

# 3. Store in vector database
from src.embeddings.vector_store import ChromaVectorStore
store = ChromaVectorStore(collection_name="documents")
store.add_tokens(tokens, embeddings)

# 4. Semantic search
results = store.search(embeddings[0], top_k=10)
```

#### Scenario 2: Knowledge Base Construction

```python
# 1. Build knowledge graph
from santok_cognitive.memory.unified_memory import UnifiedMemory
memory = UnifiedMemory()

# 2. Add facts
obj1 = memory.add("Python is a programming language", "fact")
obj2 = memory.add("Python uses dynamic typing", "fact")

# 3. Create relationships
memory.add_relation(obj1.uid, obj2.uid, RelationType.RELATED_TO)

# 4. Query with reasoning
from santok_cognitive.reasoning.reasoner import SanTOKReasoner
reasoner = SanTOKReasoner(memory.graph)
answer = reasoner.answer("What is Python?")
print(answer.explanation)
```

#### Scenario 3: Real-Time Text Analysis

```python
# 1. Set up inference pipeline
from src.embeddings.inference_pipeline import SanTOKInferencePipeline
pipeline = SanTOKInferencePipeline(
    embedding_strategy="semantic",
    vector_store="chroma"
)

# 2. Process incoming text
result = pipeline.process_text(
    "Machine learning is a subset of artificial intelligence",
    store=True
)

# 3. Find similar concepts
similar = pipeline.similarity_search(
    "deep learning",
    top_k=5
)
```

#### Scenario 4: Training Custom Models

```python
# 1. Build vocabulary
from src.training.vocabulary_builder import SanTOKVocabularyBuilder
builder = SanTOKVocabularyBuilder()
vocab = builder.build_vocabulary("corpus.txt")

# 2. Train language model
from src.training.language_model_trainer import SanTOKLanguageModelTrainer
trainer = SanTOKLanguageModelTrainer(vocab)
model = trainer.train("corpus.txt", epochs=10)

# 3. Generate text
generated = model.generate("The future of AI", max_length=100)
```

#### Scenario 5: API Integration

```python
# Start API server
python run.py

# Use REST API
import requests

# Tokenize
response = requests.post("http://localhost:8000/api/v1/tokenize", json={
    "text": "Hello world",
    "method": "word"
})
tokens = response.json()

# Generate embeddings
response = requests.post("http://localhost:8000/api/v1/embed", json={
    "text": "Hello world",
    "strategy": "feature_based"
})
embeddings = response.json()
```

### Performance Optimization Examples

**File**: `src/performance/comprehensive_performance_test.py`
- Performance benchmarking
- Tokenizer comparison
- Reconstruction accuracy testing
- Speed optimization strategies

### Running Examples

To run any example:

```bash
# Navigate to examples directory
cd examples

# Run specific example
python comprehensive_vector_store_example.py

# Or run from project root
python examples/embedding_example.py
```

### Example Outputs

Most examples generate:
- **Token files**: JSON/CSV files with tokenized data
- **Embedding files**: NumPy arrays or pickle files
- **Vector store files**: Persistent database files
- **Report files**: Markdown/JSON reports with results
- **Visualization files**: PNG/SVG charts and graphs

---

## 🧪 Testing

### Automated Tests

```bash
# Quick smoke tests via CLI
python santok_cli.py test --quick

# Full test suite (if pytest tests exist)
python -m pytest tests/

# With coverage report
python -m pytest tests/ --cov=santok --cov-report=html

# Test specific module
python -m pytest tests/test_tokenization.py -v
```

### System Verification

```bash
# Check system setup and dependencies
python check_system.py

# This verifies:
# - Python version
# - Installed dependencies
# - File structure
# - Basic functionality
```

### Manual Testing

**Test Tokenization:**
```python
from santok import TextTokenizationEngine

engine = TextTokenizationEngine()
result = engine.tokenize("Hello World", "whitespace")
assert len(result['tokens']) == 2
assert result['tokens'][0] == 'Hello'
print("✓ Tokenization test passed")
```

**Test Core Tokenizer:**
```python
from src.core.core_tokenizer import TextTokenizer

tokenizer = TextTokenizer(seed=42)
streams = tokenizer.build("Hello World")
assert "word" in streams
assert len(streams["word"].tokens) > 0
print("✓ Core tokenizer test passed")
```

**Test Embeddings:**
```python
from src.embeddings.embedding_generator import SanTOKEmbeddingGenerator

generator = SanTOKEmbeddingGenerator(strategy="feature_based")
embedding = generator.generate("Hello world")
assert embedding is not None
assert len(embedding) > 0
print("✓ Embedding generation test passed")
```

**Test API Server:**
```bash
# Start server
python start.py &

# Test health endpoint
curl http://localhost:8000/api/v1/health

# Test tokenize endpoint
curl -X POST "http://localhost:8000/api/v1/tokenize" \
  -H "Content-Type: application/json" \
  -d '{"text": "test", "method": "word"}'
```

### Performance Testing

```python
# Run performance benchmarks
from src.performance.comprehensive_performance_test import run_performance_tests

results = run_performance_tests()
print(results)
```

### Example Test Scripts

Check the `examples/` directory for comprehensive test examples:
- `test_full_workflow_500k.py` - Large-scale workflow test
- `eval_embedding_quality.py` - Embedding quality evaluation
- `test_data_interpreter.py` - Data interpretation tests

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Run tests**
   ```bash
   python santok_cli.py test
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add your feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Submit a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Include tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Santosh Chavala**

- GitHub: [@chavalasantosh](https://github.com/chavalasantosh)
- Repository: [SanTOK](https://github.com/chavalasantosh/SanTOK)
- DeepWiki: [SanTOK Documentation](https://deepwiki.com/chavalasantosh/SanTOK)

---

## 🙏 Acknowledgments

- Built with Python 3.11+
- Uses FastAPI for API servers
- Integrates with Weaviate, ChromaDB, and FAISS
- Thanks to all contributors and the open-source community

---

## 📊 Project Statistics

- **Total Files**: 300+ Python files
- **Lines of Code**: 50,000+
- **Components**: 15+ major modules
- **Tokenization Methods**: 9+
- **Supported Python Versions**: 3.11+
- **API Endpoints**: 20+
- **Inference Rules**: 20+ (Cognitive)

---

## 🔗 Additional Resources

### Documentation Files

- **[SanTOK Cognitive Documentation](santok_cognitive/README.md)** - Cognitive reasoning system
- **[SanTOK Cognitive Architecture](santok_cognitive/ARCHITECTURE.md)** - Detailed architecture
- **[SanTOK Cognitive Whitepaper](santok_cognitive/WHITEPAPER.md)** - Technical whitepaper
- **[SanTOK Complete Documentation](santok_complete/README.md)** - Complete system docs
- **[Enhanced Trainer Documentation](enhanced_semantic_trainer/README.md)** - Enhanced training
- **[Weaviate Integration Guide](weaviate_codes/README.md)** - Weaviate setup and usage

### Interactive Documentation

- **API Swagger Docs**: `http://localhost:8000/docs` (when server is running)
- **API ReDoc**: `http://localhost:8000/redoc` (when server is running)

### Documentation Directories

- `docs/api/` - API documentation
- `docs/backend/Architecture_Docs/` - Backend architecture
- `docs/examples/` - Example documentation
- `docs/guides/` - User guides
- `docs/integration/` - Integration guides
- `docs/performance/` - Performance documentation

### Example Scripts

Check the `examples/` directory for:
- Embedding examples
- Vector store usage
- Training workflows
- Integration examples
- Performance benchmarks

---

## 🆘 Support & Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Change port
PORT=8001 python run.py
```

**Python version too old:**
- Install Python 3.11+ from [python.org](https://www.python.org/downloads/)

**Dependencies fail to install:**
```bash
pip install --upgrade pip
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Import errors:**
- Ensure you're in the project root directory
- Activate virtual environment
- Run `python check_system.py` to diagnose issues

### Getting Help

1. Check the documentation in `docs/`
2. Run `python check_system.py` to verify installation
3. Check server logs for error messages
4. Review examples in `examples/` directory
5. Open an issue on GitHub

---

## 📖 Quick Reference / Cheat Sheet

### Common Operations

**Tokenization:**
```python
from santok import TextTokenizationEngine
engine = TextTokenizationEngine(seed=42)
result = engine.tokenize("Hello World", method="word")
```

**Embeddings:**
```python
from src.embeddings.embedding_generator import SanTOKEmbeddingGenerator
generator = SanTOKEmbeddingGenerator(strategy="feature_based")
embeddings = generator.generate_embeddings(token_records)
```

**Vector Store:**
```python
from src.embeddings.vector_store import ChromaVectorStore
store = ChromaVectorStore(collection_name="docs")
store.add_tokens(tokens, embeddings)
results = store.search(query_embedding, top_k=10)
```

**Cognitive Reasoning:**
```python
from santok_cognitive.memory.unified_memory import UnifiedMemory
memory = UnifiedMemory()
obj = memory.add("Python is a language", "fact")
answer = memory.search_by_content("What is Python?")
```

**API Server:**
```bash
# Start server
python run.py

# Tokenize via API
curl -X POST http://localhost:8000/api/v1/tokenize \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World", "method": "word"}'
```

### Common Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `seed` | Random seed for reproducibility | `42` |
| `method` | Tokenization method | `"word"` |
| `strategy` | Embedding strategy | `"feature_based"` |
| `embedding_dim` | Embedding dimension | `768` |
| `top_k` | Number of results | `10` |

### File Locations

| Component | Location |
|-----------|----------|
| Core Tokenizer | `src/core/core_tokenizer.py` |
| Embeddings | `src/embeddings/` |
| Vector Stores | `src/embeddings/vector_store.py` |
| Cognitive | `santok_cognitive/` |
| API Server | `src/servers/main_server.py` |
| Examples | `examples/` |
| CLI | `santok_cli.py` |

---

## 🏭 Industry Use Cases & Applications

### Healthcare & Medical AI

**Use Case**: Explainable medical diagnosis support
- **Challenge**: Medical AI must be explainable and auditable
- **SanTOK Solution**: 
  - Deterministic reasoning with full explainability
  - Knowledge graphs for medical relationships
  - Constraint enforcement for safety
- **Benefits**: 
  - Traceable decisions
  - Regulatory compliance
  - No hallucination in critical medical information

**Example:**
```python
# Medical knowledge base
memory = UnifiedMemory()
memory.add("Aspirin reduces inflammation", source="medical_literature")
memory.add("Patient has inflammation", source="patient_record")

# Query with explanation
result = memory.query("Should patient take aspirin?")
# Returns: Answer + Full reasoning trace + Confidence + Sources
```

### Finance & Banking

**Use Case**: Auditable financial decision systems
- **Challenge**: Financial decisions must be traceable and compliant
- **SanTOK Solution**:
  - Full audit trails
  - Contradiction detection
  - Source tracking
- **Benefits**:
  - Regulatory compliance
  - Risk management
  - Fraud detection

**Example:**
```python
# Financial rules engine
memory = UnifiedMemory()
memory.add("High risk requires approval", relation=RelationType.RULE)
memory.add("Transaction is high risk", source="risk_engine")

# Automated decision with audit trail
decision = memory.reason("Should transaction be approved?")
# Returns: Decision + Complete audit trail + Rule chain
```

### Legal & Compliance

**Use Case**: Legal document analysis and reasoning
- **Challenge**: Legal reasoning must be precise and explainable
- **SanTOK Solution**:
  - Symbolic reasoning for legal logic
  - Knowledge graphs for case law
  - Full explainability
- **Benefits**:
  - Precise legal analysis
  - Case law relationships
  - Explainable conclusions

**Example:**
```python
# Legal knowledge base
memory = UnifiedMemory()
memory.add("Contract breach requires damages", relation=RelationType.IMPLIES)
memory.add("Party A breached contract", source="evidence")

# Legal reasoning
conclusion = memory.reason("What are the legal consequences?")
# Returns: Conclusion + Legal reasoning chain + Precedents
```

### Enterprise Knowledge Management

**Use Case**: Internal knowledge bases with guarantees
- **Challenge**: Enterprise knowledge must be reliable and searchable
- **SanTOK Solution**:
  - Unified memory (vector + graph + tree)
  - Source tracking
  - Temporal awareness
- **Benefits**:
  - Reliable knowledge retrieval
  - Source attribution
  - Knowledge evolution tracking

**Example:**
```python
# Enterprise knowledge base
memory = UnifiedMemory()
memory.add("Product X uses technology Y", source="engineering_team", date="2024-01-15")
memory.add("Technology Y is deprecated", source="tech_lead", date="2024-03-20")

# Temporal-aware query
results = memory.search("What technology does Product X use?")
# Returns: Current answer + Historical changes + Source timeline
```

### Customer Support

**Use Case**: AI-powered customer support with full audit trails
- **Challenge**: Support responses must be accurate and traceable
- **SanTOK Solution**:
  - Constraint-grounded generation
  - Knowledge validation
  - Full audit trails
- **Benefits**:
  - Accurate responses
  - Source attribution
  - Quality assurance

**Example:**
```python
# Support knowledge base
memory = UnifiedMemory()
memory.add("Feature X requires subscription Y", source="product_docs")
memory.add("Customer has subscription Y", source="customer_db")

# Support query
response = memory.query("Can customer use Feature X?")
# Returns: Answer + Knowledge sources + Confidence + Audit trail
```

### Research & Academia

**Use Case**: Research paper analysis and knowledge extraction
- **Challenge**: Extract and reason about research findings
- **SanTOK Solution**:
  - Semantic embeddings for paper similarity
  - Knowledge graphs for research relationships
  - Citation tracking
- **Benefits**:
  - Research discovery
  - Citation networks
  - Knowledge synthesis

**Example:**
```python
# Research knowledge base
memory = UnifiedMemory()
memory.add("Study A shows X causes Y", source="paper_123", citation=True)
memory.add("Study B contradicts Study A", source="paper_456", citation=True)

# Research query
findings = memory.query("What is the relationship between X and Y?")
# Returns: Findings + Contradictions + Citations + Confidence
```

### Software Development

**Use Case**: Code analysis and documentation
- **Challenge**: Understand code relationships and generate documentation
- **SanTOK Solution**:
  - Code tokenization (supports any file type)
  - Semantic embeddings for code similarity
  - Knowledge graphs for code relationships
- **Benefits**:
  - Code understanding
  - Documentation generation
  - Refactoring support

**Example:**
```python
# Code knowledge base
memory = UnifiedMemory()
memory.add("Function X calls Function Y", source="codebase", relation=RelationType.CALLS)
memory.add("Function Y is deprecated", source="changelog")

# Code analysis
analysis = memory.query("What functions does Function X depend on?")
# Returns: Dependencies + Status + Recommendations
```

---

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q: What makes SanTOK different from other tokenizers?**
A: SanTOK provides deterministic UIDs, mathematical properties (frontend/backend numbers), perfect reversibility, and integrates tokenization with embeddings, vector stores, and cognitive reasoning - all in one framework.

**Q: Do I need external models (BERT, GPT, etc.) to use SanTOK?**
A: No! SanTOK is self-contained. You can train your own embeddings and models using only SanTOK components. External models are optional for hybrid strategies.

**Q: Is SanTOK production-ready?**
A: Yes! SanTOK includes production-ready APIs, error handling, logging, monitoring, and deployment configurations for platforms like Railway and Heroku.

**Q: What file types does SanTOK support?**
A: SanTOK supports ANY file type - text, images, videos, audio, binary files, executables, archives, and more. It's a universal tokenization system.

**Q: How fast is SanTOK?**
A: SanTOK is optimized for performance with parallel processing, caching, and efficient algorithms. See the Performance Benchmarks section for detailed metrics.

### Technical Questions

**Q: What is a deterministic UID?**
A: A deterministic UID is a unique identifier that is always the same for the same token. Same input = same UID, every time. This enables reproducible results.

**Q: What are frontend and backend numbers?**
A: Frontend digits (1-9) represent semantic categories, while backend numbers provide positional encoding. These mathematical properties help models understand relationships.

**Q: Can I use SanTOK with existing models?**
A: Yes! SanTOK provides adapters and integration tools to work with external models, transformers, and other NLP tools.

**Q: How do I choose between embedding strategies?**
A: 
- **Feature-based**: Fast, deterministic, no training needed
- **Semantic**: Best quality, requires training on your data
- **Hash-based**: Ultra-fast, good for large-scale applications
- **Hybrid**: Combines multiple strategies for best results

**Q: What vector store should I use?**
A:
- **FAISS**: Fast, in-memory, good for development
- **ChromaDB**: Persistent, disk-based, good for local deployment
- **Weaviate**: Cloud-native, scalable, best for production

### Training Questions

**Q: How much data do I need to train embeddings?**
A: Minimum 100K tokens recommended, but 1M+ tokens produces better results. The more domain-specific data, the better.

**Q: How long does training take?**
A: Depends on dataset size and hardware. Typical training: 10-30 minutes for 1M tokens on modern CPUs, faster with GPUs.

**Q: Can I resume training?**
A: Yes! SanTOK supports checkpointing and resuming training from saved models.

**Q: How do I know if my model is ready?**
A: Check the Model Readiness Checklist in the documentation. Key indicators: loss converged, perplexity reasonable, generation quality acceptable.

### Deployment Questions

**Q: Can I deploy SanTOK to cloud platforms?**
A: Yes! SanTOK includes configurations for Railway, Heroku, and other platforms. See the Deployment section for details.

**Q: What are the system requirements?**
A: Python 3.11+, 2GB+ RAM recommended, more for large datasets. No GPU required (but helps for training).

**Q: Is SanTOK secure?**
A: Yes! SanTOK includes JWT authentication, input validation, safe error handling, and security best practices.

---

## 📊 Comparison with Alternatives

### SanTOK vs. Standard Tokenizers

| Feature | Standard Tokenizers | SanTOK |
|---------|-------------------|--------|
| Deterministic UIDs | ❌ | ✅ |
| Mathematical Properties | ❌ | ✅ |
| Perfect Reversibility | ❌ | ✅ |
| Multiple Granularities | Limited | ✅ (9+ methods) |
| Embedding Integration | ❌ | ✅ |
| Vector Store Integration | ❌ | ✅ |
| Cognitive Reasoning | ❌ | ✅ |
| Self-Contained | ❌ | ✅ |

### SanTOK vs. RAG Systems

| Feature | RAG | SanTOK |
|---------|-----|--------|
| Structured Knowledge | ❌ | ✅ |
| Inference Rules | ❌ | ✅ (20+) |
| Constraint Enforcement | ❌ | ✅ |
| Explainability | ❌ | ✅ Full |
| No Hallucination | ❌ | ✅ |
| Deterministic | ❌ | ✅ |

### SanTOK vs. Knowledge Graphs

| Feature | Knowledge Graphs | SanTOK |
|---------|-----------------|--------|
| Natural Language Output | ❌ | ✅ |
| Inference Rules | Limited | ✅ (20+) |
| Constraint Enforcement | ❌ | ✅ |
| Full Explainability | Partial | ✅ |
| Integration with LLMs | ❌ | ✅ |

### SanTOK vs. Standard Embeddings

| Feature | Standard Embeddings | SanTOK Embeddings |
|---------|-------------------|------------------|
| External Dependencies | ✅ Required | ❌ Optional |
| Domain-Specific | ❌ Generic | ✅ Your domain |
| Mathematical Properties | ❌ | ✅ |
| Training Required | ❌ Pre-trained | ✅ Self-trained |
| Speed | Slow (50ms+) | Fast (2ms) |

---

## ⚠️ Known Limitations

### Current Limitations

1. **Large Vocabulary Training**: Training embeddings on vocabularies >100K tokens may require significant memory. Use sparse representations or batch processing.

2. **Language Support**: SanTOK works best with English text. Other languages may require additional preprocessing.

3. **GPU Acceleration**: While SanTOK can use GPUs, it's primarily optimized for CPU usage. GPU support is optional.

4. **Real-time Processing**: Very large files (>10GB) may require chunked processing rather than real-time.

5. **Vector Store Scaling**: FAISS and ChromaDB have practical limits. For very large scale (>100M vectors), consider Weaviate.

### Workarounds

- **Large Vocabularies**: Use `max_vocab_size` parameter to limit vocabulary
- **Memory Issues**: Enable batch processing and disk saving
- **Performance**: Use parallel processing for large datasets
- **Scaling**: Use Weaviate for cloud-native, scalable vector storage

---

## 💡 Best Practices & Recommendations

### Tokenization

1. **Choose the Right Method**: 
   - Use `word` for general text
   - Use `subword` for code or technical text
   - Use `char` for character-level analysis

2. **Set a Seed**: Always use a consistent seed for reproducible results:
   ```python
   tokenizer = TextTokenizer(seed=42)
   ```

3. **Enable Features**: Compute features for better embeddings:
   ```python
   result = tokenizer.tokenize_text(text, compute_features=True)
   ```

### Embeddings

1. **Train on Your Domain**: Don't rely on generic embeddings - train on your specific domain data.

2. **Use Hybrid Strategy**: For best results, use hybrid embeddings combining feature-based and semantic.

3. **Normalize Embeddings**: Always normalize embeddings for consistent similarity calculations.

4. **Batch Processing**: For large datasets, use batch processing to avoid memory issues.

### Training

1. **Sufficient Data**: Use at least 100K tokens, preferably 1M+ for good results.

2. **Multiple Epochs**: Train for at least 10 epochs, more for complex domains.

3. **Validation**: Always validate on held-out data to prevent overfitting.

4. **Checkpointing**: Save models regularly to enable resuming training.

### Deployment

1. **Use Production Servers**: Use `main_server.py` for production, not `simple_server.py`.

2. **Enable Authentication**: Use JWT authentication for production APIs.

3. **Monitor Performance**: Enable logging and monitoring for production deployments.

4. **Use Vector Stores**: For production, use persistent vector stores (ChromaDB or Weaviate).

### Performance

1. **Parallel Processing**: Enable parallel processing for large datasets.

2. **Caching**: Enable caching for frequently accessed data.

3. **Batch Operations**: Use batch operations for vector stores.

4. **Choose Right Backend**: Use FAISS for speed, Weaviate for scale.

---

## 🗺️ Roadmap & Future Plans

### Short Term (Next Release)

- [ ] Enhanced GPU acceleration support
- [ ] Additional language support (multilingual tokenization)
- [ ] More vector store backends (Pinecone, Qdrant)
- [ ] Improved documentation and tutorials
- [ ] Performance optimizations

### Medium Term (6 Months)

- [ ] Advanced model compression techniques
- [ ] Distributed training support
- [ ] Enhanced API features (GraphQL support)
- [ ] Web UI for model management
- [ ] More inference rules for cognitive reasoning

### Long Term (1 Year)

- [ ] Full multilingual support
- [ ] Advanced model architectures
- [ ] Integration with more LLM providers
- [ ] Enterprise features (SSO, RBAC)
- [ ] Advanced analytics and monitoring

---

## 📝 Version History

### Current Version: 1.0.0

**Features:**
- Complete tokenization system (9+ methods)
- Semantic embedding training
- Vector store integration (ChromaDB, FAISS, Weaviate)
- Cognitive reasoning system
- Production-ready APIs
- Comprehensive documentation

**For detailed changelog, see:** [CHANGELOG.md](CHANGELOG.md) (if available)

---

## 🔄 Migration Guide

### Migrating from Standard Tokenizers

1. **Replace tokenizer calls**:
   ```python
   # Old
   tokens = tokenizer.tokenize(text)
   
   # New
   from santok import TextTokenizationEngine
   engine = TextTokenizationEngine()
   result = engine.tokenize(text, method="word")
   tokens = result['tokens']
   ```

2. **Update to use UIDs**:
   ```python
   # Old: Random IDs
   token_ids = [random_id(t) for t in tokens]
   
   # New: Deterministic UIDs
   token_ids = [token.uid for token in token_records]
   ```

3. **Migrate embeddings**:
   ```python
   # Old: External embeddings
   embeddings = bert_model.encode(tokens)
   
   # New: SanTOK embeddings
   from src.embeddings.embedding_generator import SanTOKEmbeddingGenerator
   generator = SanTOKEmbeddingGenerator(strategy="semantic")
   embeddings = generator.generate_embeddings(token_records)
   ```

### Migrating from RAG Systems

1. **Replace vector store**:
   ```python
   # Old: Generic vector store
   store = VectorStore()
   
   # New: SanTOK vector store
   from src.embeddings.vector_store import ChromaVectorStore
   store = ChromaVectorStore(collection_name="documents")
   ```

2. **Add cognitive reasoning**:
   ```python
   # Old: Simple retrieval
   results = store.search(query)
   
   # New: Cognitive reasoning
   from santok_cognitive.memory.unified_memory import UnifiedMemory
   memory = UnifiedMemory()
   results = memory.search_by_content(query)
   # Includes: Reasoning, validation, explainability
   ```

---

**SanTOK** - Your complete solution for text processing, from tokenization to cognitive reasoning and production deployment.
