"""
SanTOK Complete - Comprehensive Text Processing System
A complete NLP system with tokenization, embeddings, training, servers, and more
"""

__version__ = "2.0.0"
__author__ = "Santosh Chavala"
__email__ = "chavalasantosh@example.com"

# Core Tokenization
try:
    from .core.core_tokenizer import (
        tokenize_space,
        tokenize_word,
        tokenize_char,
        tokenize_grammar,
        tokenize_subword,
        TextTokenizer,
        TokenRecord,
    )
except ImportError:
    pass

try:
    from .core.santok_engine import TextTokenizationEngine, tokenize_text, analyze_text_comprehensive
except ImportError:
    pass

# Embeddings
try:
    from .embeddings.embedding_generator import SanTOKEmbeddingGenerator
    from .embeddings.vector_store import SanTOKVectorStore
    from .embeddings.inference_pipeline import SanTOKInferencePipeline
except ImportError:
    pass

# Vector Stores
try:
    from .vector_stores.weaviate_integration import *
except ImportError:
    pass

# Training
try:
    from .training.vocabulary_builder import SanTOKVocabularyBuilder
    from .training.language_model_trainer import SanTOKLanguageModel, SanTOKLanguageModelTrainer
    from .training.enhanced_trainer import *
except ImportError:
    pass

# Integration
try:
    from .integration.vocabulary_adapter import VocabularyAdapter
    from .integration.source_map_integration import SourceMapIntegration
except ImportError:
    pass

# Interpretation
try:
    from .interpretation.data_interpreter import DataInterpreter
except ImportError:
    pass

# Compression
try:
    from .compression.compression_algorithms import CompressionAlgorithm
except ImportError:
    pass

# Utilities
try:
    from .utils.config import Config, get_config
    from .utils.logging_config import setup_logging, get_logger
    from .utils.validation import (
        validate_text_input,
        validate_file_path,
        validate_port,
        ValidationError,
    )
except ImportError:
    pass

# CLI
try:
    from .cli.cli import main as cli_main
except ImportError:
    pass

__all__ = [
    # Core Tokenization
    'TextTokenizationEngine',
    'TextTokenizer',
    'TokenRecord',
    'tokenize_text',
    'tokenize_space',
    'tokenize_word',
    'tokenize_char',
    'tokenize_grammar',
    'tokenize_subword',
    'analyze_text_comprehensive',
    # Embeddings
    'SanTOKEmbeddingGenerator',
    'SanTOKVectorStore',
    'SanTOKInferencePipeline',
    # Training
    'SanTOKVocabularyBuilder',
    'SanTOKLanguageModel',
    'SanTOKLanguageModelTrainer',
    # Integration
    'VocabularyAdapter',
    'SourceMapIntegration',
    # Interpretation
    'DataInterpreter',
    # Compression
    'CompressionAlgorithm',
    # Utils
    'Config',
    'get_config',
    'setup_logging',
    'get_logger',
    'validate_text_input',
    'validate_file_path',
    'validate_port',
    'ValidationError',
    # CLI
    'cli_main',
]

