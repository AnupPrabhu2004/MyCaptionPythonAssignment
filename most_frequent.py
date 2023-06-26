def most_frequent(string):
    # Create an empty dictionary to store the frequency of each letter
    letter_freq = {}

    # Count the frequency of each letter in the string
    for letter in string:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1

    # Sort the dictionary by value in descending order
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for letter, freq in sorted_freq:
        print(letter, '=', str(freq).zfill(2), end=' ')

# Example usage
input_string = input("Please enter a string: ")
most_frequent(input_string)
