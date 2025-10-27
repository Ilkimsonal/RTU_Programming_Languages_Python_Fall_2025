import re


def count_characters(text):
    """Count non-space characters in a string."""
    return len([ch for ch in text if not ch.isspace()])


def count_words(text):
    """Count words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Extract all numbers (integers or floats) from the text."""
    numbers = re.findall(r"\d+(?:\.\d+)?", text)
    return [float(num) for num in numbers]


def analyze_text(text):
    """Analyze text: characters, words, sum and average of numbers."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
    else:
        total = 0
        average = 0

    return char_count, word_count, total, average


if __name__ == "__main__":
    text = input("Enter some text: ")
    char_count, word_count, total, average = analyze_text(text)

    print("\n--- Text Analysis Summary ---")
    print(f"Non-space characters: {char_count}")
    print(f"Word count: {word_count}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {average}")


def count_words(text):
    """Count number of words in a string."""
    # TODO: implement
    pass


def extract_numbers(text):
    """Return list of integers found in text."""
    # TODO: implement
    pass


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    pass


if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    pass
