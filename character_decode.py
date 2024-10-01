def decode_string(encoded_str):
    """
    Decodes an encoded string where each character is followed by a number
    indicating how many times the character should be repeated.

    Parameters:
    encoded_str (str): The encoded string (e.g., 'a6b4c8d3').

    Returns:
    str: The decoded string (e.g., 'aaaaaabbbbccccccccddd').
    """
    result = ""  # Initialize an empty result string
    i = 0  # Initialize the index to iterate through the encoded string

    while i < len(encoded_str):
        char = encoded_str[i]  # Extract the current character
        i += 1  # Move to the next character
        count = ""  # Initialize an empty string to store the count

        # Extract the digits following the character to determine the count
        while i < len(encoded_str) and encoded_str[i].isdigit():
            count += encoded_str[i]
            i += 1

        # Repeat the character by the extracted count and append to the result
        result += char * int(count)

    return result  # Return the decoded string

# Example usage
encoded_str = "a6b4c8d3"
print(decode_string(encoded_str))  # Output: 'aaaaaabbbbccccccccddd'
