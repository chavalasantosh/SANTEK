"""
Quick test of SanTOK SLM - just run this to see it work
"""

from santok_slm import SanTOKSLM

def main():
    print("=" * 60)
    print("SanTOK SLM - Quick Test")
    print("=" * 60)
    print()
    
    # Create SLM
    slm = SanTOKSLM()
    
    # Load some facts
    facts = [
        "Python is a programming language",
        "Python was created by Guido van Rossum",
        "Python is used for web development and data science",
        "Python has a simple syntax",
    ]
    
    print("Loading facts...")
    slm.load_facts(facts)
    print("Done!\n")
    
    # Ask questions
    questions = [
        "What is Python?",
        "Who created Python?",
        "What is Python used for?",
    ]
    
    for question in questions:
        print(f"Q: {question}")
        answer = slm.generate(question)
        print(f"A: {answer}")
        print()
    
    print("=" * 60)
    print("That's it! The SLM works.")
    print("=" * 60)

if __name__ == "__main__":
    main()
