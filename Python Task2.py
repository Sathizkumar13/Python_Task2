1.	Python program that calculates the total number of vowels and the count of each individual vowel (A, E, I, O, U) in the given string "Guvi Geeks Network Private Limited

def count_vowels(s):
#Convert the String to Upper case 
    s = s.upper()
#Define Vowels
    vowel_counts = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    for char in s:
        if char in vowel_counts:
            vowel_counts[char] += 1
    
    total_vowels = sum(vowel_counts.values())
    
    return total_vowels, vowel_counts
#Define the String
input_string = "Guvi Geeks Network Private Limited"

total_vowels, vowel_counts = count_vowels(input_string)

print(f"Total number of vowels: {total_vowels}")
print("Count of each vowel:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")

2.	Crete a Pyramid of Numbers from 1 to 20 using For loop?

def print_pyramid(n):
    current_num = 1
    for i in range(1, n+1):
        for _ in range(n-i):
            print(" ", end=" ")
        for _ in range(i):
            if current_num > 20:
                break
            print(current_num, end=" ")
            current_num += 1
        print()  # New line after each row
print_pyramid(20)


3.	Write a program that takes a string and returns a new string with all the vowels removed.

#Define Vowels
def remove_vowels(s):
    vowels = "AEIOUaeiou"
    result = ""
# Create a new string excluding vowels    
    for char in s:
        if char not in vowels:
            result += char
    
    return result
# Test the function with an example string
input_string = "Guvi Geeks Network Private Limited"

output_string = remove_vowels(input_string)

print("Original string:", input_string)
print("String with vowels removed:", output_string)	

4.	Write a program that takes a string and returns the number of unique characters in it.

def count_unique_characters(s):
 # Characters to store only unique ones
    unique_chars = set(s)
# Return the number of unique characters
    return len(unique_chars)
# Test the function with an example string
input_string = "Guvi Geeks Network Private Limited"
unique_char_count = count_unique_characters(input_string)

print("Original string:", input_string)
print("Number of unique characters:", unique_char_count)



5.	Write a program that takes a string and returns True if it is a palindrome, False otherwise.

def is_palindrome(s):
# Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
# Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
# Test the function with an example string
test_strings = [
    "A man, a plan, a canal, Panama",
    "racecar",
    "hello",
    "No 'x' in Nixon",
    "Was it a car or a cat I saw?"
]
for test in test_strings:
    print(f"'{test}' -> {is_palindrome(test)}")
    

6.	Write a program that takes two strings and return the longest common substring between them.

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    # Create a 2D list to store lengths of longest common suffixes of substrings
    # dp[i][j] will store the length of longest common substring ending with str1[i-1] and str2[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
    return str1[end_index - max_length: end_index]
# Test the function with example strings
str1 = " GuviGeeks"
str2 = " NetworkGeeks"
print("Longest common substring:", longest_common_substring(str1, str2))


7.	Write a program that takes a string and returns the most frequent character in it.

def most_frequent_character(input_string):
    char_frequency = {}
# Create a counter object to count the frequency of each character
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    max_frequency = 0
# Find the character with the highest frequency
    most_frequent_char = ''
    for char, freq in char_frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            most_frequent_char = char

    return most_frequent_char

# Test the function with an example string
input_string = "hello world"
print("Most frequent character:", most_frequent_character(input_string))


8.	Write a program that takes a string and returns True if it is an anagram of another string, False otherwise.

def are_anagrams(str1, str2):
 # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
# Compare the frequency of characters in both strings using Counter
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
# Function with example strings
string1 = "listen"
string2 = "silent"
print("Are they anagrams?", are_anagrams(string1, string2))


9.	Write a program that takes a string and returns the number of words in it.

def count_words(input_string):
    words_list = input_string.split()
# Return the number of words
    return len(words_list)

# Example usage:
input_string = "Hello, this is a sample string."
print("Number of words:", count_words(input_string))


