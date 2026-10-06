def is_palindrome_recursive(word: str):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1])

print(is_palindrome_recursive("radar"))
print(is_palindrome_recursive("hello"))