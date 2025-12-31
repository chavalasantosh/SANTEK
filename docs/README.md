# SanTOK - Universal Tokenization Framework

A comprehensive **universal tokenization system** that works on **ANY file type** - text, images, videos, audio, GIFs, binary files, and more - with mathematical analysis, statistical features, and a modern web interface.

## 🌟 Overview

SanTOK is a complete **universal tokenization framework** that combines advanced mathematical algorithms with a modern React-based web interface. It provides multiple tokenization strategies, statistical analysis, and real-time processing capabilities for **ANY file type** - not just text!

**SanTOK supports:**
- ✅ **Text files** (.txt, .md, .json, etc.)
- ✅ **Images** (.jpg, .png, .gif, .bmp, etc.)
- ✅ **Videos** (.mp4, .avi, .mov, etc.)
- ✅ **Audio** (.mp3, .wav, .flac, etc.)
- ✅ **GIFs** (animated and static)
- ✅ **Binary files** (.exe, .dll, .bin, etc.)
- ✅ **Archives** (.zip, .rar, .7z, etc.)
- ✅ **ANY other file type!**

See [`docs/SANTOK_UNIVERSAL_FILE_SUPPORT.md`](SANTOK_UNIVERSAL_FILE_SUPPORT.md) for complete details.

## ✨ Features

### 🔧 Core Tokenization Engine
- **Universal File Support**: Tokenize ANY file type - text, images, videos, audio, GIFs, binary files, executables, archives, and more
- **Multiple Tokenization Strategies**: Whitespace, word boundary, character, subword, and byte-level tokenization
- **Mathematical Analysis**: Weighted sum calculation, digital root computation, and hash-based algorithms
- **Statistical Features**: Mean, variance, entropy index, and balance index calculations
- **Configurable Processing**: Customizable preprocessing and processing parameters
- **Pure Python**: No external dependencies required for core functionality
- **Full Reversibility**: Reconstruct original files from tokens (even binary/media files)

### 🌐 Web Interface
- **Modern React/Next.js Frontend**: Responsive, interactive web dashboard
- **Real-time Processing**: Live tokenization and analysis
- **Universal File Upload Support**: Process ANY file type (text, images, videos, audio, etc.) up to 100GB+
- **Performance Analytics**: Comprehensive metrics and visualization
- **Multiple Output Formats**: JSON, CSV, XML, TXT, and binary formats

### 📊 Advanced Analytics
- **Comprehensive Testing**: Advanced test suites for massive datasets
- **Performance Monitoring**: Real-time performance metrics and analysis
- **Academic Documentation**: Professional IEEE papers and research documentation
- **Statistical Analysis**: Detailed mathematical analysis and comparison studies

### 🔗 Pretrained Model Integration
- **Vocabulary Adapter**: Bridge SanTOK tokenization with pretrained transformer models (BERT, GPT, T5, etc.)
- **Seamless Integration**: Use SanTOK's superior tokenization with HuggingFace models
- **Metadata Preservation**: Maintain SanTOK's frontend digits and backend numbers
- **See**: `docs/VOCABULARY_COMPATIBILITY_ISSUE.md` for details

### 🗺️ Universal Source Map System
- **50+ Knowledge Sources**: Wikipedia, ArXiv, GitHub, PubMed, and more
- **Source UID Generation**: Deterministic 64-bit hash-based source identification
- **Token Source Tagging**: Every token embeds `{source_id, algorithm_id, timestamp}` metadata
- **Weighted Embedding Merging**: Combine embeddings from multiple sources with weighted averaging
- **Hierarchical Profiling**: Track embedding performance per-source and per-category
- **Railway Compute Ready**: Cloud-friendly, persistent registry, distributed system compatible
- **See**: `docs/SANTOK_SOURCE_MAP.md` for complete documentation

## ⚠️ Important: Vocabulary Compatibility

**SanTOK generates its own token IDs that don't match pretrained model vocabularies.**

If you want to use SanTOK with pretrained models (BERT, GPT, etc.), you need to use the vocabulary adapter:

