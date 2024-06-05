# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        # Sort the characters of the word to create a reference
        sorted_word = sorted(self.word)
        
        # List to hold the anagrams found
        matches = []

        # Iterate over each word in the provided list
        for word in words:
            # Compare sorted characters of the current word with the reference
            if sorted(word) == sorted_word:
                matches.append(word)

        return matches

listen = Anagram ("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
