def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage:
test_str1 = "listen"
test_str2 = "silent"

# Print the result of the function call
print(are_anagrams(test_str1, test_str2))