```python
from src.core.core_tokenizer import run_once
from src.integration.vocabulary_adapter import quick_convert_santok_to_model_ids

# Tokenize with SanTOK
santok_result = run_once("Hello world!", seed=42, embedding_bit=False)
tokens = [rec["text"] for rec in santok_result["word"]["records"]]

# Convert to model vocabulary IDs
model_ids = quick_convert_santok_to_model_ids(tokens, model_name="bert-base-uncased")

# Now safe to use with pretrained models!
```

**For new models trained from scratch with SanTOK:** Everything aligns perfectly - no adapter needed!

See `src/integration/README.md` and `docs/VOCABULARY_COMPATIBILITY_ISSUE.md` for complete details.

## 🗺️ Source Map System

SanTOK now includes a comprehensive source map system for tracking knowledge sources:

```python
from src.santok_sources import get_source_map
from src.integration.source_map_integration import create_source_aware_workflow

# Get source map
source_map = get_source_map()

# Process text with source tagging
result = create_source_aware_workflow(
    text="SanTOK is a universal tokenization system.",
    source_tag="wikipedia",
    tokenization_method="word",
    embedding_strategy="feature_based"
)

# Access source metadata
print(f"Source ID: {result['tokenization']['source_id']}")
print(f"Algorithm: {result['tokenization']['algorithm_id']}")
```

**Available Sources:**
- **Knowledge**: Wikipedia, Wikidata, ArXiv, PubMed, Project Gutenberg, StackExchange, Reddit, CommonCrawl
- **Technical**: HuggingFace Datasets, GitHub Corpus, Papers with Code, PyTorch/TensorFlow Docs
- **Domain**: Financial Reports, Legal Cases, Medical Guidelines, News Articles, Academic Theses
- **Symbolic**: Unicode Tables, ASCII Map, LaTeX Corpus, JSON Schema, YAML Configs, Regex Dataset
- **Cross-Modal**: Wikimedia Images, LAION-5B, OCR Corpus
- **Reinforcement**: User Feedback, Model Logs, Synthetic Corpus

See `docs/SANTOK_SOURCE_MAP.md` for complete documentation.

## 🚀 Quick Start

### Installation

#### From PyPI (Recommended)
```bash
pip install santok
```

#### From Source
```bash
git clone https://github.com/chavalasantosh/SanTOK.git
cd SanTOK
pip install -e .
```

### Basic Usage

#### Python API
```python
from santok import TextTokenizationEngine

# Create tokenization engine
tokenization_engine = TextTokenizationEngine(
    random_seed=12345,
    embedding_bit=False,
    normalize_case=True,
    remove_punctuation=False,
    collapse_repetitions=0
)

# Tokenize text
result = tokenization_engine.tokenize("Hello World!", "whitespace")

print(f"Tokens: {result['tokens']}")
print(f"Frontend Digits: {result['frontend_digits']}")
print(f"Features: {result['features']}")
```

#### Command Line Interface
```bash
# Basic tokenization
santok "Hello World!" --method whitespace

# With statistical features
santok "Hello World!" --method word --features

# Comprehensive analysis
santok "Hello World!" --analyze

# Process file
santok --file input.txt --method character --output results.json
```

#### Web Interface
```bash
# Start the web server
cd frontend
npm install
npm run dev

# Or use the Python server
python src/servers/main_server.py
```

## 🏗️ Project Structure

```
SanTOK/
├── 📁 santok/                    # Core Python package
│   ├── __init__.py              # Package initialization
│   ├── santok.py                # Main tokenization engine
│   └── cli.py                   # Command-line interface
├── 📁 frontend/                  # React/Next.js web interface
│   ├── app/                     # Next.js app directory
│   ├── components/              # React components
│   ├── lib/                     # Utility libraries
│   └── types/                   # TypeScript definitions
├── 📁 src/                      # Backend source code
│   ├── core/                    # Core tokenization algorithms
│   ├── servers/                 # Web servers and APIs
│   ├── tests/                   # Test suites and data
│   └── examples/                # Usage examples
├── 📁 docs/                     # Documentation and papers
│   ├── papers/                  # Academic papers
│   ├── guides/                  # User guides
│   └── performance/             # Performance documentation
├── 📁 data/                     # Sample data and outputs
│   ├── samples/                 # Sample datasets
│   └── outputs/                 # Generated outputs
├── 📁 scripts/                  # Setup and deployment scripts
├── setup.py                     # Python package configuration
├── package.json                 # Frontend dependencies
├── requirements.txt             # Python dependencies
└── main.py                      # Main entry point
```

