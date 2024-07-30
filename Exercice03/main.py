words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1

    return vowel_count


for word in words:
    result = count_vowels(word)
    print(result)
