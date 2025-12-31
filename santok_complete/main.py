#!/usr/bin/env python3
"""
SanTOK - Advanced Text Tokenization Framework
Main entry point for the application
"""

import sys
import os
from typing import NoReturn

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.core.core_tokenizer import tokenize_text, reconstruct_from_tokens
    from src.cli.main import main as cli_main
    from src.servers.main_server import app as main_app
    from src.servers.lightweight_server import app as lightweight_app
except ImportError as e:
    print(f"Error: Failed to import required modules: {e}", file=sys.stderr)
    print("Please ensure all dependencies are installed.", file=sys.stderr)
    sys.exit(1)

def main() -> None:
    """Main entry point"""
    print("🚀 SanTOK - Advanced Text Tokenization Framework")
    print("=" * 50)
    print("Available modes:")
    print("1. CLI Mode - Command line interface")
    print("2. Server Mode - Web API server")
    print("3. Lightweight Mode - Minimal server")
    print("4. Direct Mode - Direct function calls")
    
    choice = input("\nSelect mode (1-4): ").strip()
    
    if choice == "1":
        cli_main()
    elif choice == "2":
        print("Starting main server...")
        try:
            import uvicorn
            uvicorn.run(main_app, host="0.0.0.0", port=8000)
        except ImportError:
            print("Error: uvicorn is not installed. Install it with: pip install uvicorn", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error starting server: {e}", file=sys.stderr)
            sys.exit(1)
    elif choice == "3":
        print("Starting lightweight server...")
        try:
            import uvicorn
            uvicorn.run(lightweight_app, host="0.0.0.0", port=8001)
        except ImportError:
            print("Error: uvicorn is not installed. Install it with: pip install uvicorn", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error starting server: {e}", file=sys.stderr)
            sys.exit(1)
    elif choice == "4":
        demo_direct_mode()
    else:
        print(f"Invalid choice: '{choice}'. Please select 1-4.", file=sys.stderr)
        sys.exit(1)

def demo_direct_mode() -> None:
    """Demo direct function calls"""
    print("\n🔧 Direct Mode Demo")
    print("-" * 30)
    
    # Test text
    text = "Hello, world! This is a test."
    print(f"Input text: {text}")
    
    # Test different tokenizers
    tokenizers = ["space", "word", "char", "grammar"]
    
    for tokenizer_type in tokenizers:
        print(f"\n📝 {tokenizer_type.upper()} Tokenization:")
        try:
            tokens = tokenize_text(text, tokenizer_type)
            print(f"  Tokens: {len(tokens)}")
            print(f"  Sample: {[t['text'] for t in tokens[:5]]}")
            
            # Test reconstruction
            reconstructed = reconstruct_from_tokens(tokens, tokenizer_type)
            print(f"  Reconstructed: {reconstructed}")
            print(f"  Perfect: {'✅' if reconstructed == text else '❌'}")
        except Exception as e:
            print(f"  Error with {tokenizer_type} tokenizer: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()