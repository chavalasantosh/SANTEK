"""
Extract Text from Wikipedia Dump
=================================

Downloads and extracts plain text from Wikipedia XML dump.
Perfect for training data - high quality, diverse topics.
"""

import os
import sys
import re
from pathlib import Path

try:
    import bz2
    import xml.etree.ElementTree as ET
except ImportError:
    print("[ERROR] Missing required modules. Install: pip install bz2")
    sys.exit(1)


def extract_text_from_wiki_xml(xml_file: str, output_file: str, max_sentences: int = 100000):
    """
    Extract plain text sentences from Wikipedia XML dump.
    
    Args:
        xml_file: Path to Wikipedia XML file (.xml or .xml.bz2)
        output_file: Output text file (one sentence per line)
        max_sentences: Maximum sentences to extract
    """
    print("=" * 70)
    print("Wikipedia Text Extractor")
    print("=" * 70)
    print()
    print(f"Input: {xml_file}")
    print(f"Output: {output_file}")
    print(f"Max sentences: {max_sentences:,}")
    print()
    
    # Check if file exists
    if not os.path.exists(xml_file):
        print(f"[ERROR] File not found: {xml_file}")
        print()
        print("Download Wikipedia dump from:")
        print("  https://dumps.wikimedia.org/enwiki/latest/")
        print()
        print("Recommended file (BEST for training):")
        print("  enwiki-latest-pages-articles.xml.bz2")
        print("  (~24.7 GB, complete dataset)")
        print()
        print("Direct link:")
        print("  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2")
        return False
    
    # Open file (handle .bz2 compression)
    if xml_file.endswith('.bz2'):
        print("Decompressing .bz2 file...")
        file_handle = bz2.open(xml_file, 'rt', encoding='utf-8', errors='ignore')
    else:
        file_handle = open(xml_file, 'r', encoding='utf-8', errors='ignore')
    
    sentences = []
    page_count = 0
    text_count = 0
    
    print("Extracting text from Wikipedia XML...")
    print("(This may take 10-30 minutes depending on file size)")
    print()
    
    try:
        # Parse XML incrementally
        context = ET.iterparse(file_handle, events=('start', 'end'))
        context = iter(context)
        event, root = next(context)
        
        for event, elem in context:
            if event == 'end' and elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}page':
                # Extract text from page
                text_elem = elem.find('.//{http://www.mediawiki.org/xml/export-0.10/}text')
                if text_elem is not None and text_elem.text:
                    text = text_elem.text
                    
                    # Clean and split into sentences
                    cleaned = clean_wiki_text(text)
                    page_sentences = split_into_sentences(cleaned)
                    
                    for sent in page_sentences:
                        if is_valid_sentence(sent):
                            sentences.append(sent)
                            text_count += 1
                            
                            if text_count % 1000 == 0:
                                print(f"  Extracted {text_count:,} sentences...", end='\r')
                            
                            if len(sentences) >= max_sentences:
                                break
                    
                    page_count += 1
                    if page_count % 100 == 0:
                        print(f"  Processed {page_count:,} pages, {len(sentences):,} sentences...", end='\r')
                
                # Clear element to save memory
                elem.clear()
                root.clear()
                
                if len(sentences) >= max_sentences:
                    break
    
    except Exception as e:
        print(f"\n[ERROR] Extraction error: {e}")
        return False
    finally:
        file_handle.close()
    
    # Write sentences to file
    print()
    print(f"\nWriting {len(sentences):,} sentences to {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for sent in sentences:
            f.write(sent + '\n')
    
    print()
    print("=" * 70)
    print("[OK] Extraction Complete!")
    print("=" * 70)
    print()
    print(f"Pages processed: {page_count:,}")
    print(f"Sentences extracted: {len(sentences):,}")
    print(f"Output file: {os.path.abspath(output_file)}")
    print(f"File size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    print()
    print("You can now use this file in TRAIN_IMPROVED_SLM.py!")
    print()
    
    return True


def clean_wiki_text(text: str) -> str:
    """Clean Wikipedia text - remove markup, templates, etc."""
    # Remove wiki markup patterns
    text = re.sub(r'{{.*?}}', '', text)  # Templates
    text = re.sub(r'\[\[.*?\|(.*?)\]\]', r'\1', text)  # Links with pipe
    text = re.sub(r'\[\[(.*?)\]\]', r'\1', text)  # Simple links
    text = re.sub(r'\[.*?\]', '', text)  # External links
    text = re.sub(r'<.*?>', '', text)  # HTML tags
    text = re.sub(r'==+.*?==+', '', text)  # Headers
    text = re.sub(r'\'\'\'', '', text)  # Bold/italic
    text = re.sub(r'\'\'', '', text)  # Italic
    text = re.sub(r'^\*+', '', text, flags=re.MULTILINE)  # List markers
    text = re.sub(r'^\#+', '', text, flags=re.MULTILINE)  # Numbered lists
    text = re.sub(r'^\|+', '', text, flags=re.MULTILINE)  # Table markers
    
    # Clean whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text


def split_into_sentences(text: str) -> list:
    """Split text into sentences."""
    # Simple sentence splitting (can be improved)
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]


def is_valid_sentence(sentence: str) -> bool:
    """Check if sentence is valid for training."""
    # Length check
    if len(sentence) < 10 or len(sentence) > 500:
        return False
    
    # Word count
    words = sentence.split()
    if len(words) < 3 or len(words) > 100:
        return False
    
    # Check for too many special chars
    if sentence.count('[') > 2 or sentence.count('{') > 2:
        return False
    
    # Check for valid characters
    if not re.search(r'[a-zA-Z]', sentence):
        return False
    
    return True


if __name__ == "__main__":
    print("=" * 70)
    print("Wikipedia Data Extractor")
    print("=" * 70)
    print()
    print("This script extracts plain text from Wikipedia XML dumps.")
    print()
    print("Step 1: Download Wikipedia dump")
    print("  URL: https://dumps.wikimedia.org/enwiki/latest/")
    print("  Recommended: enwiki-latest-pages-articles.xml.bz2 (24.7 GB)")
    print("  Direct: https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2")
    print()
    print("Step 2: Run this script")
    print("  python EXTRACT_WIKIPEDIA_DATA.py")
    print()
    print("Step 3: Use extracted text in training")
    print("  Add to TRAIN_IMPROVED_SLM.py")
    print()
    
    # Example usage
    if len(sys.argv) >= 2:
        xml_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) >= 3 else 'wikipedia_text.txt'
        max_sentences = int(sys.argv[3]) if len(sys.argv) >= 4 else 100000
        
        extract_text_from_wiki_xml(xml_file, output_file, max_sentences)
    else:
        print("Usage:")
        print("  python EXTRACT_WIKIPEDIA_DATA.py <wikipedia.xml.bz2> [output.txt] [max_sentences]")
        print()
        print("Example:")
        print("  python EXTRACT_WIKIPEDIA_DATA.py enwiki-latest-pages-articles.xml.bz2 wikipedia_text.txt 1000000")
        print()
