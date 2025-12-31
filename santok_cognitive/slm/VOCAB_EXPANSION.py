"""
Vocabulary Expansion - Add General English Words
================================================

Expands vocabulary to 5K-8K tokens by adding general English glue words
while keeping SanTOK-specific terms intact.
"""

# Common English words that help with grammar and coherence
GENERAL_ENGLISH_WORDS = [
    # Articles and determiners
    "the", "a", "an", "this", "that", "these", "those", "some", "any", "all", "each", "every",
    
    # Pronouns
    "it", "its", "they", "them", "their", "we", "our", "you", "your", "he", "she", "his", "her",
    
    # Common verbs
    "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "can", "could", "will", "would", "should", "may", "might", "must",
    "get", "got", "make", "made", "take", "took", "give", "gave", "go", "went", "come", "came",
    "see", "saw", "know", "knew", "think", "thought", "say", "said", "tell", "told",
    "work", "works", "worked", "use", "uses", "used", "need", "needs", "needed",
    "want", "wants", "wanted", "try", "tries", "tried", "help", "helps", "helped",
    
    # Common nouns
    "way", "ways", "time", "times", "thing", "things", "part", "parts", "kind", "kinds",
    "type", "types", "form", "forms", "method", "methods", "system", "systems",
    "process", "processes", "result", "results", "example", "examples", "case", "cases",
    "way", "ways", "point", "points", "level", "levels", "step", "steps",
    
    # Adjectives
    "good", "better", "best", "bad", "worse", "worst", "new", "old", "large", "small",
    "big", "little", "high", "low", "long", "short", "wide", "narrow", "fast", "slow",
    "easy", "hard", "simple", "complex", "important", "useful", "different", "same",
    "first", "last", "next", "previous", "current", "recent", "early", "late",
    
    # Adverbs
    "very", "quite", "rather", "too", "so", "more", "most", "less", "least",
    "also", "too", "either", "neither", "only", "just", "even", "still", "yet",
    "already", "again", "once", "twice", "always", "never", "often", "sometimes",
    "usually", "rarely", "here", "there", "where", "when", "how", "why", "what",
    
    # Prepositions
    "in", "on", "at", "by", "for", "with", "from", "to", "of", "about", "into", "onto",
    "over", "under", "above", "below", "between", "among", "through", "during",
    "before", "after", "since", "until", "while", "within", "without",
    
    # Conjunctions
    "and", "or", "but", "nor", "so", "yet", "because", "since", "although", "though",
    "if", "unless", "when", "where", "while", "as", "than",
    
    # Common technical/descriptive words
    "data", "information", "value", "values", "number", "numbers", "set", "sets",
    "list", "lists", "array", "arrays", "object", "objects", "field", "fields",
    "function", "functions", "feature", "features", "property", "properties",
    "element", "elements", "component", "components", "module", "modules",
    "structure", "structures", "format", "formats", "pattern", "patterns",
    
    # Action words
    "create", "creates", "created", "generate", "generates", "generated",
    "build", "builds", "built", "make", "makes", "made", "produce", "produces", "produced",
    "process", "processes", "processed", "handle", "handles", "handled",
    "manage", "manages", "managed", "control", "controls", "controlled",
    "perform", "performs", "performed", "execute", "executes", "executed",
    "implement", "implements", "implemented", "provide", "provides", "provided",
    "support", "supports", "supported", "enable", "enables", "enabled",
    "allow", "allows", "allowed", "require", "requires", "required",
    
    # Descriptive/qualitative words
    "effective", "efficient", "powerful", "flexible", "robust", "reliable",
    "accurate", "precise", "correct", "proper", "appropriate", "suitable",
    "complete", "comprehensive", "full", "partial", "limited", "extensive",
    "basic", "advanced", "simple", "complex", "detailed", "general",
    "specific", "particular", "special", "unique", "common", "standard",
    
    # Comparison words
    "similar", "different", "same", "equal", "equivalent", "comparable",
    "better", "worse", "improved", "enhanced", "optimized", "refined",
    
    # Time/sequence words
    "then", "now", "before", "after", "during", "while", "when", "once",
    "first", "second", "third", "next", "previous", "last", "final",
    "initial", "original", "new", "old", "recent", "current", "future",
    
    # Quantity words
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "many", "few", "several", "multiple", "single", "double", "triple",
    "more", "less", "most", "least", "all", "none", "some", "any",
    
    # Question words
    "what", "which", "who", "whom", "whose", "where", "when", "why", "how",
    
    # Common phrases/connectors
    "such", "as", "like", "unlike", "instead", "rather", "however", "therefore",
    "thus", "hence", "furthermore", "moreover", "additionally", "besides",
    "although", "though", "despite", "regardless", "whether",
]

