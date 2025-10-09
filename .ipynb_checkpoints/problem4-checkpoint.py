"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):

    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    
    with open(filename, 'r') as f:
        text = f.read()
        
    return len(text.split())


def count_lines(filename):
    
    with open(filename, 'r') as f:
        line_count = 0
        for line in filename:
            line_count += 1
        return line_count

def count_characters(filename, include_spaces=True):
    characters_count = 0
    with open(filename, 'r') as f:
        for line in f:
            if include_spaces:
                characters_count += len(line)
            else:
                for ch in line:
                    if not ch.isspace(): 
                        characters_count += 1
    return characters_count
        

import string

def find_longest_word(filename):
    longest_word = ""
    with open(filename, 'r') as f: 
        for line in f:  # <-- corrected here
            line = line.strip()  
            for word in line.split():
                word = word.strip(string.punctuation)
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def word_frequency(filename):
    import string

    frequency = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            for word in line.split():
                word = word.lower()
                word = word.strip(string.punctuation)
                if not word:
                    continue
                if word not in frequency:
                    frequency[word] = 1
                else:
                    frequency[word] += 1

    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()