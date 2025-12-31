#!/usr/bin/env python
"""
SanTOK SLM - Run this to use the SLM
"""

from santok_slm import SanTOKSLM

def main():
    print("=" * 60)
    print("SanTOK SLM - Running Now")
    print("=" * 60)
    print()
    
    # Create SLM
    print("Creating SLM...")
    slm = SanTOKSLM()
    print("SLM created")
    print()
    
    # Load facts
    print("Loading facts...")
    facts = [
        "Python is a programming language",
        "Python was created by Guido van Rossum",
        "Python is used for web development and data science",
        "Python has a simple and readable syntax",
        "Python supports multiple programming paradigms",
    ]
    slm.load_facts(facts)
    print(f"Loaded {len(facts)} facts")
    print()
    
    # Generate responses
    print("=" * 60)
    print("GENERATING RESPONSES")
    print("=" * 60)
    print()
    
    questions = [
        "What is Python?",
        "Who created Python?",
        "What is Python used for?",
    ]
    
    for question in questions:
        print(f"Q: {question}")
        answer = slm.generate(question, max_length=20)
        print(f"A: {answer}")
        print()
    
    # Show stats
    print("=" * 60)
    print("STATISTICS")
    print("=" * 60)
    stats = slm.get_stats()
    print(f"Facts: {stats.get('fact_count', 'N/A')}")
    print(f"Vocabulary: {stats.get('vocab_size', 'N/A')}")
    print()
    print("SLM is ready to use!")
    print("=" * 60)

if __name__ == "__main__":
    main()