def add_general_english_to_texts(texts: list, ratio: float = 0.35) -> list:
    """
    Add general English sentences to training data to help model learn grammar.
    This creates a mixed corpus: SanTOK-specific + general English.
    
    Args:
        texts: SanTOK-specific training texts
        ratio: Ratio of grammar examples (0.35 = 35% grammar, 65% SanTOK)
    """
    # Simple grammatical sentences
    grammar_examples = [
        "This is how it works.",
        "Here is what you need to know.",
        "The system can handle this task.",
        "It provides many useful features.",
        "You can use it for various purposes.",
        "The process is simple and effective.",
        "This makes it easy to use.",
        "It supports multiple file types.",
        "The result is accurate and reliable.",
        "This enables better performance.",
        "It works with different systems.",
        "The method is proven and tested.",
        "This allows for flexible usage.",
        "It handles complex scenarios.",
        "The approach is straightforward.",
        "This gives you more control.",
        "It processes data efficiently.",
        "The output is clear and useful.",
        "This helps you get better results.",
        "It integrates with other tools.",
    ]
    
    # Compound grammar patterns (teaches sentence linking)
    compound_grammar = [
        "This is how the system works in practice.",
        "It does this by combining several components together.",
        "As a result, the process becomes more efficient.",
        "This means that the system can handle complex cases.",
        "In other words, it simplifies the overall workflow.",
        "Because of this design, performance improves significantly.",
        "Although the process is complex, the usage remains simple.",
        "When this happens, the output becomes more reliable.",
        "The system works well because it uses efficient methods.",
        "Since the approach is flexible, it adapts to different needs.",
        "While the system is powerful, it remains easy to use.",
        "If you need this feature, the system provides it.",
        "Even though it's complex, the interface stays simple.",
        "Once you understand this, everything becomes clear.",
        "After the process completes, you get the results.",
    ]
    
    # Combine all grammar examples
    all_grammar = grammar_examples + compound_grammar
    
    # Calculate how many grammar examples to add
    # ratio = grammar_count / (sanTOK_count + grammar_count)
    # grammar_count = ratio * sanTOK_count / (1 - ratio)
    sanTOK_count = len(texts)
    grammar_count = int(sanTOK_count * ratio / (1 - ratio))
    
    # Mix grammar examples with SanTOK data
    expanded = texts.copy()
    expanded.extend(all_grammar * (grammar_count // len(all_grammar) + 1))
    
    # Trim to exact ratio
    total_target = int(sanTOK_count / (1 - ratio))
    return expanded[:total_target]


if __name__ == "__main__":
    print("=" * 70)
    print("Vocabulary Expansion - General English Words")
    print("=" * 70)
    print()
    print(f"General English words available: {len(GENERAL_ENGLISH_WORDS)}")
    print()
    print("These words will be added to vocabulary during training.")
    print("They help the model learn grammar and coherence.")
    print()
    print("Sample words:")
    for i, word in enumerate(GENERAL_ENGLISH_WORDS[:30], 1):
        print(f"  {word}", end="  ")
        if i % 10 == 0:
            print()
    print()
    print("=" * 70)
