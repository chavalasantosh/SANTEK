#!/usr/bin/env python3
"""
Quick test to verify santok_complete module works
"""

import sys
import os

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

print("Testing santok_complete module...")
print("=" * 50)

try:
    import santok_complete
    print(f"✅ Module imported successfully!")
    print(f"   Version: {santok_complete.__version__}")
    
    # Test TextTokenizationEngine
    from santok_complete import TextTokenizationEngine
    print("\n✅ TextTokenizationEngine imported")
    
    engine = TextTokenizationEngine()
    print("✅ Engine created")
    
    # Test tokenization
    text = "Hello World! This is SanTOK."
    result = engine.tokenize(text, tokenization_method="whitespace")
    print(f"✅ Tokenization successful")
    print(f"   Input: '{text}'")
    print(f"   Tokens generated: {len(result.get('tokens', []))}")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! Module is working!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

