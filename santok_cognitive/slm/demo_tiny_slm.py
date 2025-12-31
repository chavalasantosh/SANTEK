"""
Demo: TinySLM - Ultra-lightweight Small Language Model

This demonstrates the TinySLM, a minimal SLM that:
- Runs on CPU with minimal memory (~1-5 MB)
- Uses simple n-gram statistics
- Works with SanTOK constraint system
- Perfect for low-resource environments

Usage:
    python demo_tiny_slm.py
"""

from .tiny_slm import TinySLMWrapper, TinySLMConfig
from .slm_generator import GenerationConfig, DecodingStrategy


def demo_basic_usage():
    """Basic usage example."""
    print("=" * 60)
    print("Demo 1: Basic TinySLM Usage")
    print("=" * 60)
    print()
    
    # Create SLM
    slm = TinySLMWrapper()
    
    # Load knowledge (facts from SanTOK Cognitive)
    facts = [
        "Python is a programming language",
        "Python was created by Guido van Rossum",
        "Python is used for web development",
        "Python supports object-oriented programming",
        "Python has a large standard library",
    ]
    
    slm.load_knowledge(facts)
    
    # Generate responses
    queries = [
        "What is Python?",
        "Who created Python?",
        "What is Python used for?",
    ]
    
    for query in queries:
        print(f"Query: {query}")
        result = slm.generate(query)
        print(f"Response: {result.text}")
        print(f"Tokens: {len(result.tokens)}")
        print()
    
    # Show statistics
    print(slm.explain())
    print()


def demo_custom_config():
    """Example with custom configuration."""
    print("=" * 60)
    print("Demo 2: Custom Configuration")
    print("=" * 60)
    print()
    
    # Custom config for more aggressive n-gram learning
    config = TinySLMConfig(
        max_ngram=4,  # Learn 4-grams
        ngram_weight=1.5,  # Higher weight on n-grams
        frequency_weight=0.3,  # Lower weight on frequency
    )
    
    slm = TinySLMWrapper(config)
    
    facts = [
        "Machine learning is a subset of artificial intelligence",
        "Deep learning uses neural networks",
        "Neural networks have multiple layers",
        "Training neural networks requires data",
        "Python is popular for machine learning",
    ]
    
    slm.load_knowledge(facts)
    
    query = "What is machine learning?"
    result = slm.generate(query)
    
    print(f"Query: {query}")
    print(f"Response: {result.text}")
    print()
    
    stats = slm.get_stats()
    print(f"Model memory: {stats['slm']['memory_estimate_mb']:.2f} MB")
    print(f"N-grams learned: {stats['slm']['ngram_count']}")
    print()


def demo_low_memory():
    """Demonstrate low memory usage."""
    print("=" * 60)
    print("Demo 3: Low Memory Configuration")
    print("=" * 60)
    print()
    
    # Configure for minimal memory
    config = TinySLMConfig(
        max_ngram=2,  # Only bigrams (smaller memory)
        max_vocab_size=5000,  # Limit vocabulary
        max_ngram_entries=10000,  # Limit n-gram storage
    )
    
    slm = TinySLMWrapper(config)
    
    # Small set of facts
    facts = [
        "SanTOK is a tokenization system",
        "SanTOK uses semantic embeddings",
        "SanTOK supports multiple languages",
    ]
    
    slm.load_knowledge(facts)
    
    query = "What is SanTOK?"
    result = slm.generate(query)
    
    print(f"Query: {query}")
    print(f"Response: {result.text}")
    print()
    
    stats = slm.get_stats()
    print("Memory Usage:")
    print(f"  Model: {stats['slm']['memory_estimate_mb']:.4f} MB")
    print(f"  Vocabulary: {stats['slm']['vocab_size']} tokens")
    print(f"  N-grams: {stats['slm']['ngram_count']}")
    print()


def demo_generation_strategies():
    """Demonstrate different generation strategies."""
    print("=" * 60)
    print("Demo 4: Generation Strategies")
    print("=" * 60)
    print()
    
    slm = TinySLMWrapper()
    
    facts = [
        "The sky is blue",
        "The sun is bright",
        "The moon is visible at night",
        "Stars twinkle in the sky",
    ]
    
    slm.load_knowledge(facts)
    
    query = "What is in the sky?"
    
    strategies = [
        ("Greedy", DecodingStrategy.GREEDY),
        ("Top-K", DecodingStrategy.TOP_K),
    ]
    
    for name, strategy in strategies:
        config = GenerationConfig(
            strategy=strategy,
            top_k=5,
            max_tokens=15,
        )
        
        # Note: We need to pass config to generate
        # For now, using default
        result = slm.generate(query)
        print(f"{name} Strategy:")
        print(f"  Response: {result.text}")
        print()


def main():
    """Run all demos."""
    print("\n" + "=" * 60)
    print("TinySLM - Ultra-lightweight Small Language Model Demo")
    print("=" * 60)
    print("\nThis SLM is designed for:")
    print("  - Low-resource environments")
    print("  - CPU-only inference")
    print("  - Minimal memory footprint (~1-5 MB)")
    print("  - Fast inference on any hardware")
    print()
    
    try:
        demo_basic_usage()
        demo_custom_config()
        demo_low_memory()
        demo_generation_strategies()
        
        print("=" * 60)
        print("All demos completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
