def isPalindrome(text):
    for i in range(0, int(len(text)/2)):
        if text[i] != text[len(text) - (i + 1)]:
            return False
    return True

text = input()
print(isPalindrome(text))