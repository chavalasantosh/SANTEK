"""
Load External Training Data
===========================

Helper functions to load and integrate external training data
(Wikipedia, books, ArXiv, etc.) with SanTOK training pipeline.
"""

import os
from typing import List


def load_text_file(file_path: str, max_lines: int = None) -> List[str]:
    """
    Load sentences from a text file (one sentence per line).
    
    Args:
        file_path: Path to text file
        max_lines: Maximum lines to load (None = all)
    
    Returns:
        List of sentences
    """
    if not os.path.exists(file_path):
        print(f"[WARNING] File not found: {file_path}")
        return []
    
    sentences = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f):
            if max_lines and i >= max_lines:
                break
            
            line = line.strip()
            if line and 10 <= len(line) <= 500:  # Filter by length
                sentences.append(line)
    
    print(f"[OK] Loaded {len(sentences):,} sentences from {file_path}")
    return sentences


def load_multiple_files(file_paths: List[str], max_per_file: int = None) -> List[str]:
    """
    Load sentences from multiple text files.
    
    Args:
        file_paths: List of file paths
        max_per_file: Maximum sentences per file (None = all)
    
    Returns:
        Combined list of sentences
    """
    all_sentences = []
    
    for file_path in file_paths:
        if os.path.exists(file_path):
            sentences = load_text_file(file_path, max_lines=max_per_file)
            all_sentences.extend(sentences)
        else:
            print(f"[WARNING] Skipping missing file: {file_path}")
    
    print(f"[OK] Total sentences loaded: {len(all_sentences):,}")
    return all_sentences


def mix_santok_and_external(santok_texts: List[str], external_texts: List[str], 
                            santok_ratio: float = 0.65) -> List[str]:
    """
    Mix SanTOK-specific texts with external data.
    
    Args:
        santok_texts: SanTOK-specific training texts
        external_texts: External training texts (Wikipedia, books, etc.)
        santok_ratio: Ratio of SanTOK texts (0.65 = 65% SanTOK, 35% external)
    
    Returns:
        Mixed list of texts
    """
    # Calculate how many external texts to include
    # santok_ratio = santok_count / (santok_count + external_count)
    # external_count = santok_count * (1 - santok_ratio) / santok_ratio
    santok_count = len(santok_texts)
    target_external_count = int(santok_count * (1 - santok_ratio) / santok_ratio)
    
    # Limit external texts
    if len(external_texts) > target_external_count:
        import random
        external_texts = random.sample(external_texts, target_external_count)
    
    # Mix
    mixed = santok_texts.copy()
    mixed.extend(external_texts)
    
    # Shuffle
    import random
    random.shuffle(mixed)
    
    print(f"[OK] Mixed {len(santok_texts):,} SanTOK + {len(external_texts):,} external = {len(mixed):,} total")
    print(f"     Ratio: {len(santok_texts)/len(mixed)*100:.1f}% SanTOK / {len(external_texts)/len(mixed)*100:.1f}% external")
    
    return mixed


if __name__ == "__main__":
    print("=" * 70)
    print("External Data Loader")
    print("=" * 70)
    print()
    print("This module provides functions to load external training data.")
    print()
    print("Usage in TRAIN_IMPROVED_SLM.py:")
    print()
    print("  from LOAD_EXTERNAL_DATA import load_text_file, mix_santok_and_external")
    print()
    print("  # Load external data")
    print("  external_texts = load_text_file('wikipedia_text.txt', max_lines=50000)")
    print()
    print("  # Mix with SanTOK data")
    print("  all_texts = mix_santok_and_external(santok_texts, external_texts, santok_ratio=0.65)")
    print()
