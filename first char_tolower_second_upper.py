#String: Hi I am John. Python Program: Convert first letter of each word into lower case and second letter as capital. If the word has only one letter convert that as lower case.

def transform_string(text):
  """Converts first letter of each word to lowercase and second to uppercase.

  Args:
    text: The input string.

  Returns:
    The transformed string.
  """
  words = text.split()
  transformed_words = []
  for word in words:
    if len(word) == 1:
      transformed_words.append(word.lower())
    else:
      transformed_words.append(word[0].lower() + word[1].upper() + word[2:])
  return " ".join(transformed_words)

string = "Hi I am John."
print(transform_string(string))  # Output: hI i Am jOhn.
