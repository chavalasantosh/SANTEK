#!/usr/bin/env python3
"""
Quick System Check for SanTOK LLM Development
Checks system capabilities and dependencies
"""

import sys
import platform
import os

print("=" * 70)
print("SanTOK System Capability Check")
print("=" * 70)
print()

# Python version
python_version = sys.version_info
print(f"[OK] Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
if python_version >= (3, 11):
    print("   Status: Compatible (3.11+ required)")
else:
    print("   [WARN] Warning: Python 3.11+ recommended")
print()

# Platform info
print(f"[OK] Platform: {platform.system()} {platform.release()}")
print(f"[OK] Architecture: {platform.machine()}")
print()

# Check dependencies
print("Checking Dependencies:")
print("-" * 70)

dependencies = {
    "numpy": "Core requirement for SLM",
    "tensorflow": "Optional - for hybrid embeddings",
    "fastapi": "Optional - for API server",
    "pandas": "Optional - for data processing",
    "sentence-transformers": "Optional - for hybrid embeddings",
}

installed = []
missing = []

for dep, desc in dependencies.items():
    try:
        mod = __import__(dep)
        version = getattr(mod, '__version__', 'unknown')
        print(f"  [OK] {dep:25} {version:15} - {desc}")
        installed.append(dep)
    except ImportError:
        print(f"  [WARN] {dep:25} {'Not installed':15} - {desc}")
        missing.append(dep)

print()
print("=" * 70)
print("System Summary")
print("=" * 70)

# Check CPU info
try:
    import psutil
    cpu_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    print(f"[OK] CPU Cores (Logical): {cpu_count}")
    if cpu_freq:
        print(f"[OK] CPU Frequency: {cpu_freq.current:.0f} MHz")
except ImportError:
    print("[WARN] psutil not installed - cannot check CPU details")

# Check RAM
try:
    import psutil
    ram = psutil.virtual_memory()
    ram_gb = ram.total / (1024**3)
    ram_available_gb = ram.available / (1024**3)
    print(f"[OK] Total RAM: {ram_gb:.2f} GB")
    print(f"[OK] Available RAM: {ram_available_gb:.2f} GB")
    
    if ram_gb >= 8:
        print("   Status: [OK] Sufficient for all SLM models")
    elif ram_gb >= 4:
        print("   Status: [OK] Sufficient for showcase/improved SLM")
    else:
        print("   Status: [WARN] Limited - only showcase SLM recommended")
except ImportError:
    print("[WARN] psutil not installed - cannot check RAM")

print()
print("=" * 70)
print("LLM Development Capabilities")
print("=" * 70)
print()

if "numpy" in installed:
    print("[OK] Ready for SLM Development!")
    print()
    print("Recommended Models:")
    print("  1. Showcase SLM (10-30 min, 2-4 GB RAM)")
    print("  2. Improved SLM (1-2 hours, 4-8 GB RAM)")
    print("  3. Full GPT-Style (4-8 hours, 8-12 GB RAM)")
    print()
    print("Next Steps:")
    print("  cd santok_cognitive/slm")
    print("  python SHOWCASE_SLM.py")
else:
    print("[WARN] NumPy not installed - required for SLM development")
    print()
    print("Install with:")
    print("  pip install numpy")

print()
print("=" * 70)
