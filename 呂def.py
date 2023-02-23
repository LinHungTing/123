# -*- coding: utf-8 -*-
def main():
    listOfWords = formListOfWords ("Gettysburg.txt")
    freq = creatFrequencyDictionary (listOfWords)
    displayWordCount (listOfWords, freq)
    displayMostCommonWords (freq)
    
def formListOfWords(fileName):
    infile = open(fileName , "r" , encoding="utf-8")
    originaLine = infile.read().lower()
    line = ""
    for ch in originaLine:
        if ("a" <= ch <= "z") or (ch == " "):
            line += ch
    listOfWords = line.split()
    return listOfWords

def creatFrequencyDictionary(listOfWords):
    freq = {}
    for word in listOfWords:
        freq[word] = 0
    for word in listOfWords:
        freq[word] = freq[word] + 1
    return freq

def displayWordCount (listofWords, freq) :
    print ("The Gettysburg Address contains", len (listofWords), "words.")
    print ("The Gettysburg Address contains", len (freq), "different words.")
    print ()

def displayMostCommonWords (freq) :
    print ("The most common words and their frequencies are:")
    listOfMostCommonWords= []
    for word in freq.keys ():
        if freq[word] >= 6:
            listOfMostCommonWords.append((word , freq[word]))
    listOfMostCommonWords.sort(key = lambda x : x[1] , reverse = True)
    for item in listOfMostCommonWords:
        print("  " , item[0] + ":" , item[1])

main()