## 🔬 Tokenization Methods

### Whitespace Tokenization
Splits text by whitespace delimiters.
```python
result = tokenization_engine.tokenize("Hello World!", "whitespace")
# Tokens: ["Hello", "World!"]
```

### Word Boundary Tokenization
Splits text into words (alphabetic characters only).
```python
result = tokenization_engine.tokenize("Hello World!", "word")
# Tokens: ["Hello", "World"]
```

### Character Tokenization
Splits text into individual characters.
```python
result = tokenization_engine.tokenize("Hello", "character")
# Tokens: ["H", "e", "l", "l", "o"]
```

### Subword Tokenization
Splits text into fixed-size subword units.
```python
result = tokenization_engine.tokenize("Hello", "subword", chunk_size=3)
# Tokens: ["Hel", "lo"]
```

## 🧮 Mathematical Features

### Frontend Digits
Small numbers (1-9) calculated using:
- **Weighted Sum**: ASCII value × position
- **Digital Root**: 9-centric reduction
- **Hash Value**: Polynomial rolling hash
- **Combined Digit**: (Weighted_Digit × 9 + Hash_Digit) % 9 + 1

### Statistical Features
- **Length Factor**: Number of tokens modulo 10
- **Balance Index**: Mean of frontend digits modulo 10
- **Entropy Index**: Variance of frontend digits modulo 10
- **Mean & Variance**: Standard statistical measures

## 🌐 Web Interface Features

### Dashboard
- **Real-time Processing**: Live tokenization and analysis
- **File Upload**: Support for large text files
- **Multiple Methods**: All tokenization strategies available
- **Performance Metrics**: Real-time statistics and analysis

### Analytics
- **Comprehensive Metrics**: Detailed performance analysis
- **Visualization**: Charts and graphs for data analysis
- **Export Options**: Multiple output formats
- **History Tracking**: Previous analysis results

## 📚 Documentation

### Academic Papers
- **Professional IEEE Paper**: Ready for publication
- **Comparison Analysis**: Detailed tokenization method comparisons
- **Performance Studies**: Comprehensive performance analysis
- **Mathematical Documentation**: Complete mathematical framework

### User Guides
- **Backend Integration**: API integration guide
- **Performance Optimization**: Performance tuning guide
- **Decoding Guide**: Text reconstruction methods
- **API Reference**: Complete API documentation

## 🧪 Testing

### Test Suites
```bash
# Run all tests
python -m pytest

# Run specific test categories
python src/tests/advanced_comprehensive_test.py
python src/tests/extreme_stress_test.py
python src/tests/real_time_monitor.py
```

### Performance Testing
- **Massive Dataset Testing**: Handles 100GB+ files
- **Stress Testing**: Extreme load testing
- **Real-time Monitoring**: Performance monitoring
- **Comprehensive Analysis**: Detailed test reports

## 🚀 Deployment

### Development
```bash
# Install dependencies
pip install -r requirements.txt
cd frontend && npm install

# Start development servers
python src/servers/main_server.py  # Backend
cd frontend && npm run dev         # Frontend
```

### Production
```bash
# Build for production
cd frontend && npm run build

# Deploy with Docker
docker build -t santok .
docker run -p 8000:8000 santok
```

## 📊 Performance

- **Large File Support**: Handles files up to 100GB+
- **High Performance**: Optimized algorithms for speed
- **Memory Efficient**: Minimal memory footprint
- **Scalable**: Supports concurrent processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Santosh Chavala**
- Email: chavalasantosh@example.com
- GitHub: [@chavalasantosh](https://github.com/chavalasantosh)

## 🙏 Acknowledgments

- Academic research and mathematical framework development
- Performance optimization and testing
- Web interface design and implementation
- Documentation and user experience

---

**SanTOK** - Universal Text Tokenization Framework for the modern era of natural language processing.