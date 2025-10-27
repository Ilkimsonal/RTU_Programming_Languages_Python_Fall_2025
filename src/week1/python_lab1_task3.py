def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    length = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return length, word_count, contains_python


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    length, word_count, contains_python = analyze_sentence(sentence)

    print(f"Total character count: {length}")
    print(f"Word count: {word_count}")
    print(f"Does it contain 'Python'?: {'Yes' if contains_python else 'No'}")
