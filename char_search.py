# List of words
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Function to return words containing the given character
def words_with_char(char,words_list):
    # Ensure the input is a single character
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    
    # Find and return words containing the character
    # result = [word for word in words_list if char in word]
    result = []
    for word in words_list:
        if char in word:
            result.append(word)
    return result

# Example usage
char = 's'
words_containing_char = words_with_char(char,words_list)
print(f"Words containing '{char}': {words_containing_char}")

char = 'd'
words_containing_char = words_with_char(char,words_list)
print(f"Words containing '{char}': {words_containing_char}")
