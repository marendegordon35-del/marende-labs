# string reversal
def reverse_string(text):
    reversed_text = ""
    for i in range(len(text) -1, -1, -1):
        reversed_text += text[i]
    return reversed_text
# Character frequency
def character_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
# Test
word = "Taboo"

print("Original:",word)
print("Reversed:", reverse_string(word))
print("Frequency:", character_frequency(word))