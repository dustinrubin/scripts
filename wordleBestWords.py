from collections import Counter

from english_words import english_words_lower_alpha_set

fiveLetterWords = [word for word in  english_words_lower_alpha_set if len(word) == 5]

def scoreLetters(words):
    letterCount = Counter()
    for word in words:
        for letter in word:
            letterCount[letter] += 1
    return letterCount

def wordsWithoutDuplicateLetters(words):
    return set(word for word in words if len(set(word)) == 5)

def scoreWords(checkWords, allWords):
    wordScores = Counter()

    for word in allWords:
        for checkWord in checkWords:
            wordMatched = False
            if word == checkWord:
                continue
            for index in range(5):
                if checkWord[index] == word[index]:
                    wordMatched = True
                    break
            if wordMatched:
                wordScores[checkWord] += 1
    return wordScores

def scoreWordsLetterOverlap(checkWords, allWords):
    wordScores = Counter()

    for word in allWords:
        for checkWord in checkWords:
            if word == checkWord:
                continue
            for index in range(5):
                if checkWord[index] == word[index]:
                    wordScores[checkWord] += 1
                
    return wordScores

letterScore = scoreLetters(fiveLetterWords)
def getLetterOrder(words):
    scoreLetters(words)
    letterOrder = [letter for letter, _ in letterScore.most_common(26)]
    return letterOrder

def rankLettersOfWord(word, letterOrder):
    print("Ranking letters in", word)
    for letter in word:
        letterPosition = letterOrder.index(letter) + 1
        print("Letter", letter, "is rank", letterPosition)

print("The most common letters are", letterScore.most_common(6))
print("The words with the most matches are",  scoreWords(fiveLetterWords, fiveLetterWords).most_common(3))
print("The most overlapping words are",  scoreWordsLetterOverlap(fiveLetterWords, fiveLetterWords).most_common(3))
print("Score of each letter in saute", letterScore["s"], letterScore["a"], letterScore["u"], letterScore["t"], letterScore["e"])
print("Letter order",  getLetterOrder(fiveLetterWords))
rankLettersOfWord("saute", getLetterOrder(fiveLetterWords))

# rankLettersOfWord("sauce", getLetterOrder(fiveLetterWords))

